# Job: Kubernetes — Container Orchestration

**You're about to:** run containers in production on Kubernetes — deployments, services, ingress, autoscaling, the YAML that keeps it correct.

> Reputation pulled live **2026-06-19** via `gh api`.

Pair with [docker-containers](docker-containers.md) for the image layer and [helm-package-manager](helm-package-manager.md) to template releases.

---

## Tier A 🟢 — Canonical

### Kubernetes source + docs
The orchestrator itself — the API reference behind every Deployment, Service, and controller. Read the concepts docs, not blog posts.
- **source:** https://github.com/kubernetes/kubernetes (docs: https://kubernetes.io/docs/)
- **reputation:** CNCF · **123,127★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a cluster (kind/minikube/EKS/GKE)
- **adapt:** none — reference. Pin your manifests to the server version you run.

---

## Tier B 🔵 — Community-proven

### Kustomize
Template-free manifest customization — overlays per environment without a templating language. Built into `kubectl`.
- **source:** https://github.com/kubernetes-sigs/kustomize
- **reputation:** **12,076★** · pushed 2026-06-08
- **last_validated:** 2026-06-19
- **assumes:** kubectl
- **adapt:** fork your base + overlays layout.

### kubectl
The official CLI — every cluster interaction. Learn the imperative-to-declarative workflow and `kubectl explain`.
- **source:** https://github.com/kubernetes/kubectl
- **reputation:** **3,298★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a kubeconfig
- **adapt:** alias your common verbs; keep contexts per cluster.
