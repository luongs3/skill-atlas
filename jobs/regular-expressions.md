# Job: Regular Expressions

**You're about to:** write, debug, or understand a regex — matching, capture groups, lookarounds.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier B 🔵 — Community-proven

### learn-regex
A clear, example-driven guide to regex from the ground up, translated into many languages.
- **source:** https://github.com/ziishaned/learn-regex
- **reputation:** **46,117★** · pushed 2025-08-25 (high stars; >6mo since push but regex syntax is stable)
- **last_validated:** 2026-06-05
- **assumes:** nothing
- **adapt:** none — learning reference.

---

## Tier A 🟢 — The right tool for this job

For regex specifically, the highest-trust workflow is **an interactive tester plus the agent**:
build the pattern against real sample strings and watch every match, rather than trusting a
pattern by reading it.
- **regex101.com** — live tester with explanation of every token, for PCRE/JS/Python/Go flavors.
- **The agent** — describe what you want to match in plain English, get the pattern, then
  *verify it on regex101 against your real inputs*. LLMs write regex well but flavor differences
  (Go's RE2 lacks lookarounds, etc.) bite — verify, don't trust.
- **last_validated:** 2026-06-05
- **adapt:** build a private skill of the patterns you reuse (email, semver, log lines) with
  test strings attached, so you never re-derive them.

---

*Regex is the canonical "looks right, is subtly wrong" failure. The private skill worth building
is a tested pattern library — each pattern paired with the inputs it must match and must reject.
See [linux-shell](linux-shell.md) for grep/ripgrep usage.*
