# Job: Authentication & Authorization

**You're about to:** implement login/identity, OAuth/OIDC, JWT handling, or access control.
Strong canonical identity servers + high-rep Go libraries.

> Reputation pulled live **2026-06-03** via `gh api`. Security-sensitive domain — prefer
> battle-tested libraries over rolling your own.

---

## Tier A 🟢 — Canonical (identity servers)

### Keycloak — full identity & access management
The leading open-source IAM: OIDC/SAML, user federation, social login, admin UI.
- **source:** https://github.com/keycloak/keycloak (docs: https://www.keycloak.org/documentation)
- **reputation:** Official (Red Hat/CNCF) · **34,711★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a server to host it
- **adapt:** fork your realm/client config conventions.

### Ory Kratos + Hydra
Cloud-native identity (Kratos = users/login) and OAuth2/OIDC provider (Hydra). API-first,
good fit for a Go microservices stack.
- **source:** https://github.com/ory/kratos (13,678★) · https://github.com/ory/hydra (17,192★) · pushed 2026-06-01
- **reputation:** Official Ory · high stars + actively maintained
- **last_validated:** 2026-06-03
- **assumes:** containerized deployment
- **adapt:** none — reference + self-host config.

---

## Tier B 🔵 — Community-proven (Go libraries)

### golang-jwt — JWT for Go
The maintained successor to dgrijalva/jwt-go; the standard JWT library for Go.
- **source:** https://github.com/golang-jwt/jwt
- **reputation:** **9,109★** · pushed 2026-06-02 (the actively-maintained fork — use this, NOT the archived dgrijalva original)
- **last_validated:** 2026-06-03
- **assumes:** Go
- **adapt:** fork your token claims + validation rules into a private skill.

### Casbin — authorization (RBAC/ABAC/ACL)
The standard pluggable authorization library for Go (and many other languages).
- **source:** https://github.com/casbin/casbin
- **reputation:** **20,159★** · pushed 2026-05-15
- **last_validated:** 2026-06-03
- **assumes:** Go
- **adapt:** fork your policy model (RBAC vs ABAC) and rules.

---

*The non-negotiable lesson for this job: **don't roll your own auth.** An LLM can write a
JWT verify loop, but the edge cases (algorithm confusion, clock skew, key rotation, replay)
are exactly where DIY auth fails. The atlas points at the libraries that already handle them.*
