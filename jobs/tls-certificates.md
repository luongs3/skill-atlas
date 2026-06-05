# Job: TLS Certificates & HTTPS

**You're about to:** issue, renew, and manage TLS certs — Let's Encrypt, local dev certs.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Certbot
The standard Let's Encrypt ACME client for issuing + auto-renewing certs.
- **source:** https://github.com/certbot/certbot (docs: https://eff-certbot.readthedocs.io)
- **reputation:** Official EFF · **33,071★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a public domain + server
- **adapt:** fork your renewal-hook + deploy conventions.

---

## Tier C 🟡 — Useful, verify

### mkcert (local dev)
Locally-trusted dev certificates with one command. NOTE: last pushed 2024-08, but stable and still works.
- **source:** https://github.com/FiloSottile/mkcert
- **reputation:** **59,020★** but pushed 2024-08-13 (stable, low-churn tool)
- **last_validated:** 2026-06-05
- **assumes:** local dev
- **adapt:** dev-only; never for production.

---

*Common failure: certs that issue but don't auto-renew (Rule-D territory — verify renewal, not just issuance). Private skill = your renewal + reload pipeline. See [nginx-web-servers](nginx-web-servers.md).*
