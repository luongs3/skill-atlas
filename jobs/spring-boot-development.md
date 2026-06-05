# Job: Spring Boot Development

**You're about to:** build a Java/Spring Boot service — dependency injection, auto-configuration, REST APIs.
All canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### Spring Boot + official docs
The framework itself and the official docs (reference guide, getting started, auto-configuration).
- **source:** https://github.com/spring-projects/spring-boot (docs: https://spring.io/projects/spring-boot)
- **reputation:** The Spring project · **80,769★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** JDK installed
- **adapt:** none — reference.

### Spring Boot reference — features & web
The official reference: configuration, profiles, data access, Spring MVC, actuator.
- **source:** https://docs.spring.io/spring-boot/docs/current/reference/html/
- **reputation:** Official Spring Boot documentation
- **last_validated:** 2026-06-04
- **assumes:** Spring Boot project scaffolded
- **adapt:** fork your package layout, bean configuration, and profile/properties conventions.

---

## Tier B 🔵 — Community-proven

### Spring Guides
The official short, task-focused guides — REST service, securing a web app, data JPA.
- **source:** https://spring.io/guides
- **reputation:** Official Spring documentation
- **last_validated:** 2026-06-04
- **assumes:** Spring Boot project
- **adapt:** fork your layering (controller/service/repo) and exception-handler conventions.

### Spring Security reference
The official reference for auth/authz — filters, OAuth2, method security, password storage.
- **source:** https://docs.spring.io/spring-security/reference/
- **reputation:** Official Spring documentation
- **last_validated:** 2026-06-04
- **assumes:** Spring Boot project
- **adapt:** fork your security-filter chain + token/session conventions.

---

*Substitution-resistant private skill: your project's package layout, bean/profile config, auth flow,
and error-handling conventions. An LLM writes Spring controllers fine; it doesn't know your repo's rules.*
