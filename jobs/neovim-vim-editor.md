# Job: Neovim / Vim

**You're about to:** configure and use (Neo)vim — modal editing, plugins, LSP, config.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Neovim + docs
The modern, extensible Vim fork with built-in LSP and Lua config.
- **source:** https://github.com/neovim/neovim (docs: https://neovim.io/doc/)
- **reputation:** Official Neovim · **100,172★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** terminal
- **adapt:** fork your init.lua / plugin set.

### Vim
The original; still everywhere on servers.
- **source:** https://github.com/vim/vim (docs: https://vimhelp.org)
- **reputation:** Official Vim · **40,432★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** terminal
- **adapt:** learn enough to edit on any box; deep config goes in Neovim.

---

## How to use this job

Reach for **Neovim** for your daily driver: the Lua config, built-in LSP client, and Treesitter are the modern baseline, and the plugin ecosystem (lazy.nvim, telescope, nvim-cmp) assumes it. Keep just enough **Vim** muscle memory to edit on any server where Neovim isn't installed — motions and `:` commands carry over, your config does not.

## Pitfalls

- **Config breakage on update:** Neovim's Lua API and LSP defaults shift across minor versions — a working `init.lua` can break after a `nvim` upgrade, especially when plugins pin different API expectations. Pin plugin versions and read breaking-change notes.
- **LSP ≠ formatting/linting:** the built-in LSP client only speaks the LSP protocol; formatters and linters that aren't language servers need a bridge (conform.nvim, nvim-lint, or null-ls/none-ls). Beginners wire up an LSP and wonder why `:lua vim.lsp.buf.format()` does nothing.
- **Vim vs Neovim divergence:** `.vimrc` Vimscript mostly works in Neovim, but plugins, terminal handling, and defaults differ — don't assume a Vim plugin or tip applies unchanged.

---

*Editor config is intensely personal — the public sources teach the engine, the private skill is your config repo (keymaps, LSP setup, plugins). That's the whole value and it can't be public.*
