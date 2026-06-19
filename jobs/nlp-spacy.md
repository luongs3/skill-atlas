# Job: NLP — Classic Text Processing

**You're about to:** do production NLP without an LLM — tokenization, NER, parsing, classification, fast + cheap.

> Reputation pulled live **2026-06-19** via `gh api`.

LLM-based text work in [llm-app-development](llm-app-development.md).

---

## Tier A 🟢 — Canonical

### spaCy
Industrial-strength NLP — fast pipelines for NER, POS, parsing. The production classic-NLP default.
- **source:** https://github.com/explosion/spaCy
- **reputation:** **33,669★** · pushed 2026-05-19
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** fork your pipeline + custom components/models.

### Transformers
The model hub library — load + fine-tune thousands of NLP/vision/audio models. The ecosystem backbone.
- **source:** https://github.com/huggingface/transformers
- **reputation:** **161,719★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Python + (GPU helps)
- **adapt:** pick a task-specific model; fork your inference.
