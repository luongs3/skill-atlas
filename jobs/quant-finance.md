# Job: Quantitative Finance & Backtesting

**You're about to:** research + backtest trading strategies and analyze market data with realistic assumptions.

> Reputation pulled live **2026-06-19** via `gh api`.

---

## Tier B 🔵 — Community-proven

### yfinance
Practical market-data access from Yahoo Finance — fine for research, not a licensed feed. Mind reliability/ToS.
- **source:** https://github.com/ranaroussi/yfinance
- **reputation:** **24,329★** · pushed 2026-06-17
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** fork your data layer; don't depend on it for prod trading.

### Qlib
Microsoft's AI-oriented quant research platform — data, models, backtesting. Heavier, research-grade.
- **source:** https://github.com/microsoft/qlib
- **reputation:** **44,804★** · pushed 2026-04-22
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** fork your data handler + strategy.

---

## Tier C 🟡 — Useful, verify

### Zipline
A well-known Pythonic backtester — but the original is largely unmaintained; verify a live fork before relying on it.
- **source:** https://github.com/quantopian/zipline
- **reputation:** **19,885★** · pushed 2024-02-13
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** prefer a maintained fork; model fees/slippage realistically.
