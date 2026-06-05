# Job: Phaser (Web Games)

**You're about to:** build a browser game with Phaser — sprites, physics, scenes in JS/TS.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Phaser + docs
The most-used HTML5 game framework. Official source + API docs + examples.
- **source:** https://github.com/photonstorm/phaser (docs: https://docs.phaser.io)
- **reputation:** Official Phaser Studio · **39,720★** · pushed 2026-06-03
- **last_validated:** 2026-06-05
- **assumes:** JS/TS toolchain
- **adapt:** fork your scene/asset-loading conventions.

---

## How to use this job

Reach for **Phaser** when you want a batteries-included 2D framework — sprites, tweens, input, audio, and a choice of Arcade or Matter physics — without assembling your own engine. Pick **Arcade physics** for fast AABB collision (platformers, shooters) and only reach for Matter when you genuinely need rotation, joints, or non-rectangular bodies; the decision hinges on whether you need real rigid-body simulation or just overlap checks. Use TypeScript from the start — the type defs catch a huge class of scene/config typos (see [typescript-javascript](typescript-javascript.md)).

## Pitfalls

- **Loading assets in `create()` instead of `preload()`.** Assets queued outside the loader's `preload` phase aren't ready when `create()` runs, so sprites silently fail to appear. Queue every load in `preload()` and reference keys in `create()`.
- **Scene state leaks between restarts.** Phaser doesn't reset your custom properties or event listeners on `scene.restart()`/`start()` — stale timers and listeners pile up and fire on dead objects. Clean up in `shutdown`/`destroy` and re-init state in `create()`.
- **Game loop tied to frame rate.** Movement coded as `x += speed` runs faster on 144Hz monitors than 60Hz. Always multiply by `delta` (or use physics velocities) so motion is frame-rate independent.

*Phaser code is well within an LLM's range; the private value is your game's scene structure and asset pipeline. See [typescript-javascript](typescript-javascript.md).*
