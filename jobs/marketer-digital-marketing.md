# Job: Marketer / Digital Marketing

**You're about to:** run analytics, campaigns, email, and content ops with an agent — on infrastructure you control.

> Reputation pulled live **2026-07-16** via `gh api`.

**Pair with task jobs:** [workflow-automation-n8n](workflow-automation-n8n.md) (campaign glue) · [social-media-research](social-media-research.md) · [data-visualization](data-visualization.md) (reporting).

---

## Tier B 🔵 — Community-proven

### PostHog
Open-source product analytics + session replay + feature flags + A/B testing. The self-hosted growth stack an agent can query via API/SQL.
- **source:** https://github.com/PostHog/posthog
- **reputation:** **35,751★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Docker/cloud; its HogQL API
- **adapt:** fork your event taxonomy + dashboards.

### Matomo
The long-standing open-source web analytics platform (GA alternative) — full data ownership, real reporting API.
- **source:** https://github.com/matomo-org/matomo
- **reputation:** **21,691★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** PHP or Docker
- **adapt:** fork your goal/funnel definitions.

### Mautic
Open-source marketing automation — email campaigns, lead scoring, segments, drip flows. The self-hosted HubSpot-shaped piece.
- **source:** https://github.com/mautic/mautic
- **reputation:** **10,142★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** PHP or Docker
- **adapt:** fork your email templates + scoring model.

### listmonk
High-performance self-hosted newsletter + mailing-list manager (Go, single binary) with a clean API — the simplest reliable email-send layer for agent campaigns.
- **source:** https://github.com/knadh/listmonk
- **reputation:** **22,152★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** a binary + Postgres; an SMTP provider
- **adapt:** fork templates; mind deliverability (SPF/DKIM) yourself.

### umami
Simple, privacy-focused web analytics — when you need traffic numbers without the GA weight.
- **source:** https://github.com/umami-software/umami
- **reputation:** **37,697★** · pushed 2026-07-15
- **last_validated:** 2026-07-16
- **assumes:** Node + Postgres/MySQL
- **adapt:** none.

---

**Honest gap:** platform-API skills (Google Ads, Meta, TikTok) exist only as SDKs, not trustworthy public agent skills — and they churn quarterly. Campaign strategy/brand voice is inherently a **private fork** (your ICP, your tone, your offer math).
