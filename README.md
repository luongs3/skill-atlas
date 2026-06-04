# Skill Atlas

![Skill Atlas — a trust-rated index of public AI-agent skills, organized by job. Trust tiers A (canonical) to D (caution).](assets/hero.png)

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

## Install (use it as a skill)

The atlas ships as a loadable **Agent Skill**. Drop it where your agent looks for skills
so it reaches for the atlas automatically at the start of a task:

```bash
# Claude Code / Hermes-style skills dir (adjust path to your setup)
git clone https://github.com/luongs3/skill-atlas \
  ~/.claude/skills/skill-atlas
```

Once installed, your agent loads `skill-atlas` when a task matches a known job and pulls
the right trust-rated skills for it. No install needed to just browse — read [`jobs/`](jobs/) directly.

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
| [Go development](jobs/go-development.md) | 🟢 A | Effective Go + Uber style guide + awesome-go |
| [Git & version control](jobs/git-version-control.md) | 🟢 A | Pro Git + git official docs |
| [DevOps & infrastructure](jobs/devops-infrastructure.md) | 🟢 A | Terraform + Kubernetes + DevOps exercises |
| [Docker & containers](jobs/docker-containers.md) | 🟢 A | Moby engine + awesome-compose |
| [Databases & SQL (Postgres)](jobs/databases-sql.md) | 🟢 A | Postgres + sqlc + migrate/goose |
| [API design (REST & gRPC)](jobs/api-design.md) | 🟢 A | MS API guidelines + grpc-go + public-apis |
| [Observability & monitoring](jobs/observability-monitoring.md) | 🟢 A | Prometheus + Grafana + OpenTelemetry |
| [Go backend libraries](jobs/go-backend-libraries.md) | 🔵 B | Gin + Cobra + Zap + Testify |
| [Scalability & distributed systems](jobs/scalability-distributed-systems.md) | 🔵 B | awesome-scalability + Kafka + Redis |
| [Software design patterns](jobs/software-design-patterns.md) | 🟡 C | Good refs but aging — learn via agent review |
| [Cloud (AWS & GCP)](jobs/cloud-aws-gcp.md) | 🟢 A | aws-cli + SDK examples + GCP samples |
| [CI/CD pipelines](jobs/cicd-pipelines.md) | 🟢 A | GH Actions starters + Argo CD + Flux |
| [Authentication & authorization](jobs/authentication-authorization.md) | 🟢 A | Keycloak + Ory + golang-jwt + Casbin |
| [Frontend frameworks](jobs/frontend-frameworks.md) | 🟢 A | React/Next/Vue/Svelte + Tailwind (all official) |
| [Message queues & streaming](jobs/message-queues-streaming.md) | 🟢 A | RabbitMQ + Temporal + NATS + Asynq |
| [Go testing](jobs/go-testing.md) | 🔵 B | Testify + Mockery + testcontainers-go |
| [Application security](jobs/security.md) | 🟢 A | OWASP cheat sheets + PayloadsAllTheThings |
| [Algorithms & system design](jobs/algorithms-system-design.md) | 🔵 B | system-design-primer (351k★) + JS-algorithms |
| [Career roadmaps & CS fundamentals](jobs/career-roadmaps.md) | 🔵 B | developer-roadmap (356k★ / roadmap.sh) |
| [Technical interview prep](jobs/interview-prep.md) | 🔵 B | High-rep community repos; freshness varies (B→D) |
| [Data analysis](jobs/data-analysis.md) | 🟢 A | Official xlsx + pandas docs + Wes McKinney |
| [Data engineering](jobs/data-engineering.md) | 🟢 A | Airflow + Spark + dbt + ClickHouse + Flink |
| [Mobile development](jobs/mobile-development.md) | 🟢 A | Flutter + React Native + Swift + Now-in-Android |
| [LLM app development](jobs/llm-app-development.md) | 🟢 A | Anthropic Cookbook + LangChain + LlamaIndex |
| [LLM serving & inference](jobs/llm-serving-inference.md) | 🟢 A | Ollama + llama.cpp + vLLM |
| [Linux & shell](jobs/linux-shell.md) | 🟢 A | tldr + ShellCheck (+ aging guides at C) |
| [Nginx & web servers](jobs/nginx-web-servers.md) | 🟢 A | nginx official + admins-handbook (C) |
| [Learning resources](jobs/learning-resources.md) | 🔵 B | free-programming-books + awesome-lang lists |
| [Upwork freelancing](jobs/upwork.md) | 🟡 C | No reputable public skill — the good one is bespoke |
| [Learning English](jobs/learning-english.md) | 🔴 D→build | Public repos stale/dead — build a private `english-coach` |

_34 jobs, all seeded with live-verified sources (`gh api`, 2026-06-03). Dead links found
during research were excluded, not listed (see each job's exclusion notes)._

---

*Curated index. Skills remain the property of their original authors under their own
licenses. This repo claims no ownership of linked skills — only the trust assessment.*
