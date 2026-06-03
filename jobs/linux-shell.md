# Job: Linux & Shell

**You're about to:** work in the terminal — bash scripting, command-line fluency, or shell
debugging. Strong canonical tools + useful (but aging) learning references.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical (tools)

### tldr-pages — practical command examples
Community-maintained simplified man pages: real usage examples instead of exhaustive flags.
The single most useful CLI companion.
- **source:** https://github.com/tldr-pages/tldr (client: `tldr <command>`)
- **reputation:** **62,758★** · pushed 2026-06-03 (high stars + updated daily)
- **last_validated:** 2026-06-03
- **assumes:** the `tldr` client installed
- **adapt:** none — reference.

### ShellCheck — shell script linter
Catches the bugs every bash script has (quoting, word-splitting, `[[ ]]` gotchas). Run it
on every script you write.
- **source:** https://github.com/koalaman/shellcheck (use: `shellcheck script.sh`)
- **reputation:** **39,517★** · pushed 2026-05-16
- **last_validated:** 2026-06-03
- **assumes:** shellcheck installed
- **adapt:** none — run it in CI.

---

## Tier C 🟡 — Useful but aging (concepts hold, verify specifics)

### The Art of Command Line
A famously good single-page guide to command-line fluency.
- **source:** https://github.com/jlevy/the-art-of-command-line
- **reputation:** **161,171★** BUT pushed **2024-06-25** (>12mo → C; core advice timeless, some tools dated)
- **last_validated:** 2026-06-03
- **assumes:** nothing
- **adapt:** read once for fluency; verify any specific tool recommendation against current options.

### bash-handbook
A readable bash scripting primer.
- **source:** https://github.com/denysdovhan/bash-handbook
- **reputation:** **6,059★** BUT pushed **2024-02-05** (>12mo → C)
- **last_validated:** 2026-06-03
- **assumes:** nothing
- **adapt:** learn the basics here, lint the result with ShellCheck (the gotchas it won't teach you).

---

*The highest-value private skill here: a personal `bash-safety` skill encoding the patterns
you keep getting wrong (`set -euo pipefail`, quoting `"$var"`, `[[ ]]` over `[ ]`) — the
exact things ShellCheck flags, turned into defaults you write from the start.*
