# Job: Vue & Svelte Development

**You're about to:** build apps in Vue or Svelte — reactivity, components, stores, SSR.
For a multi-framework overview see [frontend-frameworks](frontend-frameworks.md).

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### Vue (core) + official docs
The framework and official docs — Composition API, reactivity, SFCs, the `<script setup>` syntax.
- **source:** https://github.com/vuejs/core (docs: https://vuejs.org)
- **reputation:** Vue.js · **53,768★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Node + a bundler
- **adapt:** none — reference. Prefer Composition API + `<script setup>` over older Options-API tutorials.

### Svelte + official docs
The compiler-based framework and docs — runes, reactivity, stores, SvelteKit conventions.
- **source:** https://github.com/sveltejs/svelte (docs: https://svelte.dev)
- **reputation:** Svelte · **86,697★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Node + a bundler
- **adapt:** none — reference. Use the runes ($state/$derived) docs; pre-runes tutorials are stale.

---

## Tier B 🔵 — Community-proven

### SolidJS
Fine-grained reactive framework with a React-like API — useful when you want signals without a VDOM.
- **source:** https://github.com/solidjs/solid (docs: https://solidjs.com)
- **reputation:** SolidJS · **35,569★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** Node + a bundler
- **adapt:** fork your reactive store + routing conventions.

---

*Substitution-resistant private skill: which framework your app actually uses, your store/state
conventions, and your component-library contracts. An LLM writes Vue/Svelte fine; it doesn't know
which one you picked or how your repo is laid out.*
