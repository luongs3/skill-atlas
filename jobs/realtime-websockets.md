# Job: Realtime — WebSockets & Pub/Sub

**You're about to:** push live updates to clients — presence, broadcasting, reconnection, scaling fan-out.

> Reputation pulled live **2026-06-19** via `gh api`.

---

## Tier A 🟢 — Canonical

### Socket.IO
The mature realtime library — rooms, auto-reconnect, fallbacks. The default for Node realtime apps.
- **source:** https://github.com/socketio/socket.io
- **reputation:** **63,186★** · pushed 2026-06-17
- **last_validated:** 2026-06-19
- **assumes:** Node
- **adapt:** fork your event protocol + room strategy; plan horizontal scaling.

---

## Tier B 🔵 — Community-proven

### Centrifugo
Language-agnostic realtime messaging server — scales pub/sub independent of your app server.
- **source:** https://github.com/centrifugal/centrifugo
- **reputation:** **10,414★** · pushed 2026-06-16
- **last_validated:** 2026-06-19
- **assumes:** a server
- **adapt:** fork your channel namespaces + auth.

### ws
The bare, fast WebSocket server/client for Node — when you want the protocol, not a framework.
- **source:** https://github.com/websockets/ws
- **reputation:** **22,767★** · pushed 2026-06-11
- **last_validated:** 2026-06-19
- **assumes:** Node
- **adapt:** build your own protocol on top; handle reconnection yourself.
