# Job: Angular Development

**You're about to:** build Angular apps — components, signals, dependency injection, RxJS, the CLI.
For a broader multi-framework overview see [frontend-frameworks](frontend-frameworks.md).

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### Angular + official docs
The framework and the official docs — the source of truth for standalone components, signals, the
injector hierarchy, reactive/template-driven forms, the router, and the `ng` CLI.
- **source:** https://github.com/angular/angular (docs: https://angular.dev)
- **reputation:** Google · **100,179★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Node + the Angular CLI (`@angular/cli`); TypeScript throughout
- **adapt:** none — reference. Prefer the modern signals + standalone-component APIs in angular.dev over
  older NgModule / `*.module.ts` tutorials still floating around the web — they're stale.

---

## Tier B 🔵 — Community-proven

*Angular is a batteries-included framework — routing, forms, HTTP, animations, testing, and build
tooling all ship first-party from the team above, so there's no community substitute to list at this
tier. Reach for the official docs first. RxJS (rxjs/rxjs) underpins Angular's async APIs and is worth
reading directly. Verify any third-party library — state managers, component kits, Nx tooling —
yourself for maintenance and license before adopting them.*

---

*Substitution-resistant private skill: your workspace's module/standalone boundaries, your RxJS vs
signals conventions, your DI provider layout, your forms strategy, and your Nx/monorepo or library
structure. An LLM writes Angular components fine; it doesn't know your project's architecture or your
team's style deltas.*
