# Job: Fast DataFrames (Polars/DuckDB)

**You're about to:** crunch larger-than-memory data fast with Polars or DuckDB.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Polars
Blazing-fast DataFrame library in Rust with a Python API; the pandas successor for big data.
- **source:** https://github.com/pola-rs/polars (docs: https://docs.pola.rs)
- **reputation:** **38,678★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** Python/Rust
- **adapt:** fork your lazy-query conventions.

### DuckDB
In-process OLAP SQL engine — query Parquet/CSV/Arrow at speed, no server.
- **source:** https://github.com/duckdb/duckdb (docs: https://duckdb.org/docs)
- **reputation:** **38,612★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** nothing
- **adapt:** none — reference.

---

## How to use this job

Use **Polars** when your work is row/column transformation in a Python pipeline — joins, group-bys, feature engineering — and you want a fluent DataFrame API. Use **DuckDB** when the work is naturally SQL, when you're querying Parquet/CSV files in place, or when you need to join across files larger than memory. They interoperate via Arrow with zero copy, so the real decision is whether you think in DataFrame method chains or in SQL; many pipelines use DuckDB to read/aggregate and hand off to Polars for the rest.

## Pitfalls

- **Polars lazy vs eager is easy to confuse** — `pl.read_*` is eager, `pl.scan_*` is lazy. A lazy `LazyFrame` does nothing until `.collect()`, and forgetting it means you pass around an unexecuted plan; conversely calling `.collect()` too early throws away predicate/projection pushdown and loads everything.
- **DuckDB's memory limit defaults can OOM on huge joins/sorts** — set `PRAGMA memory_limit` and `PRAGMA temp_directory` so it can spill to disk; without a temp dir, a large hash join that exceeds RAM aborts instead of spilling.
- **Polars is null-aware in ways pandas users don't expect** — `NaN` (float) and `null` (missing) are distinct, and many aggregations skip nulls differently than pandas. Check `.null_count()` and be explicit with `drop_nulls`/`fill_null`.

---

*See [data-analysis](data-analysis.md). Reach for these when pandas hits a memory/perf wall. Private skill = your standard read/transform pipeline.*
