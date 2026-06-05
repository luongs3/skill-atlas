# Job: Building Go CLIs

**You're about to:** build a polished command-line tool in Go — flags, config, TUI.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier B 🔵 — Community-proven

### Cobra + Viper
Cobra (commands/flags, used by kubectl/gh) + Viper (config). The standard Go CLI stack.
- **source:** https://github.com/spf13/cobra · https://github.com/spf13/viper
- **reputation:** Cobra 44k★ (see [go-backend-libraries]); Viper **30,282★** pushed 2026-01-12 (stable)
- **last_validated:** 2026-06-05
- **assumes:** Go
- **adapt:** fork your command structure.

### Bubble Tea
Framework for rich terminal UIs (TUIs) in Go.
- **source:** https://github.com/charmbracelet/bubbletea (docs: https://github.com/charmbracelet/bubbletea/tree/main/examples)
- **reputation:** **42,886★** · pushed 2026-06-01
- **last_validated:** 2026-06-05
- **assumes:** Go
- **adapt:** use when your CLI needs an interactive UI.

### urfave/cli
Lighter alternative to Cobra for simple CLIs.
- **source:** https://github.com/urfave/cli
- **reputation:** **24,106★** · pushed 2026-06-03
- **last_validated:** 2026-06-05
- **assumes:** Go
- **adapt:** pick Cobra (rich) or urfave (simple).

---

*See [go-development](go-development.md) and [go-backend-libraries](go-backend-libraries.md). Private skill = your CLI's command + config conventions.*
