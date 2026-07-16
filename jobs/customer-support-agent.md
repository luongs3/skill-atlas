# Job: Customer Support Agent / Support Ops

**You're about to:** run a helpdesk — triage tickets, draft replies, manage knowledge bases — with an agent.

> Reputation pulled live **2026-07-16** via `gh api`.

**Pair with task jobs:** [workflow-automation-n8n](workflow-automation-n8n.md) (ticket routing) · [search-meilisearch-typesense](search-meilisearch-typesense.md) (KB search) · [rag-retrieval](rag-retrieval.md) (product-knowledge answers).

---

## Tier B 🔵 — Community-proven

### Chatwoot
Open-source omnichannel support (email, chat, socials) with a real API + agent-bot framework — the natural place to wire an LLM agent into a support queue.
- **source:** https://github.com/chatwoot/chatwoot
- **reputation:** **34,479★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Rails/Docker or their cloud
- **adapt:** fork your macros/canned responses + escalation rules.

### Zammad
Mature open-source helpdesk/ticketing (web, email, phone) — strong ticket model, KB, REST API.
- **source:** https://github.com/zammad/zammad
- **reputation:** **5,761★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Rails/Docker
- **adapt:** fork your SLA + routing config.

### FreeScout
Lightweight self-hosted shared-inbox helpdesk (Laravel) — the low-ops option for small teams.
- **source:** https://github.com/freescout-help-desk/freescout
- **reputation:** **4,422★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** PHP
- **adapt:** fork your saved replies.

---

**Honest gap:** YOUR product knowledge is the entire value of a support agent — that's a private RAG/KB fork, not a public skill. Tone/refund-policy/escalation rules likewise.
