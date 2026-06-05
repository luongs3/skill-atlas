# Job: Columnar Data (Apache Arrow)

**You're about to:** move data between tools fast with a shared columnar format.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Apache Arrow
The cross-language columnar memory format that lets Polars/DuckDB/Spark/pandas share data zero-copy.
- **source:** https://github.com/apache/arrow (docs: https://arrow.apache.org/docs)
- **reputation:** Official ASF · **16,810★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** a data toolchain
- **adapt:** none — it's the interchange layer under your other tools.

---

*Foundational plumbing under [dataframes-polars-duckdb](dataframes-polars-duckdb.md) and [data-engineering](data-engineering.md). You rarely use it directly, but knowing it explains why those tools interop. Private skill = where Arrow sits in your pipeline.*
