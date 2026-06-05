# Job: TypeScript & JavaScript

**You're about to:** write TS/JS — language features, types, the runtime/toolchain. All
canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### TypeScript + official handbook
The language, compiler, and the authoritative handbook.
- **source:** https://github.com/microsoft/TypeScript (docs: https://www.typescriptlang.org/docs/)
- **reputation:** Official Microsoft · **109,070★** · pushed 2026-06-02
- **last_validated:** 2026-06-04
- **assumes:** Node or a TS toolchain
- **adapt:** fork your `tsconfig` strictness conventions.

### Node.js + docs
The dominant JS runtime — official source + API docs.
- **source:** https://github.com/nodejs/node (docs: https://nodejs.org/docs/latest/api/)
- **reputation:** Official OpenJS · **117,523★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Node installed
- **adapt:** none — reference.

### MDN (the JS reference)
The canonical reference for JavaScript language + Web APIs. Not a repo — the authoritative docs.
- **source:** https://developer.mozilla.org/en-US/docs/Web/JavaScript
- **reputation:** Official Mozilla / web-standards reference
- **last_validated:** 2026-06-04
- **assumes:** nothing
- **adapt:** none — reference.

---

## Tier B 🔵 — Community-proven (modern runtimes & tooling)

### Deno / Bun (modern runtimes)
Faster, batteries-included alternatives to Node for new projects.
- **source:** https://github.com/denoland/deno (**106,941★**) · https://github.com/oven-sh/bun (**92,795★**) · both pushed 2026-06-04
- **reputation:** official, very high stars, actively maintained
- **last_validated:** 2026-06-04
- **assumes:** willingness to step off Node
- **adapt:** pick one per project; don't mix runtimes.

---

*Private skill that pays off: your project's TS strictness + lint/format config + which
runtime, encoded so a new package starts consistent. See also [frontend-frameworks](frontend-frameworks.md).*
