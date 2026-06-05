# Job: Whiteboard & Canvas Apps

**You're about to:** build an infinite-canvas/diagramming feature into an app.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### tldraw
SDK for building infinite-canvas / whiteboard apps with React.
- **source:** https://github.com/tldraw/tldraw (docs: https://tldraw.dev)
- **reputation:** **47,609★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** React
- **adapt:** fork your custom shapes + tools.

---

## Tier B 🔵 — Community-proven

### Excalidraw
Hand-drawn-style whiteboard; embeddable + a great reference implementation.
- **source:** https://github.com/excalidraw/excalidraw (docs: https://docs.excalidraw.com)
- **reputation:** **124,646★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** React
- **adapt:** embed as-is, or study it for canvas patterns.

---

## How to use this job

Use **tldraw** when you're building a product feature on a supported, maintained SDK — custom shapes, tools, and multiplayer hooks designed to be extended in a React app. Reach for **Excalidraw** when you want the hand-drawn aesthetic specifically, want to embed a near-complete editor as-is, or want a reference implementation to study canvas/state patterns. The decision hinges on build-vs-embed: tldraw is the SDK you build *on*, Excalidraw is the app you embed or learn *from*. Note tldraw's license has commercial terms.

## Pitfalls

- **Re-rendering the whole canvas on every state change tanks performance** — both libraries expect you to subscribe to scoped store changes, not lift canvas state into React component state. Bridging editor state into a parent `useState` causes full re-renders on every pointer move.
- **Coordinate spaces bite you constantly** — screen vs canvas coordinates differ once the user pans/zooms. Placing a shape at raw `clientX/clientY` drops it in the wrong spot at any zoom ≠ 100%; always convert through the editor's transform.
- **Persisting/serializing the document means versioning the schema** — shape records evolve between SDK versions, so naively storing JSON breaks on upgrade. Use the library's migration/snapshot API instead of hand-rolling save/load.

---

*See [frontend-frameworks](frontend-frameworks.md). Niche but high-value when you need it. Private skill = your custom canvas shapes/tools.*
