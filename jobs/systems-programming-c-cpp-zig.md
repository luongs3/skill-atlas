# Job: Systems Programming (C / C++ / Zig)

**You're about to:** write low-level systems code — C, C++, and Zig — with canonical toolchains and references.
Mostly canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### LLVM / Clang
The reference compiler infrastructure for C and C++ (and the backend many languages target).
- **source:** https://github.com/llvm/llvm-project
- **reputation:** The LLVM project · **38,641★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** clang/LLVM toolchain installed
- **adapt:** none — reference.

### isocpp.org — the C++ standard
The official C++ standards committee site; authoritative on the language standard and direction.
- **source:** https://isocpp.org
- **reputation:** Official C++ standards body (ISO WG21)
- **last_validated:** 2026-06-04
- **assumes:** nothing
- **adapt:** none — reference.

### Zig compiler
The reference Zig compiler. Note: pre-1.0 and last push **2025-11-27** (>6 months ago) — verify code
against the current release, since Zig's std/syntax changes fast pre-1.0.
- **source:** https://github.com/ziglang/zig
- **reputation:** ziglang org · **42,975★** · pushed 2025-11-27
- **last_validated:** 2026-06-04 (⚠️ verify against current release)
- **assumes:** Zig toolchain installed
- **adapt:** pin a Zig version; re-check API drift against release notes.

---

## Tier B 🔵 — Community-proven

### cppreference.com
The community-canonical C++ (and C) standard-library reference — the daily-driver lookup for the language.
- **source:** https://cppreference.com
- **reputation:** Community-maintained · canonical reference
- **last_validated:** 2026-06-04
- **assumes:** nothing
- **adapt:** none — reference.

---

*Substitution-resistant private skill: your build system (CMake/Meson/Zig build) conventions, your
sanitizer/UBSan + warning-flag policy, and target/ABI constraints. An LLM writes C/C++/Zig fine; it
doesn't know your repo's rules.*
