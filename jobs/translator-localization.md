# Job: Translator / Localization Specialist

**You're about to:** translate documents and localize software/content with an agent — TM, terminology, formats (PO/XLIFF), QA.

> Reputation pulled live **2026-07-16** via `gh api`.

**Pair with task jobs:** [office-documents](office-documents.md) (docx/pdf round-trip) · [i18n-localization](i18n-localization.md) (the software side of the same job).

---

## Tier B 🔵 — Community-proven

### Weblate
The leading open-source continuous-localization platform — VCS-integrated, TM, glossaries, review workflow, full REST API. The professional l10n backbone.
- **source:** https://github.com/WeblateOrg/weblate
- **reputation:** **5,979★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Docker or hosted weblate.org
- **adapt:** fork your glossary + QA checks per client.

### LibreTranslate
Self-hosted MT API (Argos models) — draft translations without sending client text to a third party. Quality below DeepL/GPT; fine for drafts + privacy.
- **source:** https://github.com/LibreTranslate/LibreTranslate
- **reputation:** **15,449★** · pushed 2026-07-13
- **last_validated:** 2026-07-16
- **assumes:** Python/Docker
- **adapt:** none; treat output as first-pass only.

### translate (Translate Toolkit)
The format-conversion workhorse — PO/XLIFF/TMX/properties converters + QA checks (pofilter). The plumbing every l10n pipeline needs.
- **source:** https://github.com/translate/translate
- **reputation:** **962★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Python CLI
- **adapt:** fork your QA-check config.

---

## Tier C 🟡 — Useful, verify

### OmegaT
The veteran desktop CAT tool — TM, glossaries, many formats. Works, but desktop-centric and quieter; verify your format needs.
- **source:** https://github.com/omegat-org/omegat
- **reputation:** **522★** · pushed 2026-07-16
- **last_validated:** 2026-07-16
- **assumes:** Java desktop app
- **adapt:** use for solo CAT work; Weblate for team/continuous.

---

**Honest gap:** translation JUDGMENT (register, domain terminology, client style guides) is the private fork — a per-client glossary + style skill on top of MT drafts. LLM translation beats the OSS MT models above; the OSS value is the workflow/format layer, not the MT itself.
