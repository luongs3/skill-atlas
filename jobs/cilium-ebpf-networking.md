# Job: Cilium & eBPF Networking

**You're about to:** use eBPF for high-performance K8s networking, network policy, and observability (Hubble).

> Reputation pulled live **2026-06-19** via `gh api`.

Deeper mesh in [service-mesh-networking](service-mesh-networking.md).

---

## Tier A 🟢 — Canonical

### Cilium
CNCF eBPF-based CNI — identity-aware network policy, load balancing, Hubble flow visibility. The modern K8s dataplane.
- **source:** https://github.com/cilium/cilium
- **reputation:** **24,546★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a cluster (kernel with eBPF)
- **adapt:** fork your NetworkPolicies + Hubble setup.

---

## Tier B 🔵 — Community-proven

### cilium/ebpf (Go library)
Pure-Go eBPF library — load and manage eBPF programs without cgo. For building your own eBPF tooling.
- **source:** https://github.com/cilium/ebpf
- **reputation:** **7,807★** · pushed 2026-06-10
- **last_validated:** 2026-06-19
- **assumes:** Go + a recent Linux kernel
- **adapt:** fork the loader pattern you need.
