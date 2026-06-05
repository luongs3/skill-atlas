# Job: Analytics Engineering (dbt)

**You're about to:** transform warehouse data with dbt — models, tests, documentation as code.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### dbt Core
SQL-based transformation framework — the 'T' in ELT, with tests + docs + lineage.
- **source:** https://github.com/dbt-labs/dbt-core (docs: https://docs.getdbt.com)
- **reputation:** Official dbt Labs · **12,937★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** a data warehouse
- **adapt:** fork your model/naming/test conventions.

---

## How to use this job

Reach for **dbt Core** once SQL transformations sprawl past a handful of ad-hoc queries and you need version control, testing, and lineage — it shines as the "T" in ELT, transforming data already loaded in the warehouse, not extracting or loading it. Use incremental models for large fact tables (don't full-refresh billions of rows every run) and lean on `ref()`/`source()` so dbt builds the DAG and runs models in dependency order. The decision to adopt hinges on team size and SQL volume; a solo analyst with three queries doesn't need it.

## Pitfalls

- **`dev` and `prod` targets can clobber each other.** If two environments or two developers point at the same schema, runs overwrite each other's tables. Use schema/dataset prefixing per target and per-developer dev schemas.
- **Incremental models drift silently.** A late-arriving or updated row that falls outside your `is_incremental()` filter never gets corrected, so incremental results quietly diverge from a full refresh. Periodically full-refresh, and pick a unique key + appropriate strategy (`merge`/`delete+insert`).
- **Tests catch shape, not correctness.** `not_null`/`unique`/`accepted_values` validate structure, but a model can pass every test and still compute the wrong number. Add bespoke data tests for business logic, and watch for cascading rebuild costs as the DAG grows.

*See [data-engineering](data-engineering.md) and [databases-sql](databases-sql.md). Private skill = your dbt project structure + testing standards.*
