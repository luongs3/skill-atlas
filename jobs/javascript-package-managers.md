# Job: JS Package Managers

**You're about to:** manage Node deps and monorepos — npm, pnpm, yarn, workspaces.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier B 🔵 — Community-proven

### pnpm
Fast, disk-efficient package manager; the modern default, great for monorepos.
- **source:** https://github.com/pnpm/pnpm (docs: https://pnpm.io)
- **reputation:** **35,371★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** Node
- **adapt:** fork your workspace + hoisting config.

### Yarn (Berry)
Yarn v2+ with Plug'n'Play and workspaces.
- **source:** https://github.com/yarnpkg/berry (docs: https://yarnpkg.com)
- **reputation:** Official Yarn · **8,073★** · pushed 2026-06-02
- **last_validated:** 2026-06-05
- **assumes:** Node
- **adapt:** pick one manager per repo; don't mix lockfiles.

---

## How to use this job

Default to **pnpm** for new projects and any monorepo — its content-addressed store saves disk and its strict, non-flat `node_modules` catches undeclared (phantom) dependencies early. Pick **Yarn Berry** only if you specifically want Plug'n'Play or are already invested in the Yarn plugin ecosystem. The decision hinges on whether your toolchain tolerates symlinks/PnP and whether catching phantom deps matters more than maximal tool compatibility; if a third-party tool chokes on either, npm's plain flat layout is the safe fallback.

## Pitfalls

- **pnpm's symlinked `node_modules` breaks tools that resolve real paths** — bundlers, some React Native setups, and anything calling `fs.realpath` can resolve a package to its store location and fail. Use `node-linker=hoisted` or `public-hoist-pattern` in `.npmrc` to work around it.
- **Yarn PnP has no `node_modules` on disk at all** — tools that shell out expecting that folder (older ESLint plugins, some test runners) break unless you enable `nodeLinker: node-modules` or install the PnP SDK shims.
- **Mixing managers leaves stale lockfiles** — committing both `package-lock.json` and `pnpm-lock.yaml` means CI may install a different tree than you tested. Pick one per repo and delete the others.

---

*See [typescript-javascript](typescript-javascript.md). Private skill = your monorepo structure + which manager and why.*
