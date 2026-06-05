# Job: Reverse Proxy & Load Balancing

**You're about to:** put a proxy/load balancer in front of services — TLS, routing, balancing.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Caddy
Web server + reverse proxy with automatic HTTPS out of the box.
- **source:** https://github.com/caddyserver/caddy (docs: https://caddyserver.com/docs)
- **reputation:** **73,150★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** a server
- **adapt:** fork your Caddyfile template.

### Traefik
Cloud-native reverse proxy with auto service-discovery (great with Docker/K8s).
- **source:** https://github.com/traefik/traefik (docs: https://doc.traefik.io)
- **reputation:** **63,565★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** Docker/K8s
- **adapt:** fork your router/middleware labels.

---

## Tier B 🔵 — Community-proven

### Envoy / HAProxy
Envoy (L7 proxy, mesh data plane) and HAProxy (battle-tested L4/L7 LB).
- **source:** https://github.com/envoyproxy/envoy (28,328★) · https://github.com/haproxy/haproxy (6,597★)
- **reputation:** official, maintained
- **last_validated:** 2026-06-05
- **assumes:** infra
- **adapt:** reference for high-scale setups.

---

*See [nginx-web-servers](nginx-web-servers.md) for nginx specifically. Private skill = your standard proxy config (TLS, headers, rate limits). Generate TLS settings from Mozilla's SSL Config Generator, not a static guide.*
