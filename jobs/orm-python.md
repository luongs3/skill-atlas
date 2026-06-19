# Job: Python ORMs & Query Builders

**You're about to:** map Python objects to SQL safely — models, migrations, relationships, async.

> Reputation pulled live **2026-06-19** via `gh api`.

TS side in [typescript-orm](typescript-orm.md); raw SQL depth in [postgresql-database](postgresql-database.md).

---

## Tier A 🟢 — Canonical

### SQLAlchemy
The Python SQL toolkit + ORM — Core + ORM, async, fine control. The reference for serious Python data access.
- **source:** https://github.com/sqlalchemy/sqlalchemy
- **reputation:** **11,926★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** fork your models + session/engine config.

### Alembic
SQLAlchemy's migration tool — autogenerate + hand-edit revisions. The standard Python migration path.
- **source:** https://github.com/sqlalchemy/alembic
- **reputation:** **4,209★** · pushed 2026-05-31
- **last_validated:** 2026-06-19
- **assumes:** SQLAlchemy
- **adapt:** fork your migration env + naming convention.

---

## Tier B 🔵 — Community-proven

### SQLModel
Pydantic + SQLAlchemy models in one — ergonomic for FastAPI apps. Verify fit for complex queries.
- **source:** https://github.com/fastapi/sqlmodel
- **reputation:** **18,116★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** Python + FastAPI
- **adapt:** fork your models; drop to SQLAlchemy when needed.
