# Job: AI Agent Orchestration

**You're about to:** build multi-step LLM agents and pipelines — chains, tools, autonomous loops.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Anthropic Cookbook
Official Claude recipes for tool-use and agents — beats a framework for anything simple.
- **source:** https://github.com/anthropics/anthropic-cookbook
- **reputation:** Official Anthropic · high stars
- **last_validated:** 2026-06-05
- **assumes:** Claude API key
- **adapt:** lift the agent recipe you need.

---

## Tier B 🔵 — Community-proven

### Dify
Open-source LLM app platform — visual agent/workflow builder, RAG, observability.
- **source:** https://github.com/langgenius/dify (docs: https://docs.dify.ai)
- **reputation:** **143,913★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** self-host or cloud
- **adapt:** fork your app templates.

### LangChain / LlamaIndex
Framework layer for chains/agents (LangChain) and RAG (LlamaIndex). Use when integrations justify the abstraction.
- **source:** https://github.com/langchain-ai/langchain (138,531★) · https://github.com/run-llama/llama_index (49,924★)
- **reputation:** both very high stars, pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** Python/JS
- **adapt:** see [llm-app-development](llm-app-development.md) for the churn warning.

### google-gemini/gemini-cli
Google's open-source terminal agent — brings Gemini into the shell with tools and MCP support.
- **source:** https://github.com/google-gemini/gemini-cli
- **reputation:** Official Google · 105,343★ · pushed 2026-06-17 (one strong agent CLI among peers → B, not canonical)
- **last_validated:** 2026-06-17
- **assumes:** Gemini API key / Node
- **adapt:** pin your model + tool config; it's one harness among several (compare Claude Code, Codex).

### NousResearch/hermes-agent
Nous Research's open-source agent runtime ("the agent that grows with you") — skills, memory, MCP, cron.
- **source:** https://github.com/NousResearch/hermes-agent
- **reputation:** Nous Research · 195,448★ · pushed 2026-06-17 (substantial Python codebase, actively developed; one runtime among peers → B)
- **last_validated:** 2026-06-17
- **assumes:** self-host; API key for your model provider
- **adapt:** encode your own skills/memory/cron; the durable asset is your config, not the harness.

---

## Tier C 🟡 — Useful, verify

### thedotmack/claude-mem
Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and inject
- **source:** https://github.com/thedotmack/claude-mem
- **reputation:** 82,803★ · pushed 2026-06-16 (auto-added 2026-06-17 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-17
- **assumes:** JavaScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### JuliusBrussee/caveman
🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman
- **source:** https://github.com/JuliusBrussee/caveman
- **reputation:** 73,637★ · pushed 2026-06-12 (auto-added 2026-06-17 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-17
- **assumes:** JavaScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### bytedance/deer-flow
An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, suba
- **source:** https://github.com/bytedance/deer-flow
- **reputation:** 71,354★ · pushed 2026-06-17 (auto-added 2026-06-17 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-17
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### ruvnet/ruflo
🌊 The leading agent meta-harness for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversationa
- **source:** https://github.com/ruvnet/ruflo
- **reputation:** 60,035★ · pushed 2026-06-18 (auto-added 2026-06-18 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-18
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### VoltAgent/awesome-agent-skills
A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor
- **source:** https://github.com/VoltAgent/awesome-agent-skills
- **reputation:** 25,803★ · pushed 2026-06-16 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** unknown toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### earthtojake/text-to-cad
A library of agent skills for CAD, CAE and CAM
- **source:** https://github.com/earthtojake/text-to-cad
- **reputation:** 12,974★ · pushed 2026-08-06 (auto-added 2026-08-07 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-07
- **assumes:** JavaScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

*This is the fastest-churning category in the atlas. The durable private skill is your agent architecture (eval harness, guardrails, retrieval strategy), not the framework. See [llm-app-development](llm-app-development.md).*
