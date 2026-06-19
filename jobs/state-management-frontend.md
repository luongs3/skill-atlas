# Job: Frontend State Management

**You're about to:** manage client + server state in React without prop-drilling or over-engineering.

> Reputation pulled live **2026-06-19** via `gh api`.

Used inside [react-development](react-development.md)/[nextjs-fullstack](nextjs-fullstack.md).

---

## Tier A 🟢 — Canonical

### Zustand
Minimal, hook-based global state — no boilerplate, no context hell. The modern default for client state.
- **source:** https://github.com/pmndrs/zustand
- **reputation:** **58,346★** · pushed 2026-06-16
- **last_validated:** 2026-06-19
- **assumes:** React
- **adapt:** fork your store slices.

### TanStack Query
Server-state caching/sync (fetch, cache, invalidate, retry). Replaces most hand-rolled data-fetching state.
- **source:** https://github.com/TanStack/query
- **reputation:** **49,791★** · pushed 2026-06-17
- **last_validated:** 2026-06-19
- **assumes:** React/Vue/Svelte/etc.
- **adapt:** fork your query keys + cache policy.

---

## Tier B 🔵 — Community-proven

### Redux Toolkit
The opinionated, modern Redux — slices, thunks, RTK Query. Pick when you genuinely need a single audited store.
- **source:** https://github.com/reduxjs/redux-toolkit
- **reputation:** **11,212★** · pushed 2026-06-14
- **last_validated:** 2026-06-19
- **assumes:** React
- **adapt:** fork your slices; don't reach for it by default.
