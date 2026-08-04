# Job: React Development

**You're about to:** build React apps — hooks, state, component patterns, SSR.
For a multi-framework overview see [frontend-frameworks](frontend-frameworks.md); this one goes React-deep.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### React + official docs
The library and the official docs — the source of truth for hooks, effects, refs, and the rules of React.
- **source:** https://github.com/facebook/react (docs: https://react.dev)
- **reputation:** Meta · **245,444★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Node + a bundler
- **adapt:** none — reference. Read the hooks + "You Might Not Need an Effect" guides before reaching for state libs.

### Next.js
The canonical React framework — App Router, server components, data fetching, routing conventions.
- **source:** https://github.com/vercel/next.js (docs: https://nextjs.org/docs)
- **reputation:** Vercel · **139,657★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** React knowledge
- **adapt:** fork your team's rendering strategy (RSC vs client) and caching conventions.

---

## Tier B 🔵 — Community-proven

### React Router
The standard client routing library when you're not on a full framework.
- **source:** https://github.com/remix-run/react-router (docs: https://reactrouter.com)
- **reputation:** Remix · **56,442★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** a React app
- **adapt:** fork your route layout + loader/data conventions.

---

*Substitution-resistant private skill: your app's state architecture (server-state vs client-state split,
which data lib, folder conventions, your design-system component contracts). An LLM writes hooks fine;
it doesn't know how your codebase draws those boundaries.*

---

## Tier C 🟡 — Useful, verify

### nextlevelbuilder/ui-ux-pro-max-skill
An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms
- **source:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **reputation:** 94,366★ · pushed 2026-06-20 (auto-added 2026-06-21 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-21
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### FlowiseAI/Flowise
Build AI Agents, Visually
- **source:** https://github.com/FlowiseAI/Flowise
- **reputation:** 55,123★ · pushed 2026-08-03 (auto-added 2026-08-04 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-04
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.
