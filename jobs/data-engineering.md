# Job: Data Engineering

**You're about to:** build data pipelines, orchestrate ETL/ELT, or work with big-data /
analytics engines. All canonical official sources, high reputation.

> Reputation pulled live **2026-06-03** via `gh api`. See also
> [data-analysis](data-analysis.md) for the exploration/notebook side.

---

## Tier A 🟢 — Canonical (official engine/tool sources)

### Apache Airflow — orchestration
The de-facto workflow orchestrator for data pipelines (DAGs, scheduling, backfills).
- **source:** https://github.com/apache/airflow (docs: https://airflow.apache.org/docs/)
- **reputation:** Official ASF · **45,677★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** an Airflow deployment
- **adapt:** fork your DAG conventions (naming, retries, alerting).

### Apache Spark — distributed processing
The standard engine for large-scale batch + streaming data processing.
- **source:** https://github.com/apache/spark (docs: https://spark.apache.org/docs/latest/)
- **reputation:** Official ASF · **43,386★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a Spark cluster
- **adapt:** none — reference.

### dbt — transformation (ELT)
The standard for SQL-based transformations in the warehouse (the "T" in ELT).
- **source:** https://github.com/dbt-labs/dbt-core (docs: https://docs.getdbt.com)
- **reputation:** Official dbt Labs · **12,911★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a data warehouse
- **adapt:** fork your model/test/naming conventions.

### ClickHouse — OLAP database
Fast columnar analytics DB — official source + docs. (DuckDB for local/embedded; see
[data-analysis](data-analysis.md).)
- **source:** https://github.com/ClickHouse/ClickHouse (docs: https://clickhouse.com/docs)
- **reputation:** Official ClickHouse · **47,770★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a ClickHouse instance
- **adapt:** none — reference.

### Apache Flink — stream processing
For true low-latency stream processing (vs Spark's micro-batch).
- **source:** https://github.com/apache/flink (docs: https://flink.apache.org/docs/)
- **reputation:** Official ASF · **26,039★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a Flink cluster
- **adapt:** none — reference.

---

*Tool choice is the skill here: orchestrator (Airflow) ≠ processing engine (Spark/Flink) ≠
transformation (dbt) ≠ OLAP store (ClickHouse). Encode your stack's actual pipeline shape
in a private skill so each new pipeline follows the same pattern.*
