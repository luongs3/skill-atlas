# Job: Helm — Kubernetes Package Manager

**You're about to:** package and template Kubernetes apps with Helm charts — values, releases, upgrades, rollbacks.

> Reputation pulled live **2026-06-19** via `gh api`.

Sits on top of [kubernetes-orchestration](kubernetes-orchestration.md).

---

## Tier A 🟢 — Canonical

### Helm
The de-facto K8s package manager — charts, `values.yaml`, release lifecycle, hooks. The docs define chart best-practice.
- **source:** https://github.com/helm/helm
- **reputation:** **29,891★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a cluster + kubectl
- **adapt:** fork a chart skeleton; pin chart + app versions.

---

## Tier D 🔴 — Caution

### helm/charts (archived classic charts)
The original community charts monorepo — ARCHIVED, superseded by per-project repos. Listed so you don't pull stale charts from it.
- **source:** https://github.com/helm/charts
- **reputation:** **15,424★** · pushed 2022-02-20 · ⚠️ ARCHIVED
- **last_validated:** 2026-06-19
- **assumes:** none
- **adapt:** do not use; find the project's own chart repo.
