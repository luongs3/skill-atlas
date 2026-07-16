# Job: Journalist / Newsroom

**You're about to:** investigate documents, analyze data, track sources, and publish with an agent.

> Reputation pulled live **2026-07-16** via `gh api`.

**Pair with task jobs:** [data-analysis](data-analysis.md) · [csv-data-wrangling](csv-data-wrangling.md) · [web-scraping](web-scraping.md) (public records) · [office-documents](office-documents.md) (FOIA PDFs).

---

## Tier B 🔵 — Community-proven

### Datasette
Simon Willison's tool for exploring + publishing data — built BY a data journalist FOR the 'here's a CSV of public records, find the story' job. Instant queryable API over any dataset.
- **source:** https://github.com/simonw/datasette
- **reputation:** **11,282★** · pushed 2026-07-14
- **last_validated:** 2026-07-16
- **assumes:** Python
- **adapt:** fork your publishing/redaction defaults.

### Aleph (OCCRP)
OCCRP's investigative-data platform — entity extraction + cross-referencing across leaks, corporate registries, sanctions lists. The follow-the-money engine.
- **source:** https://github.com/alephdata/aleph
- **reputation:** **2,398★** · pushed 2026-02-20
- **last_validated:** 2026-07-16
- **assumes:** Docker; serious for big investigations
- **adapt:** usually use OCCRP's hosted Aleph.

### DocumentCloud
The newsroom standard for hosting, OCRing, annotating, and publishing source documents (MuckRock/FOIA ecosystem).
- **source:** https://github.com/MuckRock/documentcloud
- **reputation:** **49★** · pushed 2026-07-14
- **last_validated:** 2026-07-16
- **assumes:** hosted documentcloud.org
- **adapt:** none; use the API for upload/search.

### OpenRefine
Messy-data cleanup with clustering/reconciliation — the classic 'standardize 40 spellings of the same donor name' tool.
- **source:** https://github.com/OpenRefine/OpenRefine
- **reputation:** **11,909★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Java desktop/web app
- **adapt:** none.

---

**Honest gap:** source protection and editorial judgment are not skills to download. Verification workflows (chain of custody, two-source rules) are your newsroom's private fork.
