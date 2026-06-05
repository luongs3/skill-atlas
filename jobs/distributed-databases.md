# Job: Distributed Databases

**You're about to:** pick and run a database that scales horizontally — distributed SQL,
wide-column, graph, or time-series — and accept the consistency/partition tradeoffs.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### CockroachDB — distributed SQL
Horizontally scalable, strongly consistent SQL with a Postgres-compatible wire protocol.
The default when you want SQL semantics across regions.
- **source:** https://github.com/cockroachdb/cockroach (docs: https://www.cockroachlabs.com/docs/)
- **reputation:** Cockroach Labs · **32,183★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** a multi-node cluster (or single-node for dev)
- **adapt:** fork your locality/zone config + survival goals.

### Apache Cassandra — wide-column
The AP-leaning, masterless wide-column store for huge write throughput. Model queries
first, tables second.
- **source:** https://github.com/apache/cassandra (docs: https://cassandra.apache.org/doc/)
- **reputation:** Apache Software Foundation · **9,752★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** you understand its tunable-consistency model
- **adapt:** fork your partition-key + replication-factor design.

---

## Tier B 🔵 — Community-proven

### Neo4j — graph
The standard graph database; Cypher for relationship-heavy queries.
- **source:** https://github.com/neo4j/neo4j (docs: https://neo4j.com/docs/)
- **reputation:** Neo4j Inc. · **16,644★** · pushed 2026-05-28
- **last_validated:** 2026-06-04
- **assumes:** a graph-shaped problem
- **adapt:** fork your graph model + index hints.

### TimescaleDB & InfluxDB — time-series
Timescale extends Postgres for time-series (hypertables); InfluxDB is purpose-built.
- **source:** https://github.com/timescale/timescaledb (**22,806★** · 2026-06-04) · https://github.com/influxdata/influxdb (**31,527★** · 2026-06-03)
- **reputation:** Timescale / InfluxData · both actively maintained
- **last_validated:** 2026-06-04
- **assumes:** time-stamped, append-heavy data
- **adapt:** fork your retention + rollup policy.

---

*Substitution-resistant private skill: the CAP tradeoff your workload can tolerate and the
partition/shard keys that follow. An LLM names these databases; it can't choose between
consistency and availability for your business.*
