# Job: Application Security

**You're about to:** secure an app, prep for a security review, or study attack/defense
patterns. Strong Tier-A authority (OWASP) + high-rep practitioner references.

> Reputation pulled live **2026-06-02** via `gh api`. Use these for **defensive** work and
> authorized testing only.

---

## Tier A 🟢 — Canonical

### OWASP Cheat Sheet Series
The authoritative, concise defensive guidance for nearly every appsec topic (authn,
injection, crypto, headers). The first place to check "how do I do X securely."
- **source:** https://github.com/OWASP/CheatSheetSeries (read: https://cheatsheetseries.owasp.org)
- **reputation:** Official OWASP · **32,153★** · pushed 2026-05-31 (maintained)
- **last_validated:** 2026-06-02
- **assumes:** nothing
- **adapt:** fork the cheat sheets matching your stack (e.g. Go, REST, JWT) into a private review checklist.

---

## Tier B 🔵 — Community-proven (practitioner references)

### PayloadsAllTheThings
The standard reference of attack payloads + methodology — for **authorized** pentesting
and understanding what defenses must withstand.
- **source:** https://github.com/swisskyrepo/PayloadsAllTheThings
- **reputation:** **78,136★** · pushed 2026-04-22 (high stars + maintained)
- **last_validated:** 2026-06-02
- **assumes:** authorized testing context (your own systems, a CTF, a sanctioned engagement)
- **adapt:** none — reference. Use defensively: test your own endpoints against these patterns.

### Awesome Hacking
Curated index of security learning resources, tools, and CTF material.
- **source:** https://github.com/Hack-with-Github/Awesome-Hacking
- **reputation:** **113,610★** · pushed 2026-05-07
- **last_validated:** 2026-06-02
- **assumes:** nothing — it's an index
- **adapt:** none.

---

## Tier C 🟡 — Useful, verify

### Kritt-ai/open-kritt
Orchestrate AI agents to find real vulnerabilities in code.
- **source:** https://github.com/Kritt-ai/open-kritt
- **reputation:** 1,091★ · 201 forks · pushed 2026-08-03 · created 2026-07-20 · not archived · AGPL-3.0 (added 2026-08-03; young repo w/ 3 watchers vs 1,091★ — tier C until reviewed)
- **last_validated:** 2026-08-03
- **assumes:** JavaScript/Node toolchain; you supply LLM API keys and a codebase to scan
- **adapt:** agentic SAST — read the orchestration prompts before trusting findings; LLM vuln-hunters produce false positives, so treat output as leads not verdicts.

---

*Scope note: these are listed for defensive hardening, secure coding, and authorized
testing. Don't use them against systems you don't own or aren't explicitly cleared to test.*

### vercel-labs/deepsec
Deepsec is a security harness for finding vulnerabilities in your codebase powered by coding agents
- **source:** https://github.com/vercel-labs/deepsec
- **reputation:** 6,636★ · pushed 2026-08-09 (auto-added 2026-08-11 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-11
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### cloudflare/security-audit-skill
A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings
- **source:** https://github.com/cloudflare/security-audit-skill
- **reputation:** 3,150★ · pushed 2026-07-06 (auto-added 2026-08-29 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-29
- **assumes:** JavaScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.
