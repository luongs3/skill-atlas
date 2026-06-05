# Job: Bevy (Rust Game Dev)

**You're about to:** build a game in Rust with Bevy's ECS — entities, components, systems.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Bevy + docs
Data-driven Rust game engine built on ECS. Official source + the Bevy Book.
- **source:** https://github.com/bevyengine/bevy (docs: https://bevyengine.org/learn/)
- **reputation:** Official Bevy · **46,446★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** Rust toolchain
- **adapt:** fork your ECS system/plugin organization.

---

## How to use this job

Reach for **Bevy** when you want a modern, data-driven Rust engine and you're comfortable on the ECS model — entities are IDs, components are plain data, systems are functions over queries. It fits gameplay/simulation projects where Rust's safety and performance matter and you accept a younger ecosystem; if you need a mature editor and asset store today, Bevy isn't that yet. Lean on plugins to modularize systems, and pin your Bevy version because the API moves fast.

## Pitfalls

- **Breaking API churn every release.** Bevy makes large breaking changes each minor version; tutorials and crates lag badly. Match every example to your exact version (this is why `last_validated` matters) and expect ecosystem crates to be a version behind.
- **System ordering and the borrow checker bite at runtime.** Two systems that mutably access the same component can't run in parallel, and ambiguous ordering causes nondeterministic behavior. Use explicit system sets / `.before()`/`.after()` and `Changed<T>` filters rather than assuming an order.
- **ECS misuse: shoving everything into one giant component.** Coarse components kill the cache locality and parallelism that ECS exists for. Keep components small and single-purpose, and prefer marker components + queries over `if`-chains on a god struct.

*Bevy's API churns between releases, so last_validated matters here. The durable private skill is your ECS architecture, not the version-specific API calls. See [rust-development](rust-development.md).*
