# Job: GitHub Actions — CI/CD

**You're about to:** automate build/test/deploy in GitHub Actions — workflows, matrix builds, reusable actions, secrets.

> Reputation pulled live **2026-06-19** via `gh api`.

Broader CI in [cicd-pipelines](cicd-pipelines.md); release flow in [release-automation](release-automation.md).

---

## Tier A 🟢 — Canonical

### GitHub Actions runner
The official self-hosted runner + the source of truth for runner behavior. Read for self-hosting + scaling.
- **source:** https://github.com/actions/runner
- **reputation:** **6,086★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a GitHub repo
- **adapt:** fork your workflow YAML; pin action SHAs.

---

## Tier B 🔵 — Community-proven

### act
Run GitHub Actions locally in Docker — debug workflows without push-and-pray. Huge feedback-loop win.
- **source:** https://github.com/nektos/act
- **reputation:** **70,829★** · pushed 2026-06-01
- **last_validated:** 2026-06-19
- **assumes:** Docker
- **adapt:** use locally; mind runner-image differences.

### actions/toolkit
Official JS/TS libraries for authoring custom Actions — inputs, outputs, core/github packages.
- **source:** https://github.com/actions/toolkit
- **reputation:** **5,773★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** Node/TS
- **adapt:** fork when writing a composite/JS action.
