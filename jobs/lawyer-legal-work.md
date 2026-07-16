# Job: Lawyer / Legal Work

**You're about to:** do legal research, document drafting/review, case management, and e-discovery with an agent.

> Reputation pulled live **2026-07-16** via `gh api`.

**Pair with task jobs:** [office-documents](office-documents.md) (docx/pdf skills — contracts ARE Word/PDF files) · [pdf-generation](pdf-generation.md) · [elasticsearch-search](elasticsearch-search.md) (case-file search).

---

## Tier B 🔵 — Community-proven

### CourtListener (Free Law Project)
The Free Law Project's open legal-research platform — millions of US opinions, PACER data, judges, oral arguments, with a real REST API an agent can query.
- **source:** https://github.com/freelawproject/courtlistener
- **reputation:** **977★** · pushed 2026-07-15
- **last_validated:** 2026-07-16
- **assumes:** the courtlistener.com API (or self-host)
- **adapt:** fork your search/citation workflows; US-centric.

### docassemble
Guided-interview document automation (Python) — the standard OSS for generating legal documents from structured Q&A. Made for exactly the 'agent fills in the contract' job.
- **source:** https://github.com/jhpyle/docassemble
- **reputation:** **965★** · pushed 2026-07-14
- **last_validated:** 2026-07-16
- **assumes:** Python/Docker
- **adapt:** fork your document templates + interview logic per practice area.

### eyecite (Free Law Project)
Extracts legal citations from text — battle-tested on 55M+ documents at CourtListener. The citation-parsing primitive for any legal-text pipeline.
- **source:** https://github.com/freelawproject/eyecite
- **reputation:** **263★** · pushed 2026-07-01
- **last_validated:** 2026-07-16
- **assumes:** Python
- **adapt:** none for US citations; other jurisdictions need your own patterns.

---

## Tier D 🔴 — Caution

### LexNLP
Legal-text NLP toolkit (terms, dates, amounts, citations). Historically important but effectively unmaintained — listed so you don't rediscover that.
- **source:** https://github.com/LexPredict/lexpredict-lexnlp
- **reputation:** **791★** · pushed 2024-05-27
- **last_validated:** 2026-07-16
- **assumes:** Python (older versions)
- **adapt:** extract the regex/pattern ideas, don't depend on the package.

### Blackstone
spaCy pipeline for UK legal text. Research prototype, long dead — caution.
- **source:** https://github.com/ICLRandD/Blackstone
- **reputation:** **692★** · pushed 2024-07-16
- **last_validated:** 2026-07-16
- **assumes:** Python + old spaCy
- **adapt:** don't build on it; it marks the UK-legal-NLP gap.

---

**Honest gap:** there is **no Tier-A public 'contract review' or 'legal advice' skill**, and there shouldn't be — legal judgment is jurisdiction- and matter-specific, and the liability of a confidently-wrong skill is maximal here. The real play: private fork encoding YOUR practice's playbooks (clause library, fallback positions, review checklists) on top of the docx/pdf skills. Agent output is a draft for attorney review, never advice.
