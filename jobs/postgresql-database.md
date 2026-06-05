# Job: PostgreSQL — the Database, Deep

**You're about to:** run Postgres seriously — indexing, `EXPLAIN`, replication,
partitioning, backup. The engine internals, not the app glue.

> Reputation pulled live **2026-06-04** via `gh api`.

This is Postgres-the-database. For Postgres **+ Go tooling / migrations / app wiring**,
see [databases-sql](databases-sql.md).

---

## Tier A 🟢 — Canonical

### PostgreSQL source + official docs
The reference engine and the docs every tuning decision traces back to — query planner,
index types (B-tree/GIN/GiST/BRIN), `EXPLAIN (ANALYZE, BUFFERS)`, streaming + logical
replication, declarative partitioning, VACUUM.
- **source:** https://github.com/postgres/postgres (docs: https://www.postgresql.org/docs/)
- **reputation:** The PostgreSQL project · **21,073★** · pushed 2026-06-03
- **last_validated:** 2026-06-04
- **assumes:** a running Postgres instance
- **adapt:** none — reference. Read the docs for your exact major version.

---

## Tier B 🔵 — Community-proven

### pgBackRest — backup & restore
The standard for reliable full/incremental/differential backups, PITR, and restore at scale.
Use it before you ever need it.
- **source:** https://github.com/pgbackrest/pgbackrest (docs: https://pgbackrest.org/)
- **reputation:** Crunchy Data–backed · **4,105★** · pushed 2026-06-01
- **last_validated:** 2026-06-04
- **assumes:** filesystem/object-store access to the DB host
- **adapt:** fork your repo retention + WAL-archive config; rehearse restores on a schedule.

---

*Substitution-resistant private skill: your cluster's tuning baseline — `shared_buffers`,
`work_mem`, autovacuum thresholds, partition keys, and the slow-query patterns specific to
your schema. An LLM knows `EXPLAIN`; it doesn't know which of your indexes are dead weight.*
