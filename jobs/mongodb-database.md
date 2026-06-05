# Job: MongoDB — Document Database

**You're about to:** model, query, and operate MongoDB — documents, the aggregation
pipeline, indexing, and replica-set/sharding operations.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### MongoDB server source + official docs
The reference document database and the docs behind every schema and query decision —
document modeling, the aggregation framework (`$match`/`$group`/`$lookup`), compound +
multikey + text indexes, replica sets, and sharding.
- **source:** https://github.com/mongodb/mongo (docs: https://www.mongodb.com/docs/)
- **reputation:** MongoDB Inc. · **28,343★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** a running mongod / Atlas cluster
- **adapt:** none — reference. Pin to your server version's manual.

---

## Tier B 🔵 — Community-proven

### Schema-design patterns (official guidance)
MongoDB's own pattern catalog — embed-vs-reference, bucketing, the outlier and computed
patterns. The corrective to relational-by-reflex modeling.
- **source:** https://www.mongodb.com/docs/manual/data-modeling/ (patterns: https://www.mongodb.com/blog/post/building-with-patterns-a-summary)
- **reputation:** Official MongoDB engineering guidance · actively maintained
- **last_validated:** 2026-06-04
- **assumes:** you know your read/write access patterns first
- **adapt:** fork the pattern choices that match your workload into a private modeling note.

---

*Substitution-resistant private skill: your collections' actual access patterns and the
embed/reference + shard-key decisions that follow from them. An LLM writes aggregation
pipelines fine; it doesn't know your read/write ratios, which queries must stay targeted,
or where an unbounded array will eventually blow past the 16 MB document limit.*
