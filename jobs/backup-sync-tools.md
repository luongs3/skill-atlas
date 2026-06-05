# Job: Backup & File Sync

**You're about to:** back up and sync data reliably — encrypted, deduplicated, to any storage.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### restic
Fast, encrypted, deduplicated backups to many backends. Simple and trustworthy.
- **source:** https://github.com/restic/restic (docs: https://restic.readthedocs.io)
- **reputation:** **33,869★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a backup target
- **adapt:** fork your snapshot + retention policy.

### rclone
Sync files to/from 70+ cloud storage providers (the rsync for cloud).
- **source:** https://github.com/rclone/rclone (docs: https://rclone.org)
- **reputation:** **57,732★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** storage credentials
- **adapt:** fork your remote + sync-flag conventions.

---

## Tier B 🔵 — Community-proven

### BorgBackup
Deduplicating encrypted backups, popular for servers.
- **source:** https://github.com/borgbackup/borg
- **reputation:** **13,390★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a backup host
- **adapt:** pick restic OR borg.

---

*The failure mode is a backup that runs but never restores. Verify restores, not just backups (Rule D). Private skill = your backup schedule + tested restore procedure.*
