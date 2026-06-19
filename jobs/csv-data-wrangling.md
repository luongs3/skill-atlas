# Job: CLI Data Wrangling — CSV/JSON

**You're about to:** slice, filter, and transform CSV/JSON from the shell — fast, scriptable, no notebook needed.

> Reputation pulled live **2026-06-19** via `gh api`.

In-memory analysis in [dataframes-polars-duckdb](dataframes-polars-duckdb.md).

---

## Tier A 🟢 — Canonical

### jq
The standard JSON processor for the shell — filter, map, reshape. Indispensable in pipelines + CI.
- **source:** https://github.com/jqlang/jq
- **reputation:** **34,939★** · pushed 2026-06-17
- **last_validated:** 2026-06-19
- **assumes:** a shell
- **adapt:** learn the filter language; keep snippets.

---

## Tier B 🔵 — Community-proven

### xsv
Fast CSV toolkit in Rust — slice/select/join/stats on huge files. Verify maintenance vs forks.
- **source:** https://github.com/BurntSushi/xsv
- **reputation:** **10,751★** · pushed 2025-04-24 · ⚠️ ARCHIVED
- **last_validated:** 2026-06-19
- **assumes:** a shell
- **adapt:** keep your common subcommands handy.

### Miller (mlr)
Like awk/sed/cut for CSV/TSV/JSON — named-field processing. Great for tabular ETL in the shell.
- **source:** https://github.com/johnkerl/miller
- **reputation:** **9,917★** · pushed 2026-06-17
- **last_validated:** 2026-06-19
- **assumes:** a shell
- **adapt:** fork your verb chains.
