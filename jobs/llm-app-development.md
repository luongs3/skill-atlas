# Job: LLM App Development

**You're about to:** build an app *on top of* LLMs — RAG, agents, chains, tool-use. Note:
this is the framework layer; for serving/hosting models see
[llm-serving-inference](llm-serving-inference.md), and for prompts see
[prompt-engineering](prompt-engineering.md).

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical (vendor SDKs — start here)

### Anthropic Cookbook + Claude API
For building on Claude specifically, the official recipes beat any framework abstraction.
- **source:** https://github.com/anthropics/anthropic-cookbook (skill: `mcp-and-agent-tools.md`)
- **reputation:** Official Anthropic · **44,788★**
- **last_validated:** 2026-06-03
- **assumes:** Claude API key
- **adapt:** lift the recipe (RAG, tool-use, agents) you need.

---

## Tier B 🔵 — Community-proven (frameworks — use with care)

### LangChain
The most-used LLM app framework — chains, agents, RAG, huge integration surface.
- **source:** https://github.com/langchain-ai/langchain (docs: https://python.langchain.com)
- **reputation:** **138,380★** · pushed 2026-06-02 (very high stars + maintained)
- **last_validated:** 2026-06-03
- **assumes:** Python or JS
- **adapt:** ⚠️ heavy abstraction — many teams find raw SDK calls clearer for simple apps.
  Use LangChain when you genuinely need its integrations; don't add it reflexively.

### LlamaIndex — RAG-focused
Framework specialized for retrieval/RAG over your data.
- **source:** https://github.com/run-llama/llama_index (docs: https://docs.llamaindex.ai)
- **reputation:** **49,868★** · pushed 2026-05-29
- **last_validated:** 2026-06-03
- **assumes:** Python
- **adapt:** fork your chunking/embedding/retrieval config.

---

## The honest take (substitution warning)

LLM-app frameworks are the **fastest-moving, most-churned** category in this whole atlas —
today's standard is next quarter's legacy. So:
1. **Prefer the vendor SDK** (Anthropic/OpenAI) for anything simple; frameworks earn their
   weight only at real integration complexity.
2. **`last_validated` matters more here than anywhere** — re-check before trusting a tutorial.
3. The durable private skill isn't "how to use LangChain" — it's **your app's architecture**
   (retrieval strategy, eval harness, guardrails), which survives a framework swap.

---

## Tier C 🟡 — Useful, verify

### rtk-ai/rtk
CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **source:** https://github.com/rtk-ai/rtk
- **reputation:** 63,473★ · pushed 2026-06-17 (auto-added 2026-06-18 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-18
- **assumes:** Rust toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### DietrichGebert/ponytail
Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **source:** https://github.com/DietrichGebert/ponytail
- **reputation:** 37,251★ · pushed 2026-06-19 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** JavaScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### 1Panel-dev/MaxKB
🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。
- **source:** https://github.com/1Panel-dev/MaxKB
- **reputation:** 21,369★ · pushed 2026-06-19 (auto-added 2026-06-20 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-20
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### hesreallyhim/awesome-claude-code
A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic
- **source:** https://github.com/hesreallyhim/awesome-claude-code
- **reputation:** 47,602★ · pushed 2026-06-29 (auto-added 2026-06-30 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-30
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### Shubhamsaboo/awesome-llm-apps
100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- **source:** https://github.com/Shubhamsaboo/awesome-llm-apps
- **reputation:** 127,357★ · pushed 2026-07-23 (auto-added 2026-07-25 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-07-25
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### Mintplex-Labs/anything-llm
Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience
- **source:** https://github.com/Mintplex-Labs/anything-llm
- **reputation:** 64,299★ · pushed 2026-08-04 (auto-added 2026-08-04 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-04
- **assumes:** JavaScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### esengine/DeepSeek-Reasonix
DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.
- **source:** https://github.com/esengine/DeepSeek-Reasonix
- **reputation:** 30,787★ · pushed 2026-08-05 (auto-added 2026-08-05 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-05
- **assumes:** Go toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### charmbracelet/crush
Glamourous agentic coding for all 💘
- **source:** https://github.com/charmbracelet/crush
- **reputation:** 27,074★ · pushed 2026-08-05 (auto-added 2026-08-05 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-05
- **assumes:** Go toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### letta-ai/letta
Platform for stateful agents: AI with advanced memory that can learn and self-improve over time.
- **source:** https://github.com/letta-ai/letta
- **reputation:** 24,088★ · pushed 2026-08-01 (auto-added 2026-08-05 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-05
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### alibaba/open-code-review
Fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-l
- **source:** https://github.com/alibaba/open-code-review
- **reputation:** 19,155★ · pushed 2026-08-05 (auto-added 2026-08-06 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-06
- **assumes:** Go toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.
