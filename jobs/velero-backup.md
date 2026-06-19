# Job: Velero — Kubernetes Backup & DR

**You're about to:** back up and restore cluster state + persistent volumes, and migrate between clusters.

> Reputation pulled live **2026-06-19** via `gh api`.

Runs against [kubernetes-orchestration](kubernetes-orchestration.md).

---

## Tier A 🟢 — Canonical

### Velero
The standard K8s backup/restore + DR tool — schedules, volume snapshots, cluster migration to object storage.
- **source:** https://github.com/vmware-tanzu/velero
- **reputation:** **10,068★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a cluster + object storage
- **adapt:** fork your backup schedules + restore runbook.
