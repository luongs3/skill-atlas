# Job: GraphQL APIs

**You're about to:** design and build GraphQL APIs — schemas, resolvers, clients, codegen.
For REST and general API design see [api-design](api-design.md).

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### GraphQL spec
The language specification — type system, execution semantics, the source of truth for what GraphQL is.
- **source:** https://github.com/graphql/graphql-spec (docs: https://spec.graphql.org)
- **reputation:** GraphQL Foundation · **14,566★** · pushed 2026-05-25
- **last_validated:** 2026-05-25
- **assumes:** nothing
- **adapt:** none — reference. Read the spec before trusting framework-specific blog patterns.

---

## Tier B 🔵 — Community-proven

### Apollo Client
The standard client for fetching/caching GraphQL in JS apps — normalized cache, hooks, codegen.
- **source:** https://github.com/apollographql/apollo-client (docs: https://apollographql.com/docs/react)
- **reputation:** Apollo · **19,716★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** a JS/TS frontend + a GraphQL endpoint
- **adapt:** fork your cache + codegen conventions.

### Hasura GraphQL Engine
Instant GraphQL over Postgres/other DBs — useful when you want a generated API plus permissions.
- **source:** https://github.com/hasura/graphql-engine (docs: https://hasura.io/docs)
- **reputation:** Hasura · **31,976★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** a supported database
- **adapt:** fork your permission/role + relationship conventions.

---

*Substitution-resistant private skill: your schema design — how you model entities, paginate, handle
auth/authorization, and avoid N+1 in resolvers. An LLM writes a resolver fine; it doesn't know your
domain graph or your performance constraints.*
