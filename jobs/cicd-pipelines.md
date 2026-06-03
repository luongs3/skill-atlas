# Job: CI/CD Pipelines

**You're about to:** set up continuous integration/deployment — GitHub Actions, GitOps,
or a deploy pipeline. Canonical official sources + high-rep GitOps tools.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical

### GitHub Actions starter workflows
Official, ready-to-use workflow templates for CI, deploy, linting across languages.
- **source:** https://github.com/actions/starter-workflows (docs: https://docs.github.com/actions)
- **reputation:** Official GitHub · **11,658★** · pushed 2026-06-01
- **last_validated:** 2026-06-03
- **assumes:** a GitHub repo
- **adapt:** copy the Go/Docker workflow, then harden (caching, matrix, secrets). See this
  atlas's own `.github/workflows/revalidate.yml` as a worked example.

---

## Tier B 🔵 — Community-proven (GitOps / CD)

### Argo CD — GitOps continuous delivery for Kubernetes
The leading GitOps CD tool — declarative, git-as-source-of-truth deploys to K8s.
- **source:** https://github.com/argoproj/argo-cd (docs: https://argo-cd.readthedocs.io)
- **reputation:** Official Argo (CNCF) · **23,040★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **assumes:** a Kubernetes cluster
- **adapt:** fork your app-of-apps structure + sync conventions.

### Flux — GitOps toolkit (alternative)
The other major CNCF GitOps tool. Pick Argo OR Flux based on team preference.
- **source:** https://github.com/fluxcd/flux2 (docs: https://fluxcd.io/docs/)
- **reputation:** Official Flux (CNCF) · **8,159★** · pushed 2026-06-01
- **last_validated:** 2026-06-03
- **assumes:** Kubernetes
- **adapt:** don't run both Argo and Flux; choose one.

---

*CI/CD is highly org-specific. The private skill: your pipeline's exact stages (test →
build → scan → deploy), your secrets/registry, and your rollback procedure — encoded so a
new service gets a correct pipeline without re-deriving it.*
