# Job: Monorepo Tooling

**You're about to:** manage a monorepo — task running, caching, builds with Nx or Turborepo.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Turborepo
High-performance build system for JS/TS monorepos — caching, task pipelines.
- **source:** https://github.com/vercel/turborepo (docs: https://turborepo.com/docs)
- **reputation:** Official Vercel · **30,494★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a JS monorepo
- **adapt:** fork your pipeline + caching config.

### Nx
Powerful monorepo tooling with generators, graph analysis, and plugins.
- **source:** https://github.com/nrwl/nx (docs: https://nx.dev)
- **reputation:** **28,810★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** a monorepo
- **adapt:** Nx for heavy/structured; Turborepo for lighter setups.

---

## How to use this job

Choose **Turborepo** when you want fast remote-cached task pipelines with minimal config bolted onto your existing repo structure — it does one thing (orchestrate + cache tasks) well. Choose **Nx** when you want an opinionated, structured workspace: code generators, an enforced module-boundary graph, and a plugin ecosystem for framework integrations. The decision hinges on how much structure you want imposed: Turborepo stays out of your way, Nx actively shapes the repo.

## Pitfalls

- **Cache false-positives from incomplete input hashing** — if a task depends on an env var, a global config, or a file outside the declared `inputs`, the tool serves a stale cached result. Audit `inputs`/`outputs` (Turbo) or `namedInputs` (Nx) so the hash actually captures every dependency.
- **Task-graph cycles deadlock the build** — declaring package A's build to depend on B while B depends on A (often via test/build cross-deps) causes the runner to error or hang. Keep `dependsOn` acyclic and split shared code into a leaf package.
- **Caching non-deterministic outputs poisons the cache** — tasks that embed timestamps, absolute paths, or random ordering produce a "hit" that differs from a fresh run. Make builds reproducible before enabling remote cache, or you'll ship cache artifacts that don't match source.

---

*See [javascript-package-managers](javascript-package-managers.md). Private skill = your repo's task graph + caching strategy.*
