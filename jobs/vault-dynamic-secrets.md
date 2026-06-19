# Job: Dynamic Secrets & PKI (Vault deep)

**You're about to:** issue short-lived dynamic credentials, manage a private PKI, and do transit encryption with Vault.

> Reputation pulled live **2026-06-19** via `gh api`.

Static-secrets basics in [secrets-management-vault](secrets-management-vault.md).

---

## Tier A 🟢 — Canonical

### Vault — dynamic secrets & PKI
Beyond KV: database/cloud dynamic creds, PKI issuance, transit encryption-as-a-service, leases + revocation. Docs define each engine.
- **source:** https://github.com/hashicorp/vault
- **reputation:** **35,802★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** a Vault cluster
- **adapt:** fork your secret engines + policies + auth methods.

---

## Tier B 🔵 — Community-proven

### External Secrets Operator
Sync secrets from Vault/AWS/GCP into K8s Secrets via CRDs — the GitOps-friendly bridge.
- **source:** https://github.com/external-secrets/external-secrets
- **reputation:** **6,692★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** a cluster + a backend
- **adapt:** fork your SecretStore + ExternalSecret set.
