# Job: Stream Processing

**You're about to:** process event streams in real time — Kafka, Flink, exactly-once pipelines.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Apache Kafka
The de-facto event-streaming platform — durable logs, partitions, consumer groups.
- **source:** https://github.com/apache/kafka (docs: https://kafka.apache.org/documentation)
- **reputation:** Official ASF · **32,713★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a Kafka cluster
- **adapt:** fork your topic + consumer-group conventions.

### Apache Flink
True low-latency stream processing (stateful, exactly-once) vs Spark's micro-batch.
- **source:** https://github.com/apache/flink (docs: https://flink.apache.org/docs)
- **reputation:** Official ASF · **26,042★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a Flink cluster
- **adapt:** fork your job + checkpointing conventions.

---

## How to use this job

**Kafka** is the durable, partitioned log — the transport and storage layer you almost always have. **Flink** is the compute layer for stateful, low-latency processing (windowing, joins, exactly-once) over those streams. The decision isn't Kafka *or* Flink; it's whether your transformation is simple enough for Kafka Streams / ksqlDB versus needing Flink's true event-time, large-state, exactly-once machinery.

## Pitfalls

- **Consumer lag and rebalance storms:** slow consumers fall behind the log's retention window and lose data; frequent group membership changes (deploys, crashes, long GC) trigger rebalances that pause all consumers in the group. Tune `max.poll.interval.ms` and session timeouts deliberately.
- **Exactly-once is expensive:** end-to-end exactly-once (Kafka transactions + Flink checkpoints) adds latency and operational complexity. Many pipelines are better served by idempotent consumers + at-least-once; don't pay for EOS you don't need.
- **State and checkpoint sizing:** Flink keyed state grows with cardinality; under-provisioned state backends (RocksDB) and slow checkpoints cause backpressure and failed recovery. Watch checkpoint duration and partition skew (hot keys).

---

*See [message-queues-streaming](message-queues-streaming.md) and [data-engineering](data-engineering.md). Private skill = your stream topology + delivery-guarantee choices.*
