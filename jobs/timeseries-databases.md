# Job: Time-Series Databases

**You're about to:** store + query metrics/IoT/event time-series efficiently — downsampling, retention, compression.

> Reputation pulled live **2026-06-19** via `gh api`.

---

## Tier A 🟢 — Canonical

### TimescaleDB
Postgres extension for time-series — hypertables, continuous aggregates. Pick when you want SQL + Postgres ecosystem.
- **source:** https://github.com/timescale/timescaledb
- **reputation:** **22,928★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** PostgreSQL
- **adapt:** fork your hypertable + retention/compression policy.

---

## Tier B 🔵 — Community-proven

### QuestDB
High-ingest time-series DB with SQL + fast time-bucketing. Pick for very high write throughput.
- **source:** https://github.com/questdb/questdb
- **reputation:** **17,103★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a server
- **adapt:** fork your schema + ingestion (ILP) setup.

### InfluxDB
Popular purpose-built time-series DB — tagging model, retention. Mind major-version API differences.
- **source:** https://github.com/influxdata/influxdb
- **reputation:** **31,561★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a server
- **adapt:** pick your version deliberately; fork schema.
