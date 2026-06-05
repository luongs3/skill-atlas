# Job: Code Quality & Linting

**You're about to:** enforce style and catch bugs automatically — linters, formatters, hooks.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### ESLint + Prettier
The JS/TS standard: ESLint (bug + style rules) and Prettier (formatting).
- **source:** https://github.com/eslint/eslint (27,265★) · https://github.com/prettier/prettier (51,902★)
- **reputation:** official, very high stars, pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** JS/TS project
- **adapt:** fork your rule config.

### golangci-lint
The aggregated Go linter — runs many linters fast in CI.
- **source:** https://github.com/golangci/golangci-lint (docs: https://golangci-lint.run)
- **reputation:** **19,038★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** Go project
- **adapt:** fork your enabled-linter set.

---

## Tier B 🔵 — Community-proven

### pre-commit
Git hook framework to run linters/formatters before every commit.
- **source:** https://github.com/pre-commit/pre-commit (docs: https://pre-commit.com)
- **reputation:** **15,309★** · pushed 2026-05-29
- **last_validated:** 2026-06-05
- **assumes:** a git repo
- **adapt:** fork your .pre-commit-config.yaml.

---

*See [github-pr-workflow] and language jobs. Private skill = your exact lint config + the rules your team actually enforces.*
