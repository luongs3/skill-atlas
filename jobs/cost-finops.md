# Job: Cloud Cost & FinOps

**You're about to:** see and control cloud spend — cost-per-PR estimates, Kubernetes cost allocation, rightsizing.

> Reputation pulled live **2026-06-19** via `gh api`.

---

## Tier A 🟢 — Canonical

### Infracost
Shows cloud cost diffs on Terraform PRs before apply — shift-left FinOps in CI.
- **source:** https://github.com/infracost/infracost
- **reputation:** **12,372★** · pushed 2026-06-03
- **last_validated:** 2026-06-19
- **assumes:** Terraform + CI
- **adapt:** fork the CI step + your cost policies.

---

## Tier B 🔵 — Community-proven

### OpenCost
CNCF Kubernetes cost monitoring — per-namespace/workload allocation. The vendor-neutral Kubecost core.
- **source:** https://github.com/opencost/opencost
- **reputation:** **6,599★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a cluster
- **adapt:** fork your allocation queries + showback.
