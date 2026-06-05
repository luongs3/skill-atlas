# Job: Redis — Caching & In-Memory Data

**You're about to:** use Redis as a cache and data structure server — strings, hashes,
sorted sets, TTLs, persistence, and the caching patterns that keep it correct.

> Reputation pulled live **2026-06-04** via `gh api`.

For scaling Redis across nodes (cluster, sharding, failover), pair with
[scalability-distributed-systems](scalability-distributed-systems.md).

---

## Tier A 🟢 — Canonical

### Redis source + official docs
The reference in-memory store and the docs behind every data-structure and persistence
choice — strings/hashes/lists/sets/sorted-sets/streams, `EXPIRE`/TTL, eviction policies,
RDB + AOF persistence, pub/sub, and Lua scripting.
- **source:** https://github.com/redis/redis (docs: https://redis.io/docs/)
- **reputation:** Redis Ltd. · **74,686★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** a running redis-server
- **adapt:** none — reference. Match your deployed version's command reference.

---

## Tier B 🔵 — Community-proven

### Caching patterns
The correctness layer most teams get wrong: cache-aside vs write-through, TTL + jitter,
stampede protection (locks/early-recompute), and explicit invalidation. Redis's docs cover
the primitives; the pattern discipline is on you.
- **source:** https://redis.io/docs/latest/develop/use/patterns/ (client-side caching: https://redis.io/docs/latest/develop/reference/client-side-caching/)
- **reputation:** Official Redis guidance · actively maintained
- **last_validated:** 2026-06-04
- **assumes:** Redis fronting a slower source of truth
- **adapt:** fork your TTLs, key-naming scheme, and invalidation triggers into a private note.

---

*Substitution-resistant private skill: your key namespace, TTL policy, and the
invalidation rules tied to your data's freshness needs. An LLM knows `SETEX`; it doesn't
know which of your keys may serve stale and which must never.*
