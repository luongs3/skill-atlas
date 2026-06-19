# Job: Lakehouse Tables — Delta & Iceberg

**You're about to:** get ACID transactions, time travel, and schema evolution on object-storage tables.

> Reputation pulled live **2026-06-19** via `gh api`.

Query engines in [dataframes-polars-duckdb](dataframes-polars-duckdb.md) and [spark-pyspark](spark-pyspark.md).

---

## Tier A 🟢 — Canonical

### Delta Lake
ACID table format over Parquet — time travel, MERGE, schema enforcement. The Databricks-origin standard.
- **source:** https://github.com/delta-io/delta
- **reputation:** **8,859★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** Spark or a Delta engine
- **adapt:** fork your table layout + OPTIMIZE/VACUUM policy.

### Apache Iceberg
Open table format with hidden partitioning, snapshot isolation, and broad engine support (Spark/Trino/Flink). Vendor-neutral.
- **source:** https://github.com/apache/iceberg
- **reputation:** **8,975★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a compatible engine + catalog
- **adapt:** fork your partition spec + catalog choice.
