# Job: Web / Frontend Development

**You're about to:** build a frontend, design a web UI, or test a web app with an agent.
Official Anthropic skills cover the core; check the MCP directory for integrations.

> Reputation signals pulled live **2026-06-02**.

---

## Tier A 🟢 — Canonical (official Anthropic skills)

All in `anthropics/skills/skills/` (145,275★, validated 2026-06-02).

### frontend-design
Generating frontends with good design defaults.
- **source:** https://github.com/anthropics/skills/tree/main/skills/frontend-design
- **reputation:** Official Anthropic
- **last_validated:** 2026-06-02
- **assumes:** Claude Code
- **adapt:** fork to pin your stack (React/Tailwind/etc.) and design system.

### web-artifacts-builder
Building interactive web artifacts.
- **source:** https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder
- **reputation:** Official Anthropic
- **last_validated:** 2026-06-02
- **assumes:** Claude Code
- **adapt:** none for general use.

### webapp-testing
Testing web apps (the QA half most people skip).
- **source:** https://github.com/anthropics/skills/tree/main/skills/webapp-testing
- **reputation:** Official Anthropic
- **last_validated:** 2026-06-02
- **assumes:** Claude Code; a running app to point it at
- **adapt:** fork to encode your app's auth/flows.

### canvas-design / algorithmic-art / theme-factory
Visual + generative-design skills, same repo, all Tier A.
- canvas-design → https://github.com/anthropics/skills/tree/main/skills/canvas-design
- algorithmic-art → https://github.com/anthropics/skills/tree/main/skills/algorithmic-art
- theme-factory → https://github.com/anthropics/skills/tree/main/skills/theme-factory

---

## Tier C 🟡 — Useful, verify

### OpenAI Cookbook (patterns transfer)
Not Claude-specific, but the engineering recipes (RAG, function calling, eval) are
high-quality and the patterns port over.
- **source:** https://github.com/openai/openai-cookbook
- **reputation:** Official OpenAI · **73,923★** · pushed 2026-06-01
- **last_validated:** 2026-06-02
- **assumes:** OpenAI-flavored examples — translate to Claude
- **adapt:** lift the pattern, swap the SDK.
