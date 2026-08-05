# Job: RAG — Retrieval-Augmented Generation

**You're about to:** ground an LLM in your documents — chunking, embeddings, retrieval, reranking, evaluation.

> Reputation pulled live **2026-06-19** via `gh api`.

Storage in [vector-databases](vector-databases.md); app glue in [llm-app-development](llm-app-development.md).

---

## Tier A 🟢 — Canonical

### LlamaIndex
The data framework for RAG — loaders, indexes, retrievers, query engines. Docs define the ingestion-to-query pipeline.
- **source:** https://github.com/run-llama/llama_index
- **reputation:** **50,223★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** Python + an LLM
- **adapt:** fork your ingestion + retrieval strategy; don't ship defaults.

---

## Tier B 🔵 — Community-proven

### Ragas
Evaluation for RAG — faithfulness, answer/context relevance metrics. The missing measurement layer.
- **source:** https://github.com/explodinggradients/ragas
- **reputation:** **14,433★** · pushed 2026-02-24
- **last_validated:** 2026-06-19
- **assumes:** Python + eval set
- **adapt:** fork your metric suite + golden set.

### BGE / FlagEmbedding
Top open embedding + reranker models (BGE) with usage code. The retrieval-quality lever most teams skip.
- **source:** https://github.com/FlagOpen/FlagEmbedding
- **reputation:** **11,842★** · pushed 2026-04-22
- **last_validated:** 2026-06-19
- **assumes:** Python + GPU helps
- **adapt:** pick model by your language + latency budget.

---

## Tier C 🟡 — Useful, verify

### infiniflow/ragflow
RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a
- **source:** https://github.com/infiniflow/ragflow
- **reputation:** 86,737★ · pushed 2026-08-03 (auto-added 2026-08-04 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-04
- **assumes:** Go toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### VectifyAI/PageIndex
📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG
- **source:** https://github.com/VectifyAI/PageIndex
- **reputation:** 35,019★ · pushed 2026-08-04 (auto-added 2026-08-05 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-05
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.
