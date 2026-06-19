# Job: RabbitMQ & NATS — Messaging

**You're about to:** pick and run a message broker for queues, pub/sub, and request/reply — beyond Kafka's log model.

> Reputation pulled live **2026-06-19** via `gh api`.

Log-style streaming in [kafka-event-streaming](kafka-event-streaming.md).

---

## Tier A 🟢 — Canonical

### RabbitMQ
The mature AMQP broker — exchanges, queues, routing, acks. Reach for it for classic work-queue + routing patterns.
- **source:** https://github.com/rabbitmq/rabbitmq-server
- **reputation:** **13,718★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a broker
- **adapt:** fork your exchange/queue topology + DLQ policy.

### NATS
Lightweight, blazing pub/sub + JetStream persistence — simple ops, great for microservice messaging + edge.
- **source:** https://github.com/nats-io/nats-server
- **reputation:** **20,044★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a NATS server
- **adapt:** fork your subject hierarchy + JetStream config.
