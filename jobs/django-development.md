# Job: Django Development

**You're about to:** build a Django web app — models, views, ORM, the batteries-included framework.
All canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### Django + official docs
The framework itself and the official docs (tutorial, model/ORM reference, deployment guide).
- **source:** https://github.com/django/django (docs: https://docs.djangoproject.com/)
- **reputation:** The Django project · **87,634★** · pushed 2026-06-03
- **last_validated:** 2026-06-04
- **assumes:** Python installed
- **adapt:** none — reference.

### Django docs — topic & how-to guides
The official how-to and topic guides: auth, forms, migrations, security, ORM optimization.
- **source:** https://docs.djangoproject.com/en/stable/topics/
- **reputation:** Official Django documentation
- **last_validated:** 2026-06-04
- **assumes:** Django project scaffolded
- **adapt:** fork your settings split (dev/prod), middleware stack, and app layout.

---

## Tier B 🔵 — Community-proven

### Django REST Framework
The de-facto standard for building APIs on top of Django — serializers, viewsets, auth.
- **source:** https://github.com/encode/django-rest-framework (docs: https://www.django-rest-framework.org/)
- **reputation:** Encode · very high stars · actively maintained
- **last_validated:** 2026-06-04
- **assumes:** Django project
- **adapt:** fork your permission classes + pagination defaults.

### Django security checklist
The official deployment-readiness checklist — settings every production app must harden.
- **source:** https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
- **reputation:** Official Django documentation
- **last_validated:** 2026-06-04
- **assumes:** Django project nearing deploy
- **adapt:** fork your CSP, ALLOWED_HOSTS, and secret-management conventions.

---

*Substitution-resistant private skill: your project's app layout, settings split, auth flow, and
error-handling conventions. An LLM writes Django views fine; it doesn't know your team's repo rules.*
