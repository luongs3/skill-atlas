# Job: Nginx & Web Servers

**You're about to:** configure nginx — reverse proxy, TLS, load balancing, or debug a
vhost. Canonical source + a deep (but aging) practitioner handbook.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical

### nginx official source + docs
The reference for directives, modules, and configuration.
- **source:** https://github.com/nginx/nginx (docs: https://nginx.org/en/docs/)
- **reputation:** The nginx project · **30,535★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **assumes:** nginx installed
- **adapt:** fork your standard vhost template (TLS, proxy headers, gzip, security headers).

---

## Tier C 🟡 — Useful but aging

### nginx-admins-handbook
An exhaustive practitioner guide — config patterns, performance, security hardening.
- **source:** https://github.com/trimstray/nginx-admins-handbook
- **reputation:** **14,176★** BUT pushed **2024-11-19** (>6mo → C; nginx config is stable, but verify TLS/security specifics against current best practice)
- **last_validated:** 2026-06-03
- **assumes:** basic nginx
- **adapt:** lift the hardening checklist, but re-confirm cipher suites / TLS settings against a current source (Mozilla SSL Config Generator).

---

## How to use this job

nginx config is exactly the kind of thing an LLM writes well — but a *wrong* nginx config
fails in subtle, security-relevant ways (open proxy, leaked headers, weak TLS). So:
1. Use the canonical docs for directive behavior.
2. Generate your TLS config from **Mozilla's SSL Configuration Generator** (current by
   definition), not a static guide.
3. Encode your org's standard server block as a private skill — proxy headers, rate limits,
   security headers — so every new vhost starts correct.

> This atlas's own infrastructure note: the operator's VPS uses host nginx + Certbot in
> front of a docker-compose stack — a private skill encoding *that* topology beats any
> generic nginx guide.
