# Job: Docker & Containers

**You're about to:** containerize an app, write a Dockerfile/compose stack, or debug a
container. Canonical engine source + a high-rep examples repo.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical

### Docker / Moby engine + official docs
The container engine source and the authoritative docs (Dockerfile reference, build, networking).
- **source:** https://github.com/moby/moby (docs: https://docs.docker.com)
- **reputation:** The Docker/Moby project · **71,625★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **assumes:** Docker installed
- **adapt:** none — reference. Build a private "slim image" skill (multi-stage, distroless, your base images).

---

## Tier B 🔵 — Community-proven

### awesome-compose
Official Docker repo of ready-to-use Compose samples for common stacks (Go+Postgres,
nginx, etc.). The fastest way to a working multi-service local setup.
- **source:** https://github.com/docker/awesome-compose
- **reputation:** **45,459★** · pushed 2026-05-29 (Docker-maintained, high stars)
- **last_validated:** 2026-06-03
- **assumes:** Docker Compose
- **adapt:** copy the sample closest to your stack, then harden (healthchecks, resource limits, secrets).

---

## How to use this job

Dockerfiles and compose files are exactly the kind of thing an LLM writes well from a
prompt — so the public value here is the *reference*, and the private value is a skill
encoding **your** conventions: base images you trust, your registry, your healthcheck and
non-root-user defaults, your multi-stage build pattern. Build that with `skill-creator`
rather than re-deriving a Dockerfile each time.
