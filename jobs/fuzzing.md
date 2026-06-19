# Job: Fuzzing

**You're about to:** find crashes + memory bugs by feeding programs malformed input — coverage-guided fuzzing.

> Reputation pulled live **2026-06-19** via `gh api`.

---

## Tier A 🟢 — Canonical

### AFL++
The leading coverage-guided fuzzer — mutations, instrumentation, sanitizer integration. The native-code standard.
- **source:** https://github.com/AFLplusplus/AFLplusplus
- **reputation:** **6,608★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** C/C++ build + sanitizers
- **adapt:** fork your harness + seed corpus.

### OSS-Fuzz
Google's continuous fuzzing infra + a library of real harnesses to learn from.
- **source:** https://github.com/google/oss-fuzz
- **reputation:** **12,359★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a fuzzable target
- **adapt:** study harness patterns; adapt to your code.

---

## Tier B 🔵 — Community-proven

### cargo-fuzz
libFuzzer integration for Rust — `cargo fuzz` to coverage-fuzz Rust targets. The Rust default.
- **source:** https://github.com/rust-fuzz/cargo-fuzz
- **reputation:** **1,829★** · pushed 2026-06-09
- **last_validated:** 2026-06-19
- **assumes:** Rust nightly
- **adapt:** fork your fuzz targets + corpus.
