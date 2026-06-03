# Job: Go Backend Libraries (frameworks & tooling)

**You're about to:** pick and wire the standard Go libraries for a backend service — HTTP
framework, CLI, logging, testing, DI. Distinct from [go-development](go-development.md)
(idiom/style); this is the library-choice layer.

> Reputation pulled live **2026-06-03** via `gh api`. All Tier B — these are de-facto
> community standards, not official Go-team libraries.

---

## Tier B 🔵 — Community-proven (de-facto standards)

### Gin — HTTP web framework
The most-used Go HTTP framework. Fast, minimal, huge ecosystem.
- **source:** https://github.com/gin-gonic/gin
- **reputation:** **88,591★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **assumes:** Go
- **adapt:** fork your middleware stack (auth, logging, recovery) as a private starter.
- **alt:** Echo (https://github.com/labstack/echo, 32,423★, 2026-05-28) — comparable, pick one.

### Cobra — CLI framework
The standard for building Go CLIs (used by kubectl, hugo, gh).
- **source:** https://github.com/spf13/cobra
- **reputation:** **44,044★** · pushed 2026-04-25
- **last_validated:** 2026-06-03
- **assumes:** Go
- **adapt:** none — reference.

### Zap — structured logging
Uber's high-performance structured logger; the production default.
- **source:** https://github.com/uber-go/zap
- **reputation:** **24,494★** · pushed 2026-04-28
- **last_validated:** 2026-06-03
- **assumes:** Go
- **adapt:** fork your logger config (fields, levels, sampling) as a private skill.

### Testify — testing toolkit
Assertions + mocks; the most common Go testing companion.
- **source:** https://github.com/stretchr/testify
- **reputation:** **26,003★** · pushed 2026-05-17
- **last_validated:** 2026-06-03
- **assumes:** Go
- **adapt:** none — reference. Pair with table-driven test patterns.

---

*Why this is its own job: an LLM will happily suggest a Go HTTP library, but it won't know
which one **your** services standardized on or your middleware conventions. The atlas names
the live, maintained standards; your private fork encodes the team's actual choices.*
