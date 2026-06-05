# Job: Secrets Management (Vault)

**You're about to:** manage secrets, encryption, and dynamic credentials with HashiCorp Vault.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### HashiCorp Vault
The standard for secrets management, encryption-as-a-service, and dynamic credentials.
- **source:** https://github.com/hashicorp/vault (docs: https://developer.hashicorp.com/vault)
- **reputation:** Official HashiCorp · **35,728★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a Vault deployment
- **adapt:** fork your auth-method + policy conventions.

---

## How to use this job

Reach for **Vault** when you've outgrown static secrets in env files and config and need centralized storage, audit, leasing, and especially **dynamic secrets** — short-lived DB/cloud credentials minted per request and auto-revoked. Choose the auth method by where the workload runs (Kubernetes auth in k8s, AWS/GCP IAM in cloud, AppRole for CI), and prefer dynamic secrets over long-lived static ones wherever the backend supports it. The decision to adopt hinges on whether you need rotation/audit at scale; for a tiny app, a cloud provider's managed secret store may be enough.

## Pitfalls

- **Secrets in environment variables leak.** Once Vault injects a secret into a process's env, it's visible via `/proc/<pid>/environ`, inherited by child processes, and captured in crash dumps and some logging. Prefer reading into memory or short-lived files with tight permissions, and use response wrapping.
- **The seal/unseal and root-token problem.** A sealed Vault (after restart) serves nothing until unsealed with the key shares; mismanaging Shamir shares or the recovery keys can lock you out permanently. Use auto-unseal (KMS/HSM), and revoke the initial root token after setup instead of leaving it lying around.
- **Leases and token TTLs expire mid-flight.** Dynamic credentials and tokens have TTLs; long-running jobs that don't renew get their DB creds revoked underneath them. Renew leases proactively and handle revocation, and remember the audit log records secret *access* metadata — protect it.

*Don't store secrets in env files or code. The private skill is your org's Vault paths + policies + injection pattern. See [authentication-authorization](authentication-authorization.md).*
