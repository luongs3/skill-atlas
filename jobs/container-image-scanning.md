# Job: Container & Supply-Chain Security

**You're about to:** scan images, sign artifacts, and produce SBOMs — secure the build-to-deploy chain.

> Reputation pulled live **2026-06-19** via `gh api`.

---

## Tier A 🟢 — Canonical

### Cosign (Sigstore)
Sign + verify container images and artifacts — keyless signing, attestations. The supply-chain trust standard.
- **source:** https://github.com/sigstore/cosign
- **reputation:** **6,047★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a registry + CI
- **adapt:** fork your signing + verification policy (admission).

### Syft
Generate SBOMs from images/filesystems — the inventory behind vuln management.
- **source:** https://github.com/anchore/syft
- **reputation:** **9,136★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** CI
- **adapt:** fork your SBOM format + storage.

### Grype
Vulnerability scanner that consumes Syft SBOMs — fast, scriptable. Pairs with Syft.
- **source:** https://github.com/anchore/grype
- **reputation:** **12,447★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** CI
- **adapt:** fork your match/ignore rules + gates.

---

## Tier C 🟡 — Useful, verify

### TencentCloud/CubeSandbox
Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.
- **source:** https://github.com/TencentCloud/CubeSandbox
- **reputation:** 10,958★ · pushed 2026-08-06 (auto-added 2026-08-07 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-07
- **assumes:** Rust toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.
