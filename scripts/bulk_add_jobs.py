#!/usr/bin/env python3
"""
bulk_add_jobs.py — render NEW job files from hand-curated specs with LIVE-verified
GitHub reputation. Never invents a number: every star count / push date / archived
flag is pulled this run via `gh`, and any repo that 404s is DROPPED from its job.

Why a custom meta fetch instead of atlas_common.graphql_repo_meta:
  `gh api graphql` exits non-zero whenever ANY repo in a batch is dead (NOT_FOUND in
  the errors[] array), even though valid data for the live repos is present in stdout.
  atlas_common.gh_json discards the whole chunk on rc!=0 -> every repo becomes "?".
  Here we parse stdout REGARDLESS of exit code, and read a null node as "drop it".

Input: JOBS list of specs (curated by hand — that's the judgment the atlas sells).
Output: writes jobs/<file>.md for each spec. Prints a report: live count, dropped repos.
"""
import json
import os
import subprocess
import sys

REPO_DIR = os.path.expanduser("~/Developer/skill-atlas")
JOBS_DIR = os.path.join(REPO_DIR, "jobs")
GH = "/opt/homebrew/bin/gh"
TODAY = "2026-06-22"

TIER_HEADERS = {
    "A": "## Tier A 🟢 — Canonical",
    "B": "## Tier B 🔵 — Community-proven",
    "C": "## Tier C 🟡 — Useful, verify",
    "D": "## Tier D 🔴 — Caution",
}
TIER_ORDER = ["A", "B", "C", "D"]


def fetch_meta(fulls):
    """{full -> (stars:int, pushed, archived:bool)} or full -> None if dead.
    Parses stdout even when gh exits non-zero (a dead repo in the batch causes rc=1)."""
    meta = {}
    uniq = sorted(set(fulls))
    CHUNK = 40
    for i in range(0, len(uniq), CHUNK):
        chunk = uniq[i:i + CHUNK]
        parts, idx = [], {}
        for j, full in enumerate(chunk):
            owner, name = full.split("/", 1)
            a = f"r{j}"
            idx[a] = full
            o = owner.replace('"', '\\"')
            n = name.replace('"', '\\"')
            parts.append(f'{a}: repository(owner:"{o}", name:"{n}"){{ stargazerCount pushedAt isArchived }}')
        q = "query{" + " ".join(parts) + "}"
        r = subprocess.run([GH, "api", "graphql", "-f", f"query={q}"],
                           capture_output=True, text=True, timeout=120)
        out = r.stdout.strip()
        if not out:
            for full in chunk:
                meta[full] = "ERR"
            continue
        try:
            data = json.loads(out).get("data", {})
        except Exception:
            for full in chunk:
                meta[full] = "ERR"
            continue
        for a, full in idx.items():
            node = data.get(a)
            if node is None:
                meta[full] = None
            else:
                meta[full] = (node.get("stargazerCount", 0),
                              (node.get("pushedAt") or "")[:10],
                              bool(node.get("isArchived", False)))
    return meta


def stars_fmt(n):
    return f"{n:,}★"


def render_entry(pick, meta):
    full = pick["full"]
    m = meta.get(full)
    if m is None or m == "ERR":
        return None
    stars, pushed, archived = m
    rep = f"{pick.get('rep', '')} · " if pick.get("rep") else ""
    rep += f"**{stars_fmt(stars)}** · pushed {pushed}"
    if archived:
        rep += " · ⚠️ ARCHIVED"
    src = f"https://github.com/{full}"
    if pick.get("extra_src"):
        src += f" ({pick['extra_src']})"
    return "\n".join([
        f"### {pick['name']}",
        pick["blurb"],
        f"- **source:** {src}",
        f"- **reputation:** {rep}",
        f"- **last_validated:** {TODAY}",
        f"- **assumes:** {pick['assumes']}",
        f"- **adapt:** {pick['adapt']}",
    ])


def render_job(spec, meta):
    body = [f"# Job: {spec['title']}", "", f"**You're about to:** {spec['intro']}", "",
            f"> Reputation pulled live **{TODAY}** via `gh api`.", ""]
    if spec.get("pairings"):
        body += [spec["pairings"], ""]
    body += ["---", ""]
    rendered = {t: [] for t in TIER_ORDER}
    dropped = []
    for pick in spec["picks"]:
        e = render_entry(pick, meta)
        if e is None:
            dropped.append(pick["full"])
        else:
            rendered[pick["tier"]].append(e)
    sections = []
    for t in TIER_ORDER:
        if rendered[t]:
            sections.append("\n".join([TIER_HEADERS[t], "", "\n\n".join(rendered[t])]))
    body.append("\n\n---\n\n".join(sections))
    if spec.get("footer"):
        body += ["", "---", "", spec["footer"]]
    return "\n".join(body).rstrip("\n") + "\n", dropped


def main(specs):
    all_fulls = [p["full"] for s in specs for p in s["picks"]]
    print(f"Fetching live meta for {len(set(all_fulls))} repos...", file=sys.stderr)
    meta = fetch_meta(all_fulls)
    total_live, total_dropped, empty_jobs = 0, [], []
    for spec in specs:
        text, dropped = render_job(spec, meta)
        live = len([p for p in spec["picks"] if meta.get(p["full"]) not in (None, "ERR")])
        total_live += live
        total_dropped += [(spec["file"], d) for d in dropped]
        if live == 0:
            empty_jobs.append(spec["file"])
            print(f"!! EMPTY (all dead): {spec['file']} — NOT writing", file=sys.stderr)
            continue
        with open(os.path.join(JOBS_DIR, spec["file"]), "w") as f:
            f.write(text)
        print(f"  wrote {spec['file']:42s} {live} entries", file=sys.stderr)
    print(f"\n=== {len(specs)-len(empty_jobs)} files written, {total_live} live entries ===", file=sys.stderr)
    for f, d in total_dropped:
        print(f"  DROPPED {f}: {d}", file=sys.stderr)
    if empty_jobs:
        print(f"EMPTY JOBS: {empty_jobs}", file=sys.stderr)
    return {"written": len(specs) - len(empty_jobs), "entries": total_live,
            "dropped": total_dropped, "empty": empty_jobs}


if __name__ == "__main__":
    raise SystemExit("import this module and call main(specs)")
