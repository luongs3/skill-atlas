# Job: IoT Messaging — MQTT

**You're about to:** connect devices with lightweight pub/sub — brokers, QoS, retained messages, last-will.

> Reputation pulled live **2026-06-19** via `gh api`.

---

## Tier A 🟢 — Canonical

### Eclipse Mosquitto
The reference lightweight MQTT broker — small footprint, ubiquitous in IoT. Docs define broker behavior.
- **source:** https://github.com/eclipse-mosquitto/mosquitto
- **reputation:** **10,993★** · pushed 2026-06-15
- **last_validated:** 2026-06-19
- **assumes:** a host
- **adapt:** fork your topic ACLs + TLS + persistence.

---

## Tier B 🔵 — Community-proven

### EMQX
Scalable, clustered MQTT broker for millions of connections — pick when Mosquitto won't scale.
- **source:** https://github.com/emqx/emqx
- **reputation:** **16,420★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a server/cluster
- **adapt:** fork your auth + clustering + rules.
