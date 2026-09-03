# Job: Data Visualization

**You're about to:** build charts and dashboards from data — Python plotting and JS viz.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier B 🔵 — Community-proven

### Plotly
Interactive charts for Python (and JS); good for dashboards + notebooks.
- **source:** https://github.com/plotly/plotly.py (docs: https://plotly.com/python)
- **reputation:** **18,576★** · pushed 2026-06-03
- **last_validated:** 2026-06-05
- **assumes:** Python
- **adapt:** fork your chart-theme defaults.

### D3.js
The foundational JS library for custom, bespoke data visualizations.
- **source:** https://github.com/d3/d3 (docs: https://d3js.org)
- **reputation:** **113,005★** · pushed 2026-05-28
- **last_validated:** 2026-06-05
- **assumes:** JS + SVG knowledge
- **adapt:** use for fully custom viz; reach for a higher-level lib otherwise.

---

## How to use this job

Default to **Plotly** for anything interactive in Python notebooks or dashboards — it gives you hover, zoom, and export with almost no code, and Plotly Express covers the common chart types in one line. Drop to **D3.js** only when the visual you need doesn't exist as a chart type: custom layouts, bespoke geometry, animated transitions bound to data. The decision hinges on whether you're choosing from known chart forms (high-level lib) or inventing one (D3).

## Pitfalls

- **D3 is a low-level toolkit, not a chart library:** it gives you scales, selections, and SVG/Canvas primitives — you assemble axes, legends, and tooltips yourself. Reaching for D3 to make a bar chart is days of work a high-level lib does in minutes.
- **Plotly figure bloat:** embedding many interactive Plotly figures (or large datasets) inflates HTML/notebook size into the megabytes and can freeze the browser; downsample or use WebGL traces (`scattergl`) for big point counts.
- **SVG vs Canvas scaling:** SVG-based viz (default D3/Plotly) degrades past a few thousand DOM nodes; switch to Canvas/WebGL rendering before the chart, not after it stutters.

---

## Tier C 🟡 — Useful, verify

### larashero3-dotcom/lieflat-charts
Data visualization Skill for AI Agents, turning data into polished, interactive HTML charts. 面向 AI Agents 的数据可视化 Skill，将数据快速生成精致、可交互的 HTML 图
- **source:** https://github.com/larashero3-dotcom/lieflat-charts
- **reputation:** 3,751★ · pushed 2026-08-19 (auto-added 2026-09-03 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-09-03
- **assumes:** HTML toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

*See [data-analysis](data-analysis.md). For most charts an LLM + a high-level lib suffices; D3 is for the bespoke 5%. Private skill = your house chart style.*
