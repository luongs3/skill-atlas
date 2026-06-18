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
