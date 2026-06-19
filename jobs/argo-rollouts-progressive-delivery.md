# Job: Progressive Delivery — Canary & Blue/Green

**You're about to:** ship safely with automated canary/blue-green rollouts and metric-based analysis + auto-rollback.

> Reputation pulled live **2026-06-19** via `gh api`.

Pairs with [gitops-argocd-flux](gitops-argocd-flux.md).

---

## Tier B 🔵 — Community-proven

### Argo Rollouts
K8s controller for canary + blue-green with analysis runs that auto-rollback on bad metrics.
- **source:** https://github.com/argoproj/argo-rollouts
- **reputation:** **3,503★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a cluster + a metrics source
- **adapt:** fork your Rollout strategy + AnalysisTemplates.

### Flagger
Progressive delivery operator (canary/AB/blue-green) driven by Prometheus/OTel metrics. Flux-aligned alternative.
- **source:** https://github.com/fluxcd/flagger
- **reputation:** **5,363★** · pushed 2026-06-15
- **last_validated:** 2026-06-19
- **assumes:** a cluster + mesh/ingress
- **adapt:** fork your Canary resources.
