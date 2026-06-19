# Job: OpenTelemetry — Traces, Metrics, Logs

**You're about to:** instrument apps with vendor-neutral telemetry — traces, spans, context propagation, the collector.

> Reputation pulled live **2026-06-19** via `gh api`.

Backends live in [observability-monitoring](observability-monitoring.md) and [log-aggregation](log-aggregation.md).

---

## Tier A 🟢 — Canonical

### OpenTelemetry Collector
The vendor-neutral telemetry pipeline — receive, process, export traces/metrics/logs. CNCF standard.
- **source:** https://github.com/open-telemetry/opentelemetry-collector
- **reputation:** **7,145★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** apps emitting OTLP
- **adapt:** fork your collector config (receivers/processors/exporters).

### OTel Specification
The spec behind the SDKs — semantic conventions, context propagation. Cite it when SDKs disagree.
- **source:** https://github.com/open-telemetry/opentelemetry-specification
- **reputation:** **4,263★** · pushed 2026-06-17
- **last_validated:** 2026-06-19
- **assumes:** none
- **adapt:** reference.
