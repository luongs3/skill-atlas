# Job: Container Runtimes & Compose

**You're about to:** run and orchestrate containers locally — Compose, containerd, Podman.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Docker Compose
Define and run multi-container apps from a single YAML.
- **source:** https://github.com/docker/compose (docs: https://docs.docker.com/compose)
- **reputation:** Official Docker · **37,482★** · pushed 2026-06-03
- **last_validated:** 2026-06-05
- **assumes:** Docker
- **adapt:** fork your standard compose stack (healthchecks, networks).

### containerd / runc
The low-level runtime under Docker and Kubernetes.
- **source:** https://github.com/containerd/containerd (20,801★) · https://github.com/opencontainers/runc (13,250★)
- **reputation:** official (CNCF/OCI), maintained
- **last_validated:** 2026-06-05
- **assumes:** Linux
- **adapt:** reference-level; you rarely touch these directly.

---

## Tier B 🔵 — Community-proven

### Podman
Daemonless, rootless Docker alternative.
- **source:** https://github.com/podman-desktop/podman-desktop (docs: https://podman.io)
- **reputation:** **7,687★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** Linux/macOS
- **adapt:** drop-in for Docker in many flows.

---

*See [docker-containers](docker-containers.md). Private skill = your standard local stack + base images.*
