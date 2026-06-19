# Job: Prometheus — Metrics & Alerting

**You're about to:** scrape and store time-series metrics, write PromQL, fire alerts.

> Reputation pulled live **2026-06-19** via `gh api`.

Visualize with [grafana-dashboards](grafana-dashboards.md); broader picture in [observability-monitoring](observability-monitoring.md).

---

## Tier A 🟢 — Canonical

### Prometheus
The de-facto metrics system — pull model, PromQL, alerting rules. Docs define PromQL + exposition format.
- **source:** https://github.com/prometheus/prometheus
- **reputation:** **64,622★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** scrape targets exposing /metrics
- **adapt:** fork your recording + alerting rules; mind cardinality.

---

## Tier B 🔵 — Community-proven

### Alertmanager
Routing, grouping, silencing, and dedup for Prometheus alerts. The piece people under-configure.
- **source:** https://github.com/prometheus/alertmanager
- **reputation:** **8,507★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Prometheus firing alerts
- **adapt:** fork your routing tree + receivers.

### node_exporter
Host-level metrics (CPU/mem/disk/net) — the baseline exporter on every machine.
- **source:** https://github.com/prometheus/node_exporter
- **reputation:** **13,515★** · pushed 2026-06-09
- **last_validated:** 2026-06-19
- **assumes:** Linux hosts
- **adapt:** deploy per node; scrape it.
