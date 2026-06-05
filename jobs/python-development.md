# Job: Python Development

**You're about to:** write Python — idiomatic code, packaging, the standard toolchain.
All canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### CPython + official docs
The reference implementation and the official docs (tutorial, library reference, language ref).
- **source:** https://github.com/python/cpython (docs: https://docs.python.org/3/)
- **reputation:** The Python project · **72,979★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Python installed
- **adapt:** none — reference.

### PEP 8 + the style/idiom guides
The official style guide; the baseline every Python codebase references.
- **source:** https://peps.python.org/pep-0008/
- **reputation:** Official Python Enhancement Proposal
- **last_validated:** 2026-06-04
- **assumes:** nothing
- **adapt:** fork your team's deltas from PEP 8 (line length, import order) into a private lint config.

---

## Tier B 🔵 — Community-proven (modern toolchain)

### Ruff — linter + formatter
The fast, now-standard Python linter/formatter (replaces flake8 + black + isort for most teams).
- **source:** https://github.com/astral-sh/ruff (docs: https://docs.astral.sh/ruff/)
- **reputation:** Official Astral · very high stars + actively maintained
- **last_validated:** 2026-06-04
- **assumes:** Python project
- **adapt:** fork your `ruff.toml` rule selection.

### awesome-python
The canonical curated index of Python libraries — check before adding a dependency.
- **source:** https://github.com/vinta/awesome-python
- **reputation:** **301,000★** · maintained (see [learning-resources](learning-resources.md))
- **last_validated:** 2026-06-04
- **assumes:** nothing
- **adapt:** none.

---

*Substitution-resistant private skill: your project's packaging + venv conventions (uv/poetry/pip,
src-layout, your CI's lint/type gates). An LLM writes Python fine; it doesn't know your repo's rules.*
