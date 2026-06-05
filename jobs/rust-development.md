# Job: Rust Development

**You're about to:** write Rust — idiomatic, memory-safe code, the standard toolchain, and learning paths.
All canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### rustc + official docs
The reference compiler and the official docs (std library reference, language reference, edition guides).
- **source:** https://github.com/rust-lang/rust (docs: https://doc.rust-lang.org)
- **reputation:** The Rust project · **113,409★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Rust toolchain installed (rustup/cargo)
- **adapt:** none — reference. Pin your edition + MSRV in `Cargo.toml`.

### The Rust Book
The official book; the baseline every Rust learner and team references for ownership, lifetimes, traits, and idiom.
- **source:** https://doc.rust-lang.org/book
- **reputation:** Official Rust documentation
- **last_validated:** 2026-06-04
- **assumes:** nothing
- **adapt:** fork your team's idiom deltas (error-handling crate choice — `anyhow`/`thiserror`, async runtime — `tokio`/`async-std`) into a private guide.

---

## Tier B 🔵 — Community-proven (learning)

### rustlings
The canonical hands-on exercise set for learning Rust syntax and ownership by fixing small failing programs.
- **source:** https://github.com/rust-lang/rustlings
- **reputation:** rust-lang org · **63,081★** · pushed 2026-05-25
- **last_validated:** 2026-06-04
- **assumes:** Rust toolchain installed
- **adapt:** none — learning resource; work through it before onboarding to a Rust codebase.

---

*Substitution-resistant private skill: your crate's module layout + feature-flag conventions
(workspace structure, MSRV policy, your CI's clippy/fmt gates, chosen async runtime). An LLM
writes Rust fine; it doesn't know your repo's rules.*
