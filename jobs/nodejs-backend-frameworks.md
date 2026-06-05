# Job: Node.js Backend Frameworks

**You're about to:** build a Node.js backend — pick minimal (Express) or structured (NestJS), route, middleware, serve.
All canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### Express — minimal
The minimalist, unopinionated web framework — routing + middleware, nothing more.
- **source:** https://github.com/expressjs/express (docs: https://expressjs.com/)
- **reputation:** The Express project · **69,076★** · pushed 2026-06-02
- **last_validated:** 2026-06-04
- **assumes:** Node.js installed
- **adapt:** fork your middleware order, router layout, and error-handler conventions.

### NestJS — structured
The opinionated, TypeScript-first framework — modules, DI, decorators for larger apps.
- **source:** https://github.com/nestjs/nest (docs: https://docs.nestjs.com/)
- **reputation:** The NestJS project · **75,654★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Node.js installed
- **adapt:** fork your module boundaries, provider wiring, and exception-filter conventions.

---

## Tier B 🔵 — Community-proven

### Node.js official docs
The runtime API reference — http, streams, fs, and the standard library.
- **source:** https://nodejs.org/docs/latest/api/
- **reputation:** Official Node.js documentation
- **last_validated:** 2026-06-04
- **assumes:** Node.js installed
- **adapt:** none — reference.

### Express security best practices
The official production hardening guide — helmet, TLS, rate limiting, dependency hygiene.
- **source:** https://expressjs.com/en/advanced/best-practice-security.html
- **reputation:** Official Express documentation
- **last_validated:** 2026-06-04
- **assumes:** Express app
- **adapt:** fork your helmet config, CORS policy, and rate-limit conventions.

---

*Substitution-resistant private skill: your project's middleware/module layout, auth flow, and
error-handling conventions. An LLM writes Express/Nest routes fine; it doesn't know your repo's rules.*
