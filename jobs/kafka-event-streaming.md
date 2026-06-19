# Job: Apache Kafka — Event Streaming

**You're about to:** run Kafka as the backbone for event-driven systems — topics, partitions, consumer groups, exactly-once.

> Reputation pulled live **2026-06-19** via `gh api`.

Broader queue landscape in [message-queues-streaming](message-queues-streaming.md); processing in [stream-processing](stream-processing.md).

---

## Tier A 🟢 — Canonical

### Apache Kafka
The distributed log standard — partitions, replication, consumer groups, KRaft. Docs define delivery + ordering semantics.
- **source:** https://github.com/apache/kafka
- **reputation:** **32,885★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a Kafka cluster
- **adapt:** fork your topic design + partition/retention policy.

---

## Tier B 🔵 — Community-proven

### Kafka UI
Web UI to inspect topics, consumer lag, and messages — the operability layer Kafka lacks out of the box.
- **source:** https://github.com/provectus/kafka-ui
- **reputation:** **12,165★** · pushed 2024-07-26
- **last_validated:** 2026-06-19
- **assumes:** a Kafka cluster
- **adapt:** deploy read-only first; gate writes.
