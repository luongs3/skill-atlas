# Job: JavaScript / TS Testing

**You're about to:** write unit + integration tests for JS/TS — runners, assertions, mocks.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Vitest
The fast, modern test runner for Vite/TS projects. Jest-compatible API.
- **source:** https://github.com/vitest-dev/vitest (docs: https://vitest.dev)
- **reputation:** **16,632★** · pushed 2026-06-04 (modern default)
- **last_validated:** 2026-06-05
- **assumes:** Node/Vite project
- **adapt:** fork your test config + coverage thresholds.

### Jest
The long-standing standard test framework, still dominant in React/Node.
- **source:** https://github.com/jestjs/jest (docs: https://jestjs.io)
- **reputation:** Official (OpenJS) · **45,361★** · pushed 2026-06-02
- **last_validated:** 2026-06-05
- **assumes:** Node project
- **adapt:** pick Vitest OR Jest per project; don't mix.

---

*An LLM writes a test fine; it won't know your codebase's fixtures, mocking conventions, or which flows get E2E vs unit. Encode those in a private skill. See [e2e-browser-testing](e2e-browser-testing.md).*
