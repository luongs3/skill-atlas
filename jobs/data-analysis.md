# Job: Data Analysis

**You're about to:** explore, clean, transform, or visualize data with an agent. Mix of an
official Tier-A skill, canonical tool docs, and high-rep learning repos.

> Reputation signals pulled live **2026-06-02**.

---

## Tier A 🟢 — Canonical

### xlsx (official Anthropic skill)
For spreadsheet-shaped data, the official skill handles read/write/formulas directly.
- **source:** https://github.com/anthropics/skills/tree/main/skills/xlsx
- **reputation:** Official Anthropic · in the 145k★ skills repo
- **last_validated:** 2026-06-02 (path confirmed)
- **assumes:** Claude Code
- **adapt:** none for general use.

### pandas official docs
The canonical reference for the dominant Python data library. Authoritative, always current.
- **source:** https://pandas.pydata.org/docs/
- **reputation:** Official pandas project docs
- **last_validated:** 2026-06-02 (HTTP 200)
- **assumes:** Python + pandas
- **adapt:** none — reference.

---

## Tier B 🔵 — Community-proven

### Python for Data Analysis (Wes McKinney) — notebooks
The companion notebooks to the standard pandas book, by pandas' creator. Trust by authorship.
- **source:** https://github.com/wesm/pydata-book
- **reputation:** Authored by the creator of pandas; **24,612★** · pushed 2025-10-17 (standard reference; >6mo since push → verify against current pandas)
- **last_validated:** 2026-06-02
- **assumes:** Python, Jupyter
- **adapt:** none — learning material.

### awesome-datascience
Actively-maintained curated index of data-science resources, tools, and datasets.
- **source:** https://github.com/academic/awesome-datascience
- **reputation:** **29,319★** · pushed 2026-06-01 (high stars + very recent)
- **last_validated:** 2026-06-02
- **assumes:** nothing — it's an index
- **adapt:** none.

---

## Tier C 🟡 — Useful but aging

### data-science-ipython-notebooks
Big collection of DS/ML notebooks (pandas, scikit-learn, TensorFlow).
- **source:** https://github.com/donnemartin/data-science-ipython-notebooks
- **reputation:** **29,142★** — BUT pushed **2024-03-20** (>12mo → aging; library APIs may have drifted)
- **last_validated:** 2026-06-02
- **assumes:** Python, Jupyter
- **adapt:** use the pandas/EDA notebooks; treat the deep-learning ones as version-stale.

---

## Tier C 🟡 — Modern engines worth knowing (verify fit)

For larger-than-memory or faster analysis, **Polars** and **DuckDB** are the modern picks
(both verified 2026-06-02, actively maintained):
- Polars → https://github.com/pola-rs/polars · **38,645★** · pushed 2026-06-01
- DuckDB → https://github.com/duckdb/duckdb · **38,552★** · pushed 2026-06-02

*adapt:* swap into your workflow when pandas hits a memory/perf wall.
