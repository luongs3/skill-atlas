# Job: Cloud (AWS & GCP)

**You're about to:** work with AWS or GCP — CLI, SDKs, service patterns, or architecture.
Canonical vendor sources + a high-rep practitioner guide.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical (vendor sources)

### AWS CLI + official docs
The command-line interface and the authoritative AWS service docs.
- **source:** https://github.com/aws/aws-cli (docs: https://docs.aws.amazon.com)
- **reputation:** Official AWS · **17,012★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** an AWS account
- **adapt:** build a private skill of your org's account structure, regions, and naming conventions.

### AWS SDK code examples
Official, runnable examples across every AWS service and language (incl. Go).
- **source:** https://github.com/awsdocs/aws-doc-sdk-examples
- **reputation:** Official AWS · **10,419★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **assumes:** an SDK + credentials
- **adapt:** lift the example for the service you need, then adapt to your IAM setup.

### GCP Go samples
Official Google Cloud samples for Go.
- **source:** https://github.com/GoogleCloudPlatform/golang-samples (docs: https://cloud.google.com/docs)
- **reputation:** Official GCP · **4,629★** · pushed 2026-06-01
- **last_validated:** 2026-06-03
- **assumes:** a GCP project
- **adapt:** none — reference.

---

## Tier C 🟡 — Useful but aging

### og-aws (Open Guide to AWS)
A famously practical, opinionated guide to AWS services — what's good, what bites.
- **source:** https://github.com/open-guides/og-aws
- **reputation:** **36,417★** BUT pushed **2024-08-16** (>12mo → C; AWS moves fast, verify specifics)
- **last_validated:** 2026-06-03
- **assumes:** nothing
- **adapt:** read the service notes for gotchas, but confirm pricing/limits against current AWS docs.

---

*Cloud work is heavily account-specific. The private skill that pays off: your org's
landing-zone conventions, IAM patterns, and the 5 services you actually use — things the
public docs can't know.*
