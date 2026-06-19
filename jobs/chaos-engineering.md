# Job: Chaos Engineering

**You're about to:** inject controlled failure (pod kills, latency, network loss) to prove resilience before prod does it for you.

> Reputation pulled live **2026-06-19** via `gh api`.

Runs against [kubernetes-orchestration](kubernetes-orchestration.md).

---

## Tier B 🔵 — Community-proven

### Chaos Mesh
CNCF Kubernetes-native chaos — pod/network/IO/time faults as CRDs, with a dashboard. The K8s default.
- **source:** https://github.com/chaos-mesh/chaos-mesh
- **reputation:** **7,757★** · pushed 2026-06-14
- **last_validated:** 2026-06-19
- **assumes:** a cluster
- **adapt:** fork your experiment CRDs + steady-state checks.

### LitmusChaos
GitOps-friendly chaos platform for K8s — experiment hub, workflows. Alternative to Chaos Mesh.
- **source:** https://github.com/litmuschaos/litmus
- **reputation:** **5,465★** · pushed 2026-06-17
- **last_validated:** 2026-06-19
- **assumes:** a cluster
- **adapt:** fork your chaos workflows.
