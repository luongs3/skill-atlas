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

*This is the fastest-churning category in the atlas. The durable private skill is your agent architecture (eval harness, guardrails, retrieval strategy), not the framework. See [llm-app-development](llm-app-development.md).*
