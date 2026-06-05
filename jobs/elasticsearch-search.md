# Job: Elasticsearch — Search & Analytics

**You're about to:** index and search with Elasticsearch — mappings, analyzers, the Query
DSL, aggregations, and cluster operations.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### Elasticsearch source + official docs
The reference search/analytics engine and the docs behind every relevance and scaling
decision — index mappings, analyzers + tokenizers, the Query DSL (`bool`/`match`/`term`),
aggregations, and shard/replica + cluster operations.
- **source:** https://github.com/elastic/elasticsearch (docs: https://www.elastic.co/guide/)
- **reputation:** Elastic · **76,833★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** a running Elasticsearch cluster
- **adapt:** none — reference. Mappings and DSL shift between majors — pin your version.

---

## Tier B 🔵 — Community-proven

### Relevance tuning & analyzers
The part that separates "returns results" from "returns the right results" — custom
analyzers, BM25 + function scoring, and the index-vs-search analyzer split. Elastic's own
relevance guidance is the canonical starting point.
- **source:** https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis.html (relevance: https://www.elastic.co/guide/en/elasticsearch/guide/current/scoring-theory.html)
- **reputation:** Official Elastic guidance · actively maintained
- **last_validated:** 2026-06-04
- **assumes:** documents already indexed with a mapping
- **adapt:** fork your analyzer chain + scoring tweaks into a private relevance note.

---

*Substitution-resistant private skill: your index mappings, analyzer choices, and the
relevance tuning specific to your corpus and what users actually search for. An LLM writes
a Query DSL clause fine; it doesn't know your data shape or what "good" results mean to you.*
