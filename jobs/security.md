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

*Scope note: these are listed for defensive hardening, secure coding, and authorized
testing. Don't use them against systems you don't own or aren't explicitly cleared to test.*
