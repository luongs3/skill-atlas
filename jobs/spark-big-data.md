# Job: Big Data Processing (Spark)

**You're about to:** process large datasets with Spark — batch, SQL, distributed dataframes.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Apache Spark
The standard engine for large-scale batch + SQL data processing.
- **source:** https://github.com/apache/spark (docs: https://spark.apache.org/docs/latest)
- **reputation:** Official ASF · **43,396★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** a Spark cluster
- **adapt:** fork your job-tuning + partition conventions.

---

## How to use this job

Reach for **Spark** when your data genuinely exceeds single-node memory and you need distributed batch or SQL across a cluster. For datasets that fit on one beefy machine (tens of GB, even into low hundreds), a single-node engine like DuckDB or Polars (see [dataframes-polars-duckdb](dataframes-polars-duckdb.md)) is dramatically simpler and often faster — the decision hinges on data scale and whether you already run a cluster, not on the word "big". Prefer the DataFrame/SQL API over RDDs so the Catalyst optimizer can do its job.

## Pitfalls

- **The small-files problem.** Writing thousands of tiny output files (one per partition per task) cripples downstream reads and hammers the metastore/namenode. Coalesce or `repartition` before writing, and compact regularly.
- **Skewed partitions stall the whole job.** One hot key (nulls, a default value, a mega-customer) sends most rows to a single task while the rest finish — the stage hangs on one straggler. Salt the key or enable Adaptive Query Execution's skew join handling.
- **Lazy evaluation hides the real cost.** Transformations don't run until an action; a stray `count()`/`collect()` or repeated unpersisted reuse silently recomputes the whole lineage. Cache deliberately and read the DAG in the Spark UI before blaming the cluster.

*See [data-engineering](data-engineering.md). Private skill = your cluster-tuning defaults + the dataframe patterns your team standardizes.*
