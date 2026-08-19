# Job: Stripe — Payments Integration

**You're about to:** take payments, run subscriptions, and handle webhooks correctly — idempotency, SCA, billing.

> Reputation pulled live **2026-06-19** via `gh api`.

---

## Tier A 🟢 — Canonical

### Stripe Node SDK
Official Node SDK — PaymentIntents, subscriptions, webhooks. The reference for correct payment flows.
- **source:** https://github.com/stripe/stripe-node
- **reputation:** **4,449★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a Stripe account
- **adapt:** fork your webhook handlers + idempotency keys (never trust client amounts).

### Stripe Python SDK
Official Python SDK — same coverage for Python backends. Pair with the API docs.
- **source:** https://github.com/stripe/stripe-python
- **reputation:** **2,015★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a Stripe account
- **adapt:** fork your webhook + reconciliation logic.

---

## Tier B 🔵 — Community-proven

### Stripe CLI
Local webhook forwarding + event triggering — test payment flows without a public URL. Essential for dev.
- **source:** https://github.com/stripe/stripe-cli
- **reputation:** **2,080★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a Stripe account
- **adapt:** use to replay/trigger events in dev.

---

## Tier C 🟡 — Useful, verify

### internet-court/internet-court-skill
The trust layer for agent-to-agent commerce — natural-language mandates, ERC-7710 delegated permissions, x402 payments, escrow, and dispute 
- **source:** https://github.com/internet-court/internet-court-skill
- **reputation:** 3,996★ · pushed 2026-08-11 (auto-added 2026-08-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-19
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.
