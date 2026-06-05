# Job: Headless CMS

**You're about to:** manage content via API — headless CMS for sites, apps, and storefronts.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Strapi
The leading open-source headless CMS — customizable content types + REST/GraphQL API.
- **source:** https://github.com/strapi/strapi (docs: https://docs.strapi.io)
- **reputation:** **72,315★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** Node + a database
- **adapt:** fork your content-type + role conventions.

---

## Tier B 🔵 — Community-proven

### Directus
Headless CMS + data platform that wraps any SQL database.
- **source:** https://github.com/directus/directus (docs: https://docs.directus.io)
- **reputation:** **36,036★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a SQL database
- **adapt:** use Directus to wrap an existing DB; Strapi to start fresh.

---

## How to use this job

Use **Strapi** when you're starting fresh and want to model content from scratch — define content types in its admin and get REST + GraphQL plus a role/permission system out of the box. Use **Directus** when you already have a SQL database and want a CMS/admin layer wrapped *around the existing schema* without migrating data. The decision hinges on greenfield vs existing data: Strapi owns its schema, Directus adapts to yours.

## Pitfalls

- **Strapi major-version upgrades are migrations, not bumps** — the v3→v4→v5 jumps changed the content API, plugin format, and database layer; custom code and plugins often need rewrites. Pin the version and budget real time for upgrades.
- **Public-role permissions default to locked, and it's easy to over-open them** — granting `find`/`findOne` to the public role to "make the API work" can expose draft or private content. Audit role permissions per content type before launch.
- **Directus is a thin layer over your schema, so destructive DB changes leak through** — renaming/dropping columns outside Directus desyncs its metadata, and deep relational queries can generate heavy SQL. Manage schema changes through Directus (or keep its metadata in sync) and watch query depth/limits.

---

*See [api-design](api-design.md). Private skill = your content model + the frontend's consumption pattern.*
