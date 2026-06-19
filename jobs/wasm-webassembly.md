# Job: WebAssembly

**You're about to:** run near-native code in the browser/edge — compile from Rust/C/Go, interop with JS, WASI.

> Reputation pulled live **2026-06-19** via `gh api`.

---

## Tier A 🟢 — Canonical

### wasm-bindgen
The Rust↔JS interop standard for WebAssembly — bind functions, types, the DOM. The Rust-to-web path.
- **source:** https://github.com/rustwasm/wasm-bindgen
- **reputation:** **9,047★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Rust toolchain
- **adapt:** fork your bindings + build (wasm-pack).

### Wasmtime
The reference WASI runtime — run WebAssembly server-side/edge securely. Bytecode Alliance.
- **source:** https://github.com/bytecodealliance/wasmtime
- **reputation:** **18,222★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a wasm module
- **adapt:** fork your host imports + sandbox config.

---

## Tier B 🔵 — Community-proven

### Emscripten
Compile C/C++ to WebAssembly — port native libraries to the browser. Mature, niche.
- **source:** https://github.com/emscripten-core/emscripten
- **reputation:** **27,431★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** C/C++ toolchain
- **adapt:** fork your build flags + JS glue.
