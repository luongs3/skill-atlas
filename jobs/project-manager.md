# Job: Project Manager

**You're about to:** plan, track, and report on projects with an agent — boards, timelines, status reports, resource views.

> Reputation pulled live **2026-07-16** via `gh api`.

**Pair with task jobs:** [office-documents](office-documents.md) (status decks/docs) · [workflow-automation-n8n](workflow-automation-n8n.md) (standup digests, reminders) · [data-visualization](data-visualization.md) (burn-downs).

---

## Tier B 🔵 — Community-proven

### Plane
Modern open-source project tracker (issues, cycles, modules — Jira/Linear-shaped) with an API an agent can drive for planning + status.
- **source:** https://github.com/makeplane/plane
- **reputation:** **54,591★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Docker or their cloud
- **adapt:** fork your workflow states + report templates.

### OpenProject
The heavyweight open-source PM suite — Gantt, work packages, budgets, agile boards. Closest OSS to MS Project + Jira combined.
- **source:** https://github.com/opf/openproject
- **reputation:** **15,573★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Rails/Docker
- **adapt:** fork your project templates + roles.

### Focalboard
Kanban/boards (Notion-board-shaped). Handed from Mattermost core to community maintenance — verify current health before adopting.
- **source:** https://github.com/mattermost-community/focalboard
- **reputation:** **26,290★** · pushed 2026-05-18
- **last_validated:** 2026-07-16
- **assumes:** Go binary/Docker or inside Mattermost
- **adapt:** prefer Plane for new setups.

### Wekan
Veteran open-source kanban. Works; UI dated; fine when you just need boards.
- **source:** https://github.com/wekan/wekan
- **reputation:** **20,994★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Docker/Snap
- **adapt:** none.

---

**Honest gap:** PM judgment (estimation, stakeholder management, YOUR status-report format) is a private fork. The tools above are the tracking substrate an agent reads/writes.
