# Job: Vetting Agent Skills & LLM Security

**You're about to:** decide whether an agent skill / MCP server is SAFE to install, and red-team LLM apps — scan for prompt injection, data exfiltration, tool poisoning, and excessive agency before they run with your agent's trust.

> Reputation pulled live **2026-06-22** via `gh api`.

This is the SAFETY axis the trust tier (A/B/C/D = reputable + maintained) deliberately doesn't cover — a high-star skill can still ship a prompt-injection vector. Pair with [security](security.md) and [sast-dependency-scanning](sast-dependency-scanning.md) for the code-level view.

---

## Tier A 🟢 — Canonical

### NVIDIA SkillSpector
Purpose-built security scanner for agent skills — 64 vuln patterns across 16 categories (prompt injection, data exfil, privilege escalation, MCP tool poisoning), two-stage static+LLM analysis, 0-100 risk score, SARIF output. Run `--no-llm` for a free static pass; add an API key for the semantic stage. The reference scanner for "is this SKILL.md safe to install?"
- **source:** https://github.com/NVIDIA/SkillSpector
- **reputation:** Official NVIDIA · **9,099★** · pushed 2026-06-16
- **last_validated:** 2026-06-22
- **assumes:** Python 3.12+ (or the Docker image); optional LLM API key for the semantic stage
- **adapt:** wire `scan <skill> --no-llm --format sarif` into CI / a pre-install hook; set your own risk-score gate.

### garak
NVIDIA's LLM vulnerability scanner — probes a model/endpoint for jailbreaks, prompt injection, toxicity, data leakage. Skill-side safety (SkillSpector) vs model-side safety (garak) are complementary.
- **source:** https://github.com/NVIDIA/garak
- **reputation:** Official NVIDIA · **8,164★** · pushed 2026-06-17
- **last_validated:** 2026-06-22
- **assumes:** an LLM endpoint to probe
- **adapt:** fork your probe selection + pass/fail thresholds for your model.

### promptfoo
Test + red-team prompts, agents, and RAG — vulnerability scanning, eval assertions, CI integration. The broad LLM-app testing standard; treat prompts like code under test.
- **source:** https://github.com/promptfoo/promptfoo
- **reputation:** **22,443★** · pushed 2026-06-22
- **last_validated:** 2026-06-22
- **assumes:** an LLM app / prompts to test
- **adapt:** fork your eval suite + red-team config; gate CI on it.

---

## Tier B 🔵 — Community-proven

### mcp-scan (Invariant Labs)
Security scanner specifically for MCP servers + agent skills — detects tool poisoning, rug pulls, and cross-origin risks in the MCP layer. Pair with SkillSpector for MCP-heavy setups.
- **source:** https://github.com/invariantlabs-ai/mcp-scan
- **reputation:** **2,616★** · pushed 2026-06-19
- **last_validated:** 2026-06-22
- **assumes:** MCP server configs / an agent setup
- **adapt:** fork your scan targets; run before trusting a new MCP server.

---

## Dogfood receipt — we scanned *this atlas* with SkillSpector (2026-06-22)

Proof that **a scanner score is a signal, not a verdict** — the lesson this whole job exists to teach. We ran the Tier-A pick against the atlas's own repo:

```bash
skillspector scan ./skill-atlas --no-llm --format json   # static pass, no API key
# → score 100/100 · severity CRITICAL · recommendation DO_NOT_INSTALL
```

That verdict is **wrong for this repo**, and the failure modes are instructive:

- **~20 of 22 findings are false positives on a docs-only skill.** The static pass pattern-matches on text that *names* dangerous things: `kubeconfig`/`.npmrc` in a Kubernetes/npm job entry → "Credential Access (HIGH)"; `tool: *` in a frontmatter *example* → "Excessive Agency"; `self-evolve` in prose → "Rogue Agent"; `NOT LIMITED TO` in the MIT **LICENSE** → "Scope Creep"; and the README's own `rm -rf ~/.claude/skills/skill-atlas` **uninstall instructions** → two "Tool Misuse (HIGH)".
- **7 findings are binary mis-reads** — it parsed the bytes of `hero.png` as source and "found" `rm` and "context-window-stuffing".
- **Only 2 touch real executable code**, both benign: `scripts/bulk_add_jobs.py` calls `subprocess.run([...], shell=False)` with an explicit arg list over your own curated input, and `scripts/revalidate.sh` pipes the GitHub API through `python3`. No install hook, no MCP server, no load-time network call.

**Takeaways for using any skill-scanner:**
1. **Scope the scan to what actually ships** (`git archive HEAD`), not your working tree — gitignored scratch and binary assets inflate the count.
2. **The `--no-llm` static pass is a high-recall / low-precision triage list, not a verdict.** It has no semantic stage to tell "code that does `X`" from "docs that mention `X`". The LLM stage (needs an API key) filters most of this.
3. **SkillSpector exits 0 even on a CRITICAL score** (v2.2.3) — a CI gate must parse the JSON `risk_assessment`, not the exit code, and should stay **advisory** for doc-style skills. This atlas wires it that way in [`.github/workflows/skillspector.yml`](../.github/workflows/skillspector.yml).

The honest read: SkillSpector is genuinely useful for *executable* skills (hooks, MCP servers, scripts), where its categories map to real behavior. Against a trust-index of pure Markdown it's almost all noise — which is exactly why the **install policy below is the asset, not the number**.

---

## Tier C 🟡 — Useful, verify

### elder-plinius/T3MP3ST
autonomous red teaming platform; multi-agent offensive-security meta-harness
- **source:** https://github.com/elder-plinius/T3MP3ST
- **reputation:** 5,536★ · pushed 2026-08-02 (auto-added 2026-08-12 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-12
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

*Substitution-resistant private layer: your **install policy** — the risk-score threshold you block at, the categories you treat as hard-fail vs advisory, and the allowlist of skills you've already reviewed. The scanner produces a number; the policy that turns that number into install/block is yours. Note SkillSpector + mcp-scan are days-old (2026-06) and fast-moving — a scan is a strong signal, not a safety guarantee; a clean scan ≠ trusted, and a flagged skill deserves a human read, not auto-rejection.*
