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

---

## Tier C 🟡 — Useful, verify

### getagentseal/codeburn
Free, local tool to track AI coding token usage and cost across 31 tools and agents (Claude Code, Cursor, Codex, Gemini and more), by model,
- **source:** https://github.com/getagentseal/codeburn
- **reputation:** 9,193★ · pushed 2026-08-04 (auto-added 2026-08-08 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-08
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.
