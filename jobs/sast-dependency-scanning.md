# Job: SAST & Dependency Scanning

**You're about to:** catch vulnerabilities in code + dependencies in CI — static analysis, SCA, secret detection.

> Reputation pulled live **2026-06-19** via `gh api`.

Broad practice in [security](security.md); container side in [container-image-scanning](container-image-scanning.md).

---

## Tier A 🟢 — Canonical

### Semgrep
Fast, rule-based static analysis across many languages — write custom rules in CI. The pragmatic SAST default.
- **source:** https://github.com/semgrep/semgrep
- **reputation:** **15,561★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** CI
- **adapt:** fork your ruleset + per-repo ignores.

### Trivy
All-in-one scanner — deps, containers, IaC, secrets. The one tool most pipelines start with.
- **source:** https://github.com/aquasecurity/trivy
- **reputation:** **36,496★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** CI/CD
- **adapt:** fork your severity gates + ignore policy.

### Gitleaks
Detect hardcoded secrets in git history + pre-commit — stop credential leaks before push.
- **source:** https://github.com/gitleaks/gitleaks
- **reputation:** **27,777★** · pushed 2026-06-13
- **last_validated:** 2026-06-19
- **assumes:** git + CI
- **adapt:** fork your rules; add as a pre-commit hook.
