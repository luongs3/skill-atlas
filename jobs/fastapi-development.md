# Job: FastAPI Development

**You're about to:** build an async Python API — type-hinted routes, Pydantic models, auto OpenAPI docs.
All canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### FastAPI + official docs
The framework itself and the official docs (tutorial, dependency injection, security, async guide).
- **source:** https://github.com/fastapi/fastapi (docs: https://fastapi.tiangolo.com/)
- **reputation:** The FastAPI project · **98,903★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Python installed
- **adapt:** none — reference.

### FastAPI docs — advanced & deployment
The official advanced guide: dependencies, background tasks, middleware, deployment patterns.
- **source:** https://fastapi.tiangolo.com/advanced/
- **reputation:** Official FastAPI documentation
- **last_validated:** 2026-06-04
- **assumes:** FastAPI app scaffolded
- **adapt:** fork your router layout, dependency wiring, and settings management.

---

## Tier B 🔵 — Community-proven

### Pydantic
The data-validation layer FastAPI is built on — models, validators, settings management.
- **source:** https://github.com/pydantic/pydantic (docs: https://docs.pydantic.dev/)
- **reputation:** Official Pydantic · very high stars · actively maintained
- **last_validated:** 2026-06-04
- **assumes:** Python project
- **adapt:** fork your shared base-model config + validation conventions.

### Starlette
The ASGI toolkit FastAPI runs on — routing, middleware, websockets, background tasks.
- **source:** https://github.com/encode/starlette (docs: https://www.starlette.io/)
- **reputation:** Encode · high stars · actively maintained
- **last_validated:** 2026-06-04
- **assumes:** ASGI server (uvicorn) installed
- **adapt:** fork your middleware stack + lifespan conventions.

---

*Substitution-resistant private skill: your project's router layout, auth/dependency-injection flow,
and error-handling conventions. An LLM writes FastAPI routes fine; it doesn't know your repo's rules.*
