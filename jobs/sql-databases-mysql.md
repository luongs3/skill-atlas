# Job: SQL Databases — MySQL & SQLite

**You're about to:** work with MySQL and SQLite — schema, indexing, query tuning, and the
operational differences between a server engine and an embedded one.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### MySQL official docs
The reference manual for the MySQL server — InnoDB storage, indexing, `EXPLAIN`,
replication, and transactions. **Note:** the GitHub `mysql/mysql-server` mirror is *not*
canonical; treat `dev.mysql.com/doc` as the source of truth.
- **source:** https://dev.mysql.com/doc/
- **reputation:** Oracle / MySQL · official vendor manual
- **last_validated:** 2026-06-04
- **assumes:** a running mysqld (match your 8.x point release)
- **adapt:** none — reference. Version-pin; defaults and SQL modes shift between releases.

### SQLite source + official docs
The reference embedded database — single-file, serverless, the most-deployed SQL engine.
Docs cover SQL dialect quirks, type affinity, WAL mode, and the C API.
- **source:** https://github.com/sqlite/sqlite (docs: https://sqlite.org/docs.html)
- **reputation:** D. Richard Hipp / SQLite · **9,743★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** the SQLite library/CLI available
- **adapt:** none — reference. Know its dynamic-typing + concurrency model before you rely on it.

---

## Tier B 🔵 — Community-proven

*None pinned — the official manuals above are sufficient. Add a community tuning guide here
only after you've verified it against your MySQL major version.*

---

*Substitution-resistant private skill: your schema, index strategy, and the engine choice
itself — when SQLite's single-writer model is fine vs when you need MySQL's concurrency. An
LLM writes SQL fine; it doesn't know your data volume or write-contention reality.*

---

## Tier C 🟡 — Useful, verify

### t8y2/dbx
20 MB lightweight cross-platform database client for 70+ databases, including MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, SQL Server,
- **source:** https://github.com/t8y2/dbx
- **reputation:** 13,518★ · pushed 2026-08-07 (auto-added 2026-08-07 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-07
- **assumes:** Rust toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.
