# Job: Scalability & Distributed Systems

**You're about to:** design a system that scales — caching, queues, consistency, sharding,
event streaming. Directly relevant to senior backend design rounds and real architecture.

> Reputation pulled live **2026-06-03** via `gh api`. See also
> [algorithms-system-design](algorithms-system-design.md).

---

## Tier B 🔵 — Community-proven (high rep + maintained)

### awesome-scalability
Curated, deep index of how real systems scale — patterns + real-world architecture
post-mortems from big tech. The best single jumping-off point.
- **source:** https://github.com/binhnguyennus/awesome-scalability
- **reputation:** **71,419★** · pushed 2026-01-04 (high stars; ~5mo since push — fine, it's an index)
- **last_validated:** 2026-06-03
- **assumes:** nothing
- **adapt:** none — read the case studies relevant to your scale problem.

---

## Tier A 🟢 — Canonical (the infrastructure itself)

### Apache Kafka — event streaming
The de-facto event-streaming platform — official source + docs.
- **source:** https://github.com/apache/kafka (docs: https://kafka.apache.org/documentation/)
- **reputation:** Official ASF · **32,705★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a Kafka cluster (or Redpanda locally)
- **adapt:** build a private skill of your topic/partition/consumer-group conventions.

### Redis — caching & data structures
The standard in-memory cache/store — official source + docs.
- **source:** https://github.com/redis/redis (docs: https://redis.io/docs/)
- **reputation:** Official Redis · **74,664★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a Redis instance
- **adapt:** none — reference. Note caching patterns (cache-aside, TTL, stampede) in a private skill.

---

## Tier C 🟡 — Useful but aging

### System Design 101
Visual explanations of scalability concepts (load balancing, CDN, consistency).
- **source:** https://github.com/ByteByteGoHq/system-design-101
- **reputation:** **83,084★** BUT pushed **2025-04-04** (>12mo → C; visuals still useful, verify specifics)
- **last_validated:** 2026-06-03
- **assumes:** nothing
- **adapt:** none — use the diagrams as a mental-model primer.
