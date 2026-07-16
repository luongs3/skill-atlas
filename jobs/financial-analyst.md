# Job: Financial Analyst

**You're about to:** build financial models, pull market/fundamentals data, and produce analysis/reports with an agent.

> Reputation pulled live **2026-07-16** via `gh api`.

**Pair with task jobs:** [quant-finance](quant-finance.md) (backtesting: yfinance, Qlib) · [office-documents](office-documents.md) (xlsx skill — models live in Excel) · [data-analysis](data-analysis.md) · [data-visualization](data-visualization.md).

---

## Tier B 🔵 — Community-proven

### OpenBB
The leading open-source investment-research platform — equities, macro, options, crypto data behind one Python/CLI interface. The closest thing to an open Bloomberg for agents.
- **source:** https://github.com/OpenBB-finance/OpenBB
- **reputation:** **70,667★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Python; API keys for premium sources
- **adapt:** fork your data-source config + report templates.

### FinanceDatabase
300k+ symbols (equities, ETFs, funds, indices, currencies) with sector/industry metadata — the universe-selection layer before analysis.
- **source:** https://github.com/JerBouma/FinanceDatabase
- **reputation:** **8,139★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Python
- **adapt:** none; filter to your coverage universe.

### FinanceToolkit
100+ financial ratios, indicators and performance measurements, transparently computed from fundamentals — ratio analysis an agent can actually show its work on.
- **source:** https://github.com/JerBouma/FinanceToolkit
- **reputation:** **5,114★** · pushed 2026-07-14
- **last_validated:** 2026-07-16
- **assumes:** Python; FMP API key for full data
- **adapt:** fork the ratio set your shop reports on.

### yfinance
Practical Yahoo Finance market data — fine for research/prototyping, not a licensed feed (also listed in quant-finance).
- **source:** https://github.com/ranaroussi/yfinance
- **reputation:** **24,723★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Python
- **adapt:** don't depend on it for production/compliance work.

---

**Honest gap:** no public skill encodes YOUR house modeling standards (DCF assumptions, comp sets, format conventions). Private-fork the xlsx skill with your model templates.
