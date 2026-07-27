# Job: Recruiter / Talent Acquisition

**You're about to:** source candidates, screen resumes, and run hiring pipelines with an agent.

> Reputation pulled live **2026-07-16** via `gh api`.

**Pair with task jobs:** [office-documents](office-documents.md) (docx/pdf — resumes) · [workflow-automation-n8n](workflow-automation-n8n.md) (pipeline glue) · [web-scraping](web-scraping.md) (sourcing, mind ToS).

---

## Tier B 🔵 — Community-proven

### Reactive Resume
Popular open-source resume builder — useful on the candidate-facing side and as a rendering layer for structured resume data.
- **source:** https://github.com/AmruthPillai/Reactive-Resume
- **reputation:** **39,621★** · pushed 2026-07-09
- **last_validated:** 2026-07-16
- **assumes:** Docker/Node
- **adapt:** fork templates.

### JSON Resume
The open resume-data standard — parse resumes INTO a schema an agent can filter/rank/render, instead of regexing PDFs.
- **source:** https://github.com/jsonresume/resume-schema
- **reputation:** **2,398★** · pushed 2026-06-12 · ⚠️ ARCHIVED
- **last_validated:** 2026-07-16
- **assumes:** Node ecosystem of themes/tools
- **adapt:** fork your screening rubric over the schema.

---

## Tier D 🔴 — Caution

### OpenCATS
Open-source applicant tracking system (PHP) — now ARCHIVED upstream. Listed so you don't rediscover it's frozen; use its schema as a reference only.
- **source:** https://github.com/opencats/OpenCATS
- **reputation:** **711★** · pushed 2026-07-09
- **last_validated:** 2026-07-16
- **assumes:** PHP/MySQL
- **adapt:** probably don't; use its schema as a reference model.

---

**Honest gap:** the public layer here is THIN — no Tier-A recruiting skill exists. Sourcing (LinkedIn etc.) is ToS-constrained and can't ship as a public skill. The real asset is a private fork: your screening rubric, your outreach sequences, your interview loop — on top of the docx/pdf skills and an ATS API.
