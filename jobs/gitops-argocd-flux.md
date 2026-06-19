# Job: GitOps — Argo CD & Flux

**You're about to:** drive cluster state from Git — declarative deploys, automated sync, drift correction.

> Reputation pulled live **2026-06-19** via `gh api`.

Sits on [kubernetes-orchestration](kubernetes-orchestration.md).

---

## Tier B 🔵 — Community-proven

### Argo CD
The leading GitOps controller with a UI — syncs a cluster to a Git repo, shows drift, supports app-of-apps.
- **source:** https://github.com/argoproj/argo-cd
- **reputation:** **23,177★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a cluster
- **adapt:** fork your App/AppProject + repo structure.

### Flux
CNCF GitOps toolkit — controller-based, no UI, composes well with Kustomize/Helm. Pick over Argo when you want pure-CRD.
- **source:** https://github.com/fluxcd/flux2
- **reputation:** **8,204★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a cluster
- **adapt:** fork your GitRepository + Kustomization set.

### Argo Workflows
Kubernetes-native workflow/DAG engine — CI, batch, ML pipelines as CRDs. Different tool, same org.
- **source:** https://github.com/argoproj/argo-workflows
- **reputation:** **16,773★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a cluster
- **adapt:** fork your WorkflowTemplate set.
