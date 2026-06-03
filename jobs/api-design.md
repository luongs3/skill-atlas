# Job: API Design (REST & gRPC)

**You're about to:** design an HTTP/REST or gRPC API — resource modeling, versioning,
error shapes, pagination. Strong canonical guideline + high-rep references.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical

### Microsoft REST API Guidelines
The most-referenced production REST guideline — naming, versioning, errors, pagination,
long-running ops. Opinionated and concrete.
- **source:** https://github.com/microsoft/api-guidelines
- **reputation:** Microsoft official · **23,278★** · pushed 2026-05-21
- **last_validated:** 2026-06-03
- **assumes:** designing an HTTP API
- **adapt:** fork the rules your org adopts into a private API-review checklist.

### gRPC-Go + official gRPC docs
For RPC/service-to-service APIs in Go — the canonical implementation and design guidance.
- **source:** https://github.com/grpc/grpc-go (docs: https://grpc.io/docs/)
- **reputation:** Official gRPC · **22,942★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **assumes:** Go, protobuf
- **adapt:** none — reference. Pair with your proto style conventions.

---

## Tier B 🔵 — Community-proven (reference / inspiration)

### public-apis
Massive index of public APIs — useful for finding integration targets or studying how
real APIs shape their endpoints.
- **source:** https://github.com/public-apis/public-apis
- **reputation:** **438,930★** · pushed 2026-06-01 (one of GitHub's most-starred, maintained)
- **last_validated:** 2026-06-03
- **assumes:** nothing — it's an index
- **adapt:** none.

---

*The substitution-resistant value here is a private skill that encodes your org's API
conventions (error envelope, auth scheme, versioning rule). The public guidelines tell you
what *good* looks like; your skill enforces what *your team* decided.*
