---
name: skill-atlas
description: Find the right public AI-agent skill for a job — and know whether to trust it. Load when about to start a task type (Upwork freelancing, technical interviews, office documents, MCP/tool building, prompt engineering, web/frontend, data analysis, learning English) and you want to know which existing public skills to pull in, rated by source reputation and freshness. Answers "which skill do I load for X, and can I trust it?"
---

# Skill Atlas

A trust-rated index of public AI-agent skills, organized by job. Use it to answer:
**"I'm about to do X — which public skills should I load, and can I trust them?"**

The skills themselves live in their original repos. This atlas catalogs *which ones are
good, where they come from, and how stale they are* — the trust layer most skill lists skip.

## When to load this skill

At the **start of a task** that matches a known job, before hunting for tools yourself:

| If the task is about… | Read |
|---|---|
| Winning work on Upwork | `jobs/upwork.md` |
| Technical interview prep | `jobs/interview-prep.md` |
| Word/PDF/PowerPoint/Excel | `jobs/office-documents.md` |
| Building an MCP server / agent tool | `jobs/mcp-and-agent-tools.md` |
| Writing better prompts | `jobs/prompt-engineering.md` |
| Frontend / web app build or test | `jobs/web-frontend.md` |
| Exploring / cleaning / charting data | `jobs/data-analysis.md` |
| Improving English for work | `jobs/learning-english.md` |

## How to use an entry

Each entry carries a **trust tier** plus source URL, reputation signal, and a
`last_validated` date. Workflow:

1. Read the ranked list for your job. Prefer 🟢 A (canonical) and 🔵 B (community-proven).
2. Treat 🟡 C as "read before trusting" and 🔴 D as "stale — caution."
3. Load the public skill, then **fork it private and adapt it to yourself**. The public
   skill is the starting point; your private version encodes your voice, creds, and rules.

## Trust tiers

- 🟢 **A — Canonical:** official vendor source (Anthropic, the spec author). Trust by authorship.
- 🔵 **B — Community-proven:** high reputation (stars/installs) **and** actively maintained.
- 🟡 **C — Useful, verify:** plausible but low/unknown reputation. Read before trusting.
- 🔴 **D — Caution:** stale (>12mo), unmaintained, or known-broken. Listed so you don't rediscover it.

## Keeping it honest

`scripts/revalidate.sh` re-checks every source's liveness + GitHub stars/last-push (uses
`gh` for 5000 req/hr if available). An entry whose `last_validated` is >6 months old is
treated as C until reproven. See `_meta/SCHEMA.md` for the full schema and
`CONTRIBUTING.md` for the trust bar on new entries.

---

*Index repo: https://github.com/luongs3/skill-atlas — skills remain property of their
original authors under their own licenses; this repo provides only the trust assessment.*
