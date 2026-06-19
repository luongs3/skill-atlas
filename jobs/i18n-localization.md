# Job: Internationalization (i18n)

**You're about to:** localize apps — translation loading, pluralization, dates/numbers, RTL.

> Reputation pulled live **2026-06-19** via `gh api`.

---

## Tier A 🟢 — Canonical

### i18next
The most complete JS i18n framework — interpolation, plurals, namespaces, framework bindings. The default.
- **source:** https://github.com/i18next/i18next
- **reputation:** **8,584★** · pushed 2026-06-10
- **last_validated:** 2026-06-19
- **assumes:** a JS app
- **adapt:** fork your namespace structure + loading strategy.

---

## Tier D 🔴 — Caution

### format-message (ICU)
ICU MessageFormat tooling — listed as a reference point; verify maintenance before adopting.
- **source:** https://github.com/format-message/format-message
- **reputation:** **206★** · pushed 2026-02-15
- **last_validated:** 2026-06-19
- **assumes:** a JS app
- **adapt:** prefer i18next/FormatJS unless you specifically need this.
