# Job: API Contract Testing

**You're about to:** verify services agree on their API contract so a provider change can't silently break consumers.

> Reputation pulled live **2026-06-19** via `gh api`.

Schema-first design in [api-design](api-design.md).

---

## Tier A 🟢 — Canonical

### Pact
Consumer-driven contract testing — consumers define expectations, providers verify. The category standard.
- **source:** https://github.com/pact-foundation/pact-specification
- **reputation:** **314★** · pushed 2024-04-11
- **last_validated:** 2026-06-19
- **assumes:** two services + CI
- **adapt:** fork your pacts + broker setup.

---

## Tier B 🔵 — Community-proven

### Schemathesis
Property-based testing driven by your OpenAPI/GraphQL schema — auto-finds spec violations.
- **source:** https://github.com/schemathesis/schemathesis
- **reputation:** **3,391★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** an OpenAPI/GraphQL spec
- **adapt:** fork your check selection + CI step.
