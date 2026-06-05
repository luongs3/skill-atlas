# Job: Python Packaging & Environments

**You're about to:** manage Python deps, virtualenvs, and builds — the modern fast toolchain.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### uv
The fast all-in-one Python package + project + env manager (replaces pip/poetry/pyenv for most).
- **source:** https://github.com/astral-sh/uv (docs: https://docs.astral.sh/uv)
- **reputation:** Official Astral · **85,991★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** Python
- **adapt:** fork your pyproject + lockfile conventions.

---

## How to use this job

Reach for **uv** as the default for new Python projects — it replaces pip, pip-tools, virtualenv, pyenv, and most of poetry with one fast Rust binary, and it manages Python interpreter versions too. Use `uv sync` against a committed `uv.lock` for reproducible installs, `uv run` to execute inside the project env without manual activation, and `uv pip` as a drop-in when you just need pip semantics. The decision to switch hinges mostly on whether your team tolerates a young (pre-1.0) tool; the speed and lockfile story are already worth it for most.

## Pitfalls

- **The lockfile is platform/marker-aware but not magic.** `uv.lock` resolves for your declared platforms; a dependency with native wheels missing for a target (e.g. an ARM/musl box) still fails at install time. Test installs on every platform you ship to, and commit the lockfile.
- **uv-managed Python ≠ system Python.** uv can download its own interpreters; tools or scripts expecting the system `python3` may pick the wrong one, and global `pip install` outside uv pollutes nothing useful. Standardize on `uv run`/`uv sync` so everyone hits the same interpreter.
- **Editable installs and PEP 517 build quirks still apply.** uv is fast but doesn't fix a broken `pyproject.toml` build backend; missing build deps or a misconfigured `[build-system]` fail the same way as pip. Verify the package actually builds, not just resolves.

*See [python-development](python-development.md). Private skill = your project layout + dependency policy. uv is the current default; the file stays honest if a faster tool supersedes it.*
