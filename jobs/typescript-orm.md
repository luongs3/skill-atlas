# Job: TypeScript ORMs

**You're about to:** talk to a database from TS with type safety — Prisma, Drizzle, TypeORM.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier B 🔵 — Community-proven

### Prisma
Type-safe ORM with schema-first modeling and migrations; the popular default.
- **source:** https://github.com/prisma/prisma (docs: https://www.prisma.io/docs)
- **reputation:** **46,068★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** Node + a database
- **adapt:** fork your schema + migration conventions.

### Drizzle / TypeORM
Drizzle (SQL-first, lightweight, edge-friendly) and TypeORM (decorator-based, mature).
- **source:** https://github.com/drizzle-team/drizzle-orm (34,678★) · https://github.com/typeorm/typeorm (36,525★)
- **reputation:** high stars, maintained, pushed 2026-06
- **last_validated:** 2026-06-05
- **assumes:** Node + DB
- **adapt:** Drizzle for SQL-first/edge; Prisma for DX; pick one.

---

## How to use this job

Pick on how close you want to stay to SQL. **Prisma** gives the smoothest DX — schema-first modeling, generated client, managed migrations — at the cost of a heavier abstraction and a generated query engine. **Drizzle** is SQL-first and lightweight, with a tiny runtime that fits edge/serverless and lets you write queries that read like SQL. **TypeORM** is the mature decorator/Active Record option for codebases already invested in it. Choose one and standardize.

## Pitfalls

- **N+1 queries behind lazy relations:** loading a list then accessing a relation per row fires one query per item. It's invisible until you log SQL or watch latency — use eager `include`/`with`/joins and inspect generated queries.
- **Migration drift:** the schema file, the migration history, and the actual database can diverge — especially after manual DB edits or `db push` in dev. Treat migrations as the source of truth, run them in CI, and diff against prod before deploy.
- **Type safety ≠ runtime safety:** generated types reflect the schema at codegen time, not the live DB. A column dropped or retyped out-of-band compiles fine and fails at runtime; raw queries also bypass the type layer entirely.

---

*See [databases-sql](databases-sql.md) and [typescript-javascript](typescript-javascript.md). Private skill = your schema + query conventions.*
