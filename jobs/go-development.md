# Job: Go Development

**You're about to:** write idiomatic, production-grade Go — project layout, style, library
choices. Well-served by community-proven sources (no single official "how to structure Go"
exists, which is itself worth knowing).

> Reputation pulled live **2026-06-02** via `gh api`.

---

## Tier A 🟢 — Canonical

### Effective Go + the standard library docs
The official idiom guide and API reference. Always start here for "what's the Go way."
- **source:** https://go.dev/doc/effective_go (pkg docs: https://pkg.go.dev/std)
- **reputation:** Official Go team
- **last_validated:** 2026-06-02
- **assumes:** Go installed
- **adapt:** none — reference.

---

## Tier B 🔵 — Community-proven (high rep + maintained)

### Uber Go Style Guide
The most widely-adopted production Go style guide. Concrete, opinionated, battle-tested.
- **source:** https://github.com/uber-go/guide
- **reputation:** **17,548★** · pushed 2026-04-15 (high stars + maintained)
- **last_validated:** 2026-06-02
- **assumes:** intermediate Go
- **adapt:** fork the rules your team actually enforces into a private review checklist.

### awesome-go
The canonical curated index of Go libraries and tools — check before adding a dependency.
- **source:** https://github.com/avelino/awesome-go
- **reputation:** **174,343★** · pushed 2026-05-30
- **last_validated:** 2026-06-02
- **assumes:** nothing — it's an index
- **adapt:** none.

### golang-standards/project-layout
A widely-referenced project structure template. **Caveat:** popular but *not* official,
and parts of the Go community actively dispute it for smaller projects.
- **source:** https://github.com/golang-standards/project-layout
- **reputation:** **56,053★** · pushed 2026-04-28 — high stars, BUT name implies an
  official standard it isn't. Read the criticism before adopting wholesale.
- **last_validated:** 2026-06-02
- **assumes:** Go module project
- **adapt:** take the `cmd/` `internal/` `pkg/` split if it fits; ignore the rest for small services.
