# Job: Frontend Frameworks

**You're about to:** build a UI with a modern JS framework, or pick one. All canonical
official sources, all very high reputation and actively maintained.

> Reputation pulled live **2026-06-03** via `gh api`. See also
> [web-frontend](web-frontend.md) for design + agent skills.

---

## Tier A 🟢 — Canonical (official framework sources)

### React
The most-used UI library — official source + docs.
- **source:** https://github.com/facebook/react (docs: https://react.dev)
- **reputation:** Official Meta · **245,444★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **assumes:** JS/TS toolchain
- **adapt:** none — reference.

### Next.js
The dominant React framework (SSR, routing, full-stack).
- **source:** https://github.com/vercel/next.js (docs: https://nextjs.org/docs)
- **reputation:** Official Vercel · **139,657★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** React knowledge
- **adapt:** fork your app-router conventions.

### Vue
- **source:** https://github.com/vuejs/core (docs: https://vuejs.org)
- **reputation:** Official Vue · **53,755★** · pushed 2026-06-03
- **last_validated:** 2026-06-03

### Svelte
- **source:** https://github.com/sveltejs/svelte (docs: https://svelte.dev)
- **reputation:** Official Svelte · **86,678★** · pushed 2026-06-03
- **last_validated:** 2026-06-03

### Tailwind CSS
The utility-first CSS framework most paired with the above.
- **source:** https://github.com/tailwindlabs/tailwindcss (docs: https://tailwindcss.com/docs)
- **reputation:** Official Tailwind Labs · **95,213★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **adapt:** fork your design tokens / theme config.

---

## How to pick (for a backend eng who needs a frontend)

If you just need a UI for a tool: **React + Tailwind** (or Next.js if you need SSR/routing)
is the safe, best-documented default — and it's what Anthropic's official `frontend-design`
skill ([see web-frontend](web-frontend.md)) generates well. Don't agonize over the framework
war for an internal tool; pick the one with the most training data (React) and move on.
