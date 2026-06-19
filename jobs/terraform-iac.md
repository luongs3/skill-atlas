# Job: Infrastructure as Code — Terraform / OpenTofu

**You're about to:** define cloud infra declaratively — providers, state, modules, plan/apply, drift.

> Reputation pulled live **2026-06-19** via `gh api`.

Pair with [cloud-aws-gcp](cloud-aws-gcp.md) for the provider side.

---

## Tier A 🟢 — Canonical

### Terraform
The reference IaC tool — HCL, state, providers, modules. Docs define provider + state semantics.
- **source:** https://github.com/hashicorp/terraform
- **reputation:** **48,738★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a cloud account + credentials
- **adapt:** fork your module layout + remote-state backend.

---

## Tier B 🔵 — Community-proven

### OpenTofu
The MPL-licensed community fork of Terraform after the BSL relicense — drop-in compatible. Pick it if license matters.
- **source:** https://github.com/opentofu/opentofu
- **reputation:** **29,102★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** same as Terraform
- **adapt:** swap the binary; mind provider registry config.

### terraform-aws-modules (VPC et al.)
Battle-tested community AWS modules — VPC, EKS, RDS. Read before trusting; they encode real opinions.
- **source:** https://github.com/terraform-aws-modules/terraform-aws-vpc
- **reputation:** **3,239★** · pushed 2026-04-02
- **last_validated:** 2026-06-19
- **assumes:** AWS provider
- **adapt:** fork the module call + your variable values.
