# Job: Office Documents (Word / PDF / PowerPoint / Excel)

**You're about to:** create, edit, or extract from `.docx`, `.pdf`, `.pptx`, or `.xlsx`
files with an agent. This is the **strongest** job in the atlas — Anthropic ships
official Tier-A skills for every format, so you rarely need anything else.

> Reputation signals pulled live **2026-06-02**.

---

## Tier A 🟢 — Canonical (official Anthropic skills)

All four live in `anthropics/skills/skills/` (145,275★, pushed 2026-05-29, verified
2026-06-02). Trust by authorship — Anthropic wrote and maintains them.

### docx — Word documents
- **source:** https://github.com/anthropics/skills/tree/main/skills/docx
- **reputation:** Official Anthropic · part of the 145k★ skills repo
- **last_validated:** 2026-06-02 (path confirmed via API)
- **assumes:** Claude / Claude Code skill loader
- **adapt:** none for general use; fork only if you have a fixed company template.

### pdf — PDF read/fill/extract
- **source:** https://github.com/anthropics/skills/tree/main/skills/pdf
- **reputation:** Official Anthropic
- **last_validated:** 2026-06-02
- **assumes:** Claude Code
- **adapt:** none.

### pptx — PowerPoint decks
- **source:** https://github.com/anthropics/skills/tree/main/skills/pptx
- **reputation:** Official Anthropic
- **last_validated:** 2026-06-02
- **assumes:** Claude Code
- **adapt:** fork to bake in your slide template / brand if you make decks repeatedly.

### xlsx — Excel spreadsheets
- **source:** https://github.com/anthropics/skills/tree/main/skills/xlsx
- **reputation:** Official Anthropic
- **last_validated:** 2026-06-02
- **assumes:** Claude Code
- **adapt:** none.

---

## Related official skills (same repo)

- **brand-guidelines** — apply a consistent brand across generated docs → https://github.com/anthropics/skills/tree/main/skills/brand-guidelines
- **doc-coauthoring** — collaborative long-doc writing → https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring

Both Tier A, same repo, validated 2026-06-02.

---

*Why this job has no Tier-C noise: the format skills are a solved problem with an official
source. Don't load a random community "pdf helper" when Anthropic ships one.*
