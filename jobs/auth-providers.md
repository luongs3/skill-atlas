# Job: Auth Providers — Keycloak, Auth.js, Authentik

**You're about to:** add login, SSO, and OIDC/OAuth to apps without hand-rolling auth.

> Reputation pulled live **2026-06-19** via `gh api`.

Protocol-level depth in [authentication-authorization](authentication-authorization.md).

---

## Tier A 🟢 — Canonical

### Keycloak
Mature open IAM — OIDC/SAML, social login, user federation, fine-grained roles. The self-host SSO standard.
- **source:** https://github.com/keycloak/keycloak
- **reputation:** **34,989★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** JVM + a DB
- **adapt:** fork your realm config + client scopes.

### Auth.js (NextAuth)
Auth for Next.js/JS apps — providers, sessions, JWT/DB strategies. The default for the JS ecosystem.
- **source:** https://github.com/nextauthjs/next-auth
- **reputation:** **28,274★** · pushed 2026-06-12
- **last_validated:** 2026-06-19
- **assumes:** a JS app
- **adapt:** fork your providers + session/callback config.

---

## Tier B 🔵 — Community-proven

### authentik
Modern self-hosted IdP — OIDC/SAML/LDAP, flows-as-config, slick UI. A lighter Keycloak alternative.
- **source:** https://github.com/goauthentik/authentik
- **reputation:** **22,064★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Docker
- **adapt:** fork your flows + providers.

### Ory Kratos
API-first identity (no UI lock-in) — headless login/registration/recovery. Pick when you own the frontend.
- **source:** https://github.com/ory/kratos
- **reputation:** **13,708★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Go service + a DB
- **adapt:** fork your identity schema + self-service flows.
