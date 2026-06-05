# Job: Service Mesh & Cloud Networking

**You're about to:** add a service mesh, mTLS, or eBPF networking to a Kubernetes cluster.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Cilium
eBPF-based networking, security, and observability for K8s.
- **source:** https://github.com/cilium/cilium (docs: https://docs.cilium.io)
- **reputation:** Official (CNCF) · **24,450★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a Kubernetes cluster
- **adapt:** fork your network-policy conventions.

### HashiCorp Consul
Service discovery + service mesh + health checking.
- **source:** https://github.com/hashicorp/consul (docs: https://developer.hashicorp.com/consul)
- **reputation:** Official HashiCorp · **29,909★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a cluster or VMs
- **adapt:** none — reference.

---

*See [devops-infrastructure](devops-infrastructure.md) and [observability-monitoring](observability-monitoring.md). Private skill = your mesh topology + policy set.*
