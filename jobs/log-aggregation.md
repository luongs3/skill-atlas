# Job: Log Aggregation & Tracing

**You're about to:** collect, search, and trace logs across services — Loki, Jaeger, OTel.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Grafana Loki
Log aggregation designed to pair with Prometheus/Grafana; label-based, cheap.
- **source:** https://github.com/grafana/loki (docs: https://grafana.com/docs/loki)
- **reputation:** Official Grafana · **28,310★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a Grafana stack
- **adapt:** fork your label + retention conventions.

### Jaeger + OpenTelemetry Collector
Distributed tracing (Jaeger) + the vendor-neutral telemetry pipeline (OTel Collector).
- **source:** https://github.com/jaegertracing/jaeger (22,858★) · https://github.com/open-telemetry/opentelemetry-collector (7,105★)
- **reputation:** official (CNCF), maintained
- **last_validated:** 2026-06-05
- **assumes:** instrumented services
- **adapt:** see [observability-monitoring](observability-monitoring.md).

---

*Extends [observability-monitoring](observability-monitoring.md). Private skill = your trace/log correlation + the runbooks that map symptoms to queries.*
