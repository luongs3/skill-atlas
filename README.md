# Skill Atlas

**A curated, trust-rated index of public AI-agent skills, organized by job.**

This is not a skill store and not another dump of links. It answers one question an
agent (or a person configuring one) actually has:

> *"I'm about to do **X** (work on Upwork / run an interview / learn English).
> Which public skills should I load, and can I trust them?"*

The skills themselves live in their original repos. This atlas only catalogs **which
ones are good, where they come from, and how stale they are** — the trust layer that
every `awesome-*` list skips.

## Why this exists

A skill is *instructions an AI follows confidently*. That makes a stale or wrong skill
**worse than no skill** — it produces a confident wrong answer instead of making the
agent think. A public skill is only useful if you can answer three things about it
before loading:

1. **Source** — who wrote it, and is that source reputable? (verifiable identity, not a self-claim)
2. **Freshness** — when was it last validated against current tools? (a date someone re-checked, not the publish date)
3. **Fit** — what does it assume about your environment?

Every entry in this atlas carries that metadata. See [`_meta/SCHEMA.md`](_meta/SCHEMA.md).

## How to use it

1. Find your job under [`jobs/`](jobs/) (e.g. [`jobs/upwork.md`](jobs/upwork.md)).
2. Read the ranked skill list. Each entry has a **trust tier**, source URL, and last-validated date.
3. Load the public skill into your agent.
4. **Fork it private and adapt it to yourself.** The public skill is the starting
   point; your private version encodes your voice, creds, and rules. Never publish the
   private fork.

## Trust tiers (full definitions in `_meta/SCHEMA.md`)

| Tier | Meaning |
|------|---------|
| 🟢 **A — Canonical** | Official vendor source (Anthropic, the spec author). Trust by authorship. |
| 🔵 **B — Community-proven** | High reputation (stars/installs/maintainer track record) + actively maintained. |
| 🟡 **C — Useful, verify** | Plausible and useful but low/unknown reputation or unmaintained. Read before trusting. |
| 🔴 **D — Caution** | Stale, unmaintained >12mo, or known-broken against current tools. Listed so you don't rediscover it. |

## Index of jobs

| Job | Best tier available | Notes |
|-----|--------------------|-------|
| [Office documents (docx/pdf/pptx/xlsx)](jobs/office-documents.md) | 🟢 A | Official Anthropic skill per format — solved problem |
| [MCP servers & agent tools](jobs/mcp-and-agent-tools.md) | 🟢 A | Official mcp-builder + reference servers |
| [Prompt engineering](jobs/prompt-engineering.md) | 🟢 A | Official interactive tutorial + courses |
| [Web / frontend development](jobs/web-frontend.md) | 🟢 A | Official frontend-design + webapp-testing |
| [Technical interview prep](jobs/interview-prep.md) | 🔵 B | High-rep community repos; freshness varies (B→D) |
| [Data analysis](jobs/data-analysis.md) | 🟢 A | Official xlsx + pandas docs + Wes McKinney |
| [Upwork freelancing](jobs/upwork.md) | 🟡 C | No reputable public skill — the good one is bespoke |
| [Learning English](jobs/learning-english.md) | 🔵 B | Thin public layer — build a private `english-coach` |

_All 8 jobs seeded with live-verified sources. Dead links found during research were
excluded, not listed (see each job's exclusion notes)._

---

*Curated index. Skills remain the property of their original authors under their own
licenses. This repo claims no ownership of linked skills — only the trust assessment.*
