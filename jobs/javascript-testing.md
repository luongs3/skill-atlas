# Job: JavaScript / TS Testing

**You're about to:** write unit + integration tests for JS/TS — runners, assertions, mocks.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier B 🔵 — Community-proven

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

## How to use this job

Default to **Vitest** for new Vite/TS projects: it shares Vite's transform pipeline (so ESM, TS, and path aliases just work), runs fast with native watch mode, and its API is Jest-compatible. Stay on **Jest** when you inherit an existing Jest suite or a React Native / Babel-heavy stack where its ecosystem and `jest-*` tooling are entrenched — migration cost, not capability, drives the choice. Pick one per project; don't run both runners side by side.

## Pitfalls

- **ESM vs CommonJS mocking pain:** Jest's `jest.mock` hoisting and CommonJS roots make mocking pure-ESM packages awkward; Vitest handles ESM natively but `vi.mock` has its own hoisting rules. Mixing module systems is the usual source of "mock not applied" surprises.
- **Fake timers and async leaks:** `vi.useFakeTimers()`/`jest.useFakeTimers()` not paired with restore, or unawaited promises/timers, leak state between tests and cause flaky, order-dependent failures. Always reset mocks/timers in `afterEach`.
- **Config and transform drift:** TS path aliases, JSX, and coverage settings must be configured in the test runner separately from your build — tests passing locally but failing in CI is usually a transform/environment (`jsdom` vs `node`) mismatch.

---

*An LLM writes a test fine; it won't know your codebase's fixtures, mocking conventions, or which flows get E2E vs unit. Encode those in a private skill. See [e2e-browser-testing](e2e-browser-testing.md).*
