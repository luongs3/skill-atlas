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

## How to use this job

Choose on where your traffic lives. **Cilium** is the default when you're Kubernetes-native and want eBPF-based networking, network policy, and observability in the data path without sidecars (its Hubble/Tetragon stack and sidecar-free mesh cut per-pod overhead). **Consul** wins when you span VMs and multiple clusters, or need service discovery + KV + mesh as one product — its decision hinges on heterogeneous, non-K8s-only topologies.

## Pitfalls

- **Sidecar tax vs eBPF tradeoffs:** sidecar meshes add latency and a memory/CPU footprint per pod; eBPF/sidecarless approaches shift that into the kernel but require recent kernel versions and tighter compatibility with your CNI.
- **mTLS rotation and clock skew:** certificate rotation, short-lived SPIFFE identities, and skewed node clocks silently break mTLS handshakes — failures look like intermittent connection resets, not config errors.
- **Policy default-deny lockout:** flipping network policy to default-deny without first mapping every required east-west flow (DNS, health checks, control plane) will partition your own services; stage it in audit/observe mode first.

---

*See [devops-infrastructure](devops-infrastructure.md) and [observability-monitoring](observability-monitoring.md). Private skill = your mesh topology + policy set.*
