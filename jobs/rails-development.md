# Job: Rails Development

**You're about to:** build a Ruby on Rails app — MVC, Active Record, convention over configuration.
All canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### Rails + official guides
The framework itself and the official guides (getting started, Active Record, routing, security).
- **source:** https://github.com/rails/rails (docs: https://guides.rubyonrails.org/)
- **reputation:** The Rails project · **58,481★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Ruby installed
- **adapt:** none — reference.

### Rails Guides — Active Record & migrations
The official guides for the ORM: associations, validations, migrations, query interface.
- **source:** https://guides.rubyonrails.org/active_record_basics.html
- **reputation:** Official Rails documentation
- **last_validated:** 2026-06-04
- **assumes:** Rails app scaffolded
- **adapt:** fork your concern layout, service-object pattern, and migration conventions.

---

## Tier B 🔵 — Community-proven

### Rails API docs
The full API reference for Rails modules — ActionController, ActiveSupport, ActionView.
- **source:** https://api.rubyonrails.org/
- **reputation:** Official Rails API documentation
- **last_validated:** 2026-06-04
- **assumes:** Rails project
- **adapt:** none — reference.

### Rails security guide
The official guide to securing a Rails app — CSRF, SQL injection, mass assignment, sessions.
- **source:** https://guides.rubyonrails.org/security.html
- **reputation:** Official Rails documentation
- **last_validated:** 2026-06-04
- **assumes:** Rails app
- **adapt:** fork your strong-params, CSP, and session-store conventions.

---

*Substitution-resistant private skill: your project's service-object pattern, concern layout, auth
flow, and error-handling conventions. An LLM writes Rails controllers fine; it doesn't know your rules.*
