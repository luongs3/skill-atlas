# Job: SQLite & Embedded Databases

**You're about to:** use SQLite well — the most-deployed database — plus modern embedded/edge variants.

> Reputation pulled live **2026-06-19** via `gh api`.

Server SQL in [sql-databases-mysql](sql-databases-mysql.md)/[postgresql-database](postgresql-database.md).

---

## Tier A 🟢 — Canonical

### SQLite
The most widely deployed database — serverless, single-file, rock-solid. Docs define the SQL dialect + quirks.
- **source:** https://github.com/sqlite/sqlite
- **reputation:** **9,803★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** nothing — it's embedded
- **adapt:** reference; learn the type affinity + WAL gotchas.

### DuckDB
In-process analytical SQL ("SQLite for analytics") — blazing on Parquet/CSV. The local-analytics default.
- **source:** https://github.com/duckdb/duckdb
- **reputation:** **38,867★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** nothing — embedded
- **adapt:** fork your queries; great for ETL + notebooks.

---

## Tier B 🔵 — Community-proven

### libSQL (Turso)
An open SQLite fork for the edge — replication, remote access. Pick for distributed SQLite needs.
- **source:** https://github.com/tursodatabase/libsql
- **reputation:** **16,847★** · pushed 2026-06-02
- **last_validated:** 2026-06-19
- **assumes:** libSQL/Turso
- **adapt:** fork your replication + embedded-replica setup.
