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

*See [message-queues-streaming](message-queues-streaming.md) and [data-engineering](data-engineering.md). Private skill = your stream topology + delivery-guarantee choices.*
