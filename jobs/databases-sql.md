# Job: Databases & SQL (PostgreSQL-first)

**You're about to:** design schemas, write/optimize SQL, run migrations, or wire a Go app
to Postgres. Strong canonical sources + high-rep Go tooling.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical

### PostgreSQL official source + docs
The reference implementation and the best SQL documentation in existence (the docs are a
genuine teaching resource, not just an API dump).
- **source:** https://github.com/postgres/postgres (docs: https://www.postgresql.org/docs/)
- **reputation:** The Postgres project · **21,073★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a Postgres instance
- **adapt:** build a private "pg gotchas" skill — the locking/index/EXPLAIN patterns you re-look-up.

---

## Tier B 🔵 — Community-proven (Go + Postgres tooling)

### sqlc — compile SQL to type-safe Go
Write SQL, generate type-safe Go. The modern alternative to ORMs for a Go/Postgres stack.
- **source:** https://github.com/sqlc-dev/sqlc
- **reputation:** **17,827★** · pushed 2026-05-29 (high stars + maintained)
- **last_validated:** 2026-06-03
- **assumes:** Go + a SQL schema
- **adapt:** fork the config patterns that match your schema conventions.

### golang-migrate — schema migrations
The standard migration tool for Go services.
- **source:** https://github.com/golang-migrate/migrate
- **reputation:** **18,561★** · pushed 2026-03-19 (high stars; push ~3mo — fine)
- **last_validated:** 2026-06-03
- **assumes:** Go, a SQL DB
- **adapt:** none — reference for migration file format + CLI.

### goose — migrations (alternative)
A lighter migration tool, supports Go-based migrations as well as SQL.
- **source:** https://github.com/pressly/goose
- **reputation:** **10,812★** · pushed 2026-05-16
- **last_validated:** 2026-06-03
- **assumes:** Go
- **adapt:** pick goose OR migrate; don't run both.

---

*The private fork that pays off here: a `sql-review` skill encoding your team's schema
conventions (naming, indexing rules, when a migration needs `CONCURRENTLY`). Generic SQL
help an LLM gives free; your team's rules it doesn't know.*

---

## Tier C 🟡 — Useful, verify

### safishamsi/graphify
AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, she
- **source:** https://github.com/safishamsi/graphify
- **reputation:** 68,261★ · pushed 2026-06-16 (auto-added 2026-06-17 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-17
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### Graphify-Labs/graphify
AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, she
- **source:** https://github.com/Graphify-Labs/graphify
- **reputation:** 77,138★ · pushed 2026-07-03 (auto-added 2026-07-04 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-07-04
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.
