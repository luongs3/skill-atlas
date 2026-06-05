# Job: Workflow Automation (n8n)

**You're about to:** automate workflows visually — connect apps, APIs, and triggers without glue code.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### n8n
Fair-code workflow automation; self-hostable, 400+ integrations, code nodes when you need them.
- **source:** https://github.com/n8n-io/n8n (docs: https://docs.n8n.io)
- **reputation:** Official n8n · **191,135★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** a self-host or cloud instance
- **adapt:** fork your credential + error-workflow conventions.

---

## How to use this job

Reach for **n8n** when you need to wire SaaS apps, webhooks, and APIs together quickly and want a visual canvas non-engineers can read — it's the no/low-code layer, with Code nodes as an escape hatch for the 10% that needs real logic. Self-host (fair-code license) when data residency or unlimited executions matter; use n8n Cloud to skip ops. The decision vs. code-first orchestration (see [data-engineering](data-engineering.md)) hinges on workflow complexity and who maintains it — n8n excels at glue, not at heavy data pipelines or strict idempotency guarantees.

## Pitfalls

- **No built-in idempotency.** A webhook retried by the source, or a workflow re-run, fires side effects twice (duplicate emails, double charges). Add your own dedup key check; n8n won't deduplicate for you.
- **Self-hosted upgrades break workflows.** Node versions and the execution engine change across releases; pinned community nodes and credentials can silently stop working after an upgrade. Pin the n8n image version, back up the database, and test upgrades on a staging instance.
- **Execution data and credentials are sensitive at rest.** Full payloads are stored in execution history (handy for debugging, risky for PII), and credentials live in the DB encrypted only by your `N8N_ENCRYPTION_KEY`. Lose that key and credentials are unrecoverable; leak it and they're exposed. Set retention pruning and guard the key.

*n8n is the no-code layer; for code-first orchestration see [data-engineering](data-engineering.md). Private skill = your standard sub-workflows + credential store.*
