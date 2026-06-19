# Job: Envoy — L7 Proxy & Edge

**You're about to:** route, balance, and observe service traffic with Envoy — the dataplane under most service meshes.

> Reputation pulled live **2026-06-19** via `gh api`.

Mesh control planes in [service-mesh-networking](service-mesh-networking.md).

---

## Tier A 🟢 — Canonical

### Envoy
CNCF high-performance L7 proxy — dynamic config (xDS), observability, the dataplane behind Istio. Docs define the config model.
- **source:** https://github.com/envoyproxy/envoy
- **reputation:** **28,429★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a service topology
- **adapt:** fork your listener/cluster/route config or its xDS source.
