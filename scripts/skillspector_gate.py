#!/usr/bin/env python3
"""Advisory SkillSpector gate for the Skill Atlas CI.

Parses a SkillSpector JSON report and prints a compact, human-readable summary
to stdout (and to $GITHUB_STEP_SUMMARY when running in Actions).

Deliberately ADVISORY: it always exits 0. The atlas is a docs-only trust index,
so SkillSpector's static pass is high-recall / low-precision here (it flags text
that merely *names* dangerous things — see jobs/agent-skill-security.md for the
dogfood receipt). The report is a triage list for a human glance, not a build
gate. If this repo ever ships executable hooks/MCP servers, flip ADVISORY off.

Usage:
    skillspector scan <dir> --no-llm --format json --output report.json
    python3 scripts/skillspector_gate.py report.json
"""
import json
import os
import sys
from collections import Counter

ADVISORY = True  # always exit 0; the static pass is noisy on a pure-Markdown skill


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else "report.json"
    try:
        with open(path) as fh:
            report = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"skillspector-gate: could not read {path}: {exc}")
        return 0  # never break CI on our own tooling

    ra = report.get("risk_assessment", {})
    score = ra.get("score", "?")
    severity = ra.get("severity", "?")
    rec = ra.get("recommendation", "?")
    issues = report.get("issues", [])

    by_sev = Counter(i.get("severity", "?") for i in issues)
    # PNG/binary mis-reads are pure noise on a docs repo — count them separately.
    binary = [i for i in issues if str(i.get("location", {}).get("file", "")).endswith(
        (".png", ".jpg", ".jpeg", ".gif", ".ico", ".woff", ".woff2")
    )]
    text_issues = [i for i in issues if i not in binary]

    lines = []
    lines.append("## 🛡️ SkillSpector scan (advisory)")
    lines.append("")
    lines.append(f"- **score:** {score}/100 · **severity:** {severity} · "
                 f"**recommendation:** `{rec}`")
    lines.append(f"- **issues:** {len(issues)} "
                 f"({', '.join(f'{k}:{v}' for k, v in sorted(by_sev.items())) or 'none'})")
    if binary:
        lines.append(f"- **{len(binary)} are binary-asset mis-reads** (PNG bytes "
                     f"parsed as source) — ignored.")
    lines.append("")
    lines.append("> Advisory only — this atlas is a docs-only trust index, so the "
                 "static pass over-flags text that merely *names* risky things. "
                 "See `jobs/agent-skill-security.md` for why. CI is never failed by "
                 "this step; a human triages the list below.")
    lines.append("")

    if text_issues:
        lines.append("| sev | category | file:line | match |")
        lines.append("|-----|----------|-----------|-------|")
        for i in sorted(text_issues, key=lambda x: x.get("location", {}).get("file", "")):
            loc = i.get("location", {})
            f = loc.get("file", "?")
            ln = loc.get("start_line", "?")
            cat = i.get("category", "?")
            sev = i.get("severity", "?")
            match = (i.get("finding") or "").strip().replace("\n", " ").replace("|", "\\|")[:48]
            lines.append(f"| {sev} | {cat} | `{f}:{ln}` | `{match}` |")
    else:
        lines.append("_No text findings._")

    summary = "\n".join(lines)
    print(summary)

    gh_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if gh_summary:
        try:
            with open(gh_summary, "a") as fh:
                fh.write(summary + "\n")
        except OSError:
            pass

    if not ADVISORY and rec == "DO_NOT_INSTALL":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
