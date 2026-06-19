# Job: Data Validation & Quality

**You're about to:** assert expectations on data, catch schema drift, and gate pipelines on quality.

> Reputation pulled live **2026-06-19** via `gh api`.

Runs inside [airflow-orchestration](airflow-orchestration.md)/[dbt-transformations](dbt-transformations.md).

---

## Tier A 🟢 — Canonical

### Great Expectations
Declarative data quality — expectations, validation, data docs. The category-defining tool.
- **source:** https://github.com/great-expectations/great_expectations
- **reputation:** **11,581★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** Python + data sources
- **adapt:** fork your expectation suites + checkpoints.

### Pydantic
Type-driven validation/parsing for Python — the runtime contract for ingestion + API boundaries.
- **source:** https://github.com/pydantic/pydantic
- **reputation:** **28,056★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Python 3.8+
- **adapt:** fork your models; reuse across pipeline + API.
