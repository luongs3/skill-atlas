# Job: LLM Observability & Evals

**You're about to:** trace, debug, and evaluate LLM apps — token/latency/cost tracking, prompt + output eval.

> Reputation pulled live **2026-06-19** via `gh api`.

App side in [llm-app-development](llm-app-development.md); RAG eval in [rag-retrieval](rag-retrieval.md).

---

## Tier A 🟢 — Canonical

### Langfuse
Open-source LLM tracing, prompt management, and evals — self-hostable. The observability layer for agents.
- **source:** https://github.com/langfuse/langfuse
- **reputation:** **29,372★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** an LLM app
- **adapt:** fork your trace instrumentation + eval datasets.

---

## Tier B 🔵 — Community-proven

### Phoenix (Arize)
OSS LLM/ML observability + evals with OTel tracing — strong for RAG debugging.
- **source:** https://github.com/Arize-ai/phoenix
- **reputation:** **10,193★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** fork your eval suite + tracing setup.

### DeepEval
Pytest-style LLM eval framework — assertion-based metrics for CI. Treat prompts like code under test.
- **source:** https://github.com/confident-ai/deepeval
- **reputation:** **16,308★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** fork your metric set + test cases.
