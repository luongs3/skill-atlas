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

*Substitution-resistant private layer: your **install policy** — the risk-score threshold you block at, the categories you treat as hard-fail vs advisory, and the allowlist of skills you've already reviewed. The scanner produces a number; the policy that turns that number into install/block is yours. Note SkillSpector + mcp-scan are days-old (2026-06) and fast-moving — a scan is a strong signal, not a safety guarantee; a clean scan ≠ trusted, and a flagged skill deserves a human read, not auto-rejection.*
