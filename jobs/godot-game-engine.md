# Job: Godot Game Engine

**You're about to:** build a 2D/3D game with Godot — scenes, nodes, GDScript, export.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Godot Engine + docs
The open-source engine, official source and the full docs (GDScript, scenes, physics, export).
- **source:** https://github.com/godotengine/godot (docs: https://docs.godotengine.org)
- **reputation:** Official Godot Foundation · **112,072★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** Godot installed
- **adapt:** fork your project's node/scene organization + input-map conventions.

---

## Tier B 🔵 — Community-proven

### Awesome Godot
Curated index of Godot plugins, assets, and tutorials.
- **source:** https://github.com/godotengine/awesome-godot
- **reputation:** Community-curated, maintained
- **last_validated:** 2026-06-05
- **assumes:** nothing
- **adapt:** none — index.

---

## How to use this job

Build from the **official engine + docs** as the source of truth — the docs cover the scene/node model, signals, physics, and export pipeline far better than scattered tutorials, and the version you install must match the docs version (Godot 3.x vs 4.x APIs differ heavily). Use **Awesome Godot** to find a maintained plugin or addon before writing your own, but vet each for the engine major version it targets.

## Pitfalls

- **3.x vs 4.x is a hard break:** GDScript syntax, the rendering backend (Vulkan), and many node names changed in Godot 4. Copy-pasting 3.x tutorial code into a 4.x project fails in subtle ways — confirm the version of any snippet or addon.
- **Node references break on scene refactor:** `get_node("Path/To/Node")` and `$Path` are string/path-based, so renaming or reparenting a node in the scene tree silently breaks them at runtime, not at parse time. Prefer `@onready` exported NodePaths or unique names (`%Name`).
- **`_process` vs `_physics_process`:** putting movement/physics in `_process` (frame-rate dependent) instead of `_physics_process` (fixed timestep) causes jitter and inconsistent collisions across machines.

---

## Tier C 🟡 — Useful, verify

### anysearch-ai/anysearch-skill
Unified real-time search engine skill for AI agents. Supports general web search, vertical domain search, parallel batch search, and full-pa
- **source:** https://github.com/anysearch-ai/anysearch-skill
- **reputation:** 5,278★ · pushed 2026-08-04 (auto-added 2026-08-10 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-10
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

*An LLM writes GDScript fine, but doesn't know your game's architecture (state machines, scene tree, signals). Encode that in a private skill.*
