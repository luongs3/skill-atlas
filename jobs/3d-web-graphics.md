# Job: 3D Web Graphics

**You're about to:** render 3D in the browser — scenes, meshes, shaders with Three.js.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Three.js
The standard library for 3D in the browser (WebGL/WebGPU).
- **source:** https://github.com/mrdoob/three.js (docs: https://threejs.org/docs)
- **reputation:** **112,850★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** JS + WebGL basics
- **adapt:** fork your scene-setup boilerplate.

---

## Tier B 🔵 — Community-proven

### PixiJS
Fast 2D WebGL renderer (games, interactive graphics).
- **source:** https://github.com/pixijs/pixijs (docs: https://pixijs.download/release/docs)
- **reputation:** **47,322★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** JS
- **adapt:** use for 2D; Three.js for 3D.

---

## How to use this job

Reach for **Three.js** whenever you need true 3D — perspective cameras, lighting, meshes, GLTF models, or WebGPU. Use **PixiJS** when the work is fundamentally 2D (sprites, particles, interactive graphics, games) where Three.js's 3D machinery is overhead you don't need. The decision hinges on dimensionality, not complexity: a heavy 2D scene still belongs in Pixi, and a simple 3D cube still belongs in Three.

## Pitfalls

- **Geometries, materials, and textures are not garbage-collected** — they hold GPU resources. Removing a mesh from the scene leaks VRAM unless you explicitly call `.dispose()` on each. Long-running apps that rebuild scenes will crash the tab without disposal discipline.
- **The render loop keeps running when the tab is hidden if you use `setInterval`/`setTimeout`** — always drive it with `requestAnimationFrame`, which pauses on hidden tabs and avoids burning battery and GPU.
- **Loading many textures without a power-of-two check or mipmap setting causes silent quality/perf hits** — non-POT textures disable mipmapping and wrapping in WebGL1; resize assets or set the correct filters.

---

*See [frontend-frameworks](frontend-frameworks.md). Private skill = your render-loop + asset-loading setup.*
