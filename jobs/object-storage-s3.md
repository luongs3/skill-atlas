# Job: Object Storage (S3)

**You're about to:** store and serve files via S3-compatible object storage, self-hosted or cloud.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## How to use this job

Reach for **MinIO** when you need the S3 API on infrastructure you control — local dev/CI, on-prem, air-gapped, or data-residency requirements that rule out a public cloud. If you just want durable managed storage and don't care about running the server, go straight to AWS S3 (see [cloud-aws-gcp](cloud-aws-gcp.md)); the decision hinges on whether owning the operational burden (erasure-coding, capacity, upgrades) buys you something you actually need. Either way, code against the S3 SDK so you can swap the endpoint without rewriting.

## Pitfalls

- **Egress and request costs dominate, not storage.** On cloud S3 the per-GB storage is cheap; cross-region/internet egress and per-request charges (especially millions of small `GET`/`LIST` calls) are what blow up the bill. Batch and cache aggressively.
- **`LIST` is paginated, slow, and not a filesystem.** There are no real directories — prefixes are a naming convention, and listing a bucket with millions of keys is expensive and eventually-consistent on some providers. Don't build hot paths around `LIST`; keep an index.
- **Abandoned multipart uploads cost money silently.** Failed large uploads leave orphaned parts that you keep paying for until a lifecycle rule aborts them. Set an `AbortIncompleteMultipartUpload` lifecycle policy.

*See [cloud-aws-gcp](cloud-aws-gcp.md) for AWS S3 itself. Private skill = your bucket layout + access-policy patterns.*

---

## Tier B 🔵 — Community-proven (high rep + maintained)

### MinIO
High-performance S3-compatible object storage you can self-host. NOTE: pushed 2026-04, slightly older than most.
- **source:** https://github.com/minio/minio (docs: https://min.io/docs)
- **reputation:** **61,197★** · pushed 2026-04-24
- **last_validated:** 2026-06-05
- **assumes:** a server or cluster
- **adapt:** fork your bucket + IAM-policy conventions.
