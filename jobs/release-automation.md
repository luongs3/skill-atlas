# Job: Release Automation & Versioning

**You're about to:** automate versioning, changelogs, and releases from commits.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### semantic-release
Fully automated version + changelog + publish from conventional commits.
- **source:** https://github.com/semantic-release/semantic-release (docs: https://semantic-release.gitbook.io)
- **reputation:** **23,742★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** CI + conventional commits
- **adapt:** fork your release config + plugins.

### Changesets
Versioning + changelogs for monorepos (per-package releases).
- **source:** https://github.com/changesets/changesets
- **reputation:** **11,937★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a monorepo
- **adapt:** Changesets for monorepos; semantic-release for single packages.

---

## How to use this job

Use **semantic-release** for a single package where you want a fully hands-off pipeline: it computes the next version from conventional commits and publishes on merge with no manual step. Use **Changesets** for monorepos where packages version independently and you want a human-reviewed intent file (the changeset) captured per PR. The decision hinges on monorepo vs single package and on whether you want releases fully automatic (semantic-release) or gated by an explicit, reviewable changelog entry (Changesets).

## Pitfalls

- **semantic-release derives everything from commit messages** — one badly typed commit (`fix` vs `feat` vs `BREAKING CHANGE:` footer) silently produces the wrong semver bump. Enforce commit format with commitlint in CI or you'll ship a patch that should have been a major.
- **semantic-release needs a clean CI token and shallow-clone fix** — it walks git tags to find the last release, so a shallow `git clone --depth 1` makes it think every release is the first. Set `fetch-depth: 0` in your checkout step.
- **Changesets won't release packages with no changeset file** — forgetting to add one means the PR merges but that package never bumps or publishes. Add the changeset bot or a CI check that fails PRs touching `src` without a changeset.

---

## Tier C 🟡 — Useful, verify

### lsdefine/GenericAgent
Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption
- **source:** https://github.com/lsdefine/GenericAgent
- **reputation:** 13,678★ · pushed 2026-08-07 (auto-added 2026-08-07 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-07
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

*See [cicd-pipelines](cicd-pipelines.md). Private skill = your release flow + versioning policy.*
