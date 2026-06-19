# Job: Vector Databases — Semantic Search

**You're about to:** store and query embeddings for semantic search and RAG — ANN indexes, filtering, hybrid search.

> Reputation pulled live **2026-06-19** via `gh api`.

The retrieval side of [rag-retrieval](rag-retrieval.md).

---

## Tier A 🟢 — Canonical

### Qdrant
Rust vector DB with strong filtering and payload support — fast, easy to self-host. A top RAG default.
- **source:** https://github.com/qdrant/qdrant
- **reputation:** **32,457★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** embeddings to store
- **adapt:** fork your collection schema + distance metric.

### Milvus
Scalable vector database built for billion-scale ANN — multiple index types, cloud-native. Pick at scale.
- **source:** https://github.com/milvus-io/milvus
- **reputation:** **44,845★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** embeddings + infra
- **adapt:** fork your index choice + sharding.

---

## Tier B 🔵 — Community-proven

### Weaviate
Vector DB with built-in hybrid search and module ecosystem — schema-first, GraphQL API.
- **source:** https://github.com/weaviate/weaviate
- **reputation:** **16,350★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** embeddings
- **adapt:** fork your class schema + vectorizer config.

### Chroma
Embedded/lightweight vector store — the fastest path to a local RAG prototype. Verify scale fit.
- **source:** https://github.com/chroma-core/chroma
- **reputation:** **28,486★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** fine for prototypes; reassess for prod scale.
