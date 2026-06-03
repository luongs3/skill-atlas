# Job: Observability & Monitoring

**You're about to:** instrument a service with metrics/traces/logs, set up dashboards, or
debug a production incident. Strong canonical tool sources.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical (official tool sources)

### Prometheus
The de-facto metrics + alerting system — official source + docs.
- **source:** https://github.com/prometheus/prometheus (docs: https://prometheus.io/docs/)
- **reputation:** Official CNCF · **64,252★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **assumes:** a service to scrape
- **adapt:** build a private "PromQL cheatsheet" skill of the queries you actually use.

### Grafana
The dashboard/visualization layer — official source + docs.
- **source:** https://github.com/grafana/grafana (docs: https://grafana.com/docs/)
- **reputation:** Official Grafana Labs · **74,136★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a data source (Prometheus, Loki, etc.)
- **adapt:** none — reference.

### OpenTelemetry Go
The vendor-neutral standard for traces/metrics/logs instrumentation in Go.
- **source:** https://github.com/open-telemetry/opentelemetry-go (docs: https://opentelemetry.io/docs/languages/go/)
- **reputation:** Official OTel · **6,408★** · pushed 2026-06-03 (active; lower stars because Go-specific)
- **last_validated:** 2026-06-03
- **assumes:** Go service
- **adapt:** fork the span/attribute conventions your services standardize on.

---

## How to use this job

Observability is a "wire it correctly once" domain — the canonical docs are complete and
current. The private skill worth building: an **incident-runbook** skill that maps your
service's key metrics/alerts to the dashboards and queries that diagnose them, so a 3am
page doesn't start from a blank PromQL box.
