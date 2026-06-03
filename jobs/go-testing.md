# Job: Go Testing

**You're about to:** write tests for Go code — unit, integration, mocks, or container-based
tests. Distinct from [go-backend-libraries](go-backend-libraries.md); this is the testing
toolchain specifically.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical

### Go standard `testing` + table-driven tests
The built-in testing package is the foundation — table-driven tests are the idiomatic Go
pattern, no third-party lib required.
- **source:** https://pkg.go.dev/testing (guide: https://go.dev/doc/tutorial/add-a-test)
- **reputation:** Official Go team
- **last_validated:** 2026-06-03
- **assumes:** Go
- **adapt:** none — start here before reaching for a framework.

---

## Tier B 🔵 — Community-proven (toolchain)

### Testify — assertions + mocks
The most-used testing companion: `assert`, `require`, `mock`, `suite`.
- **source:** https://github.com/stretchr/testify
- **reputation:** **26,003★** · pushed 2026-05-17
- **last_validated:** 2026-06-03
- **assumes:** Go
- **adapt:** none — reference.

### Mockery — mock generation
Generates testify-compatible mocks from interfaces.
- **source:** https://github.com/vektra/mockery
- **reputation:** **7,121★** · pushed 2026-05-01 (the maintained mock generator — see deprecated note below)
- **last_validated:** 2026-06-03
- **assumes:** Go interfaces
- **adapt:** fork your mock-gen config (which packages, output dirs).

### testcontainers-go — integration tests with real dependencies
Spin up real Postgres/Redis/Kafka in Docker for integration tests. The modern standard for
testing against real infra instead of mocks.
- **source:** https://github.com/testcontainers/testcontainers-go
- **reputation:** **4,861★** · pushed 2026-06-03 (active; lower stars because Go-specific)
- **last_validated:** 2026-06-03
- **assumes:** Go + Docker
- **adapt:** fork your container setup (which deps, fixtures).
- **alt:** ory/dockertest (4,515★, 2026-04-24) — similar, lighter.

---

## Tier D 🔴 — Deprecated (do not use)

### golang/mock (gomock — original)
- **source:** https://github.com/golang/mock
- **reputation:** 9,364★ but **archived/unmaintained (last push 2024-01-08)**. Google
  archived it; the community moved to Uber's fork (go.uber.org/mock) or mockery.
- **adapt:** if you see `github.com/golang/mock` in a codebase, migrate to `go.uber.org/mock`.

---

*The substitution-resistant value: an LLM writes a table-driven test fine, but won't know
your codebase's test conventions (fixtures, golden files, which deps get testcontainers vs
mocks). Encode those in a private `go-test-conventions` skill.*
