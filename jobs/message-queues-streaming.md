# Job: Message Queues & Streaming

**You're about to:** add async messaging, a task queue, event streaming, or durable
workflows. Canonical broker sources + high-rep Go tooling. (For Kafka/Redis specifically,
see also [scalability-distributed-systems](scalability-distributed-systems.md).)

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical (brokers / engines)

### RabbitMQ
The classic, battle-tested message broker (AMQP) — official source + docs.
- **source:** https://github.com/rabbitmq/rabbitmq-server (docs: https://www.rabbitmq.com/docs)
- **reputation:** Official (Broadcom/VMware) · **13,685★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a broker instance
- **adapt:** fork your exchange/queue/routing conventions.

### Temporal — durable execution / workflows
For long-running, reliable workflows (sagas, retries, human-in-the-loop) — official source.
- **source:** https://github.com/temporalio/temporal (docs: https://docs.temporal.io)
- **reputation:** Official Temporal · **20,717★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a Temporal cluster + SDK
- **adapt:** fork your workflow/activity patterns.

### NATS (Go client)
Lightweight, high-performance messaging + JetStream for streaming. (Server in
[scalability](scalability-distributed-systems.md).)
- **source:** https://github.com/nats-io/nats.go (docs: https://docs.nats.io)
- **reputation:** Official NATS (CNCF) · **6,630★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **assumes:** Go + a NATS server
- **adapt:** none — reference.

---

## Tier B 🔵 — Community-proven (Go task queue)

### Asynq — Redis-backed task queue for Go
The standard Go background-job/task-queue library (Sidekiq-like), backed by Redis.
- **source:** https://github.com/hibiken/asynq
- **reputation:** **13,335★** · pushed 2026-05-26 (high stars + maintained)
- **last_validated:** 2026-06-03
- **assumes:** Go + Redis
- **adapt:** fork your queue/priority/retry conventions.

---

*Picking the right tool is the whole game here: a task queue (Asynq) ≠ a broker (RabbitMQ)
≠ a stream (Kafka/NATS JetStream) ≠ a workflow engine (Temporal). The atlas names the
live, maintained option in each category; encode *which one your services use* in a
private skill so the choice isn't re-litigated per feature.*
