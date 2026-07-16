# Job: Accountant / Bookkeeper

**You're about to:** do professional accounting/bookkeeping with an agent — ledgers, reconciliation, invoices, statements, close.

> Reputation pulled live **2026-07-16** via `gh api`.

**Pair with task jobs:** [office-documents](office-documents.md) (the official Anthropic **xlsx**/**pdf**/**docx** skills are the real Tier-A backbone here) · [pdf-generation](pdf-generation.md) (invoices/reports) · [csv-data-wrangling](csv-data-wrangling.md) (bank exports) · [data-validation-quality](data-validation-quality.md) (ledger sanity checks).

---

## Tier B 🔵 — Community-proven

### Beancount
Double-entry plain-text accounting in Python — the strongest programmable ledger for agent workflows: transactions are text, so an agent can write, query, and validate them.
- **source:** https://github.com/beancount/beancount
- **reputation:** **5,808★** · pushed 2026-05-18
- **last_validated:** 2026-07-16
- **assumes:** Python
- **adapt:** fork your chart of accounts + importers for your bank formats.

### Fava
Web UI for Beancount — balance sheets, income statements, journals. The human-review layer on top of agent-written ledgers.
- **source:** https://github.com/beancount/fava
- **reputation:** **2,528★** · pushed 2026-07-13
- **last_validated:** 2026-07-16
- **assumes:** Python, a Beancount ledger
- **adapt:** none for general use.

### hledger
Mature plain-text double-entry accounting (Haskell) — excellent CLI reporting, strict validation, CSV import rules.
- **source:** https://github.com/simonmichael/hledger
- **reputation:** **4,583★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** hledger CLI
- **adapt:** fork your CSV import rules per bank.

### Invoice Ninja
Full invoicing platform (Laravel) — invoices, quotes, payments, client portal. Self-host and drive via its API.
- **source:** https://github.com/invoiceninja/invoiceninja
- **reputation:** **9,887★** · pushed 2026-07-15
- **last_validated:** 2026-07-16
- **assumes:** PHP/Laravel or Docker
- **adapt:** fork invoice templates + payment-gateway config.

---

## Tier C 🟡 — Useful, verify

### ledger (ledger-cli)
The original plain-text accounting CLI. Still works, community quieter than hledger/beancount — verify fit before committing.
- **source:** https://github.com/ledger/ledger
- **reputation:** **5,990★** · pushed 2026-07-03
- **last_validated:** 2026-07-16
- **assumes:** C++ CLI
- **adapt:** prefer hledger/beancount for new setups.

### Akaunting
Free online accounting software (Laravel) — income/expenses/invoicing. Core is open, many features are paid apps; verify the free tier covers you.
- **source:** https://github.com/akaunting/akaunting
- **reputation:** **9,961★** · pushed 2026-07-15
- **last_validated:** 2026-07-16
- **assumes:** PHP/Laravel or Docker
- **adapt:** verify the paid-app boundary before adopting.

---

**Honest gap:** there is **no trustworthy public tax/GAAP/IFRS agent skill** — tax rules are jurisdiction-specific and change yearly; a confidently-wrong skill is worse than none. Build a **private fork**: your chart of accounts, your jurisdiction's rules, your close checklist, on top of the official Anthropic xlsx/pdf skills + Beancount.
