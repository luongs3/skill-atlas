# Job: Building MCP Servers & Agent Tools

**You're about to:** build an MCP server, package an agent tool, or wire a custom
integration into Claude/another agent. This job is well-served by Tier-A + Tier-B sources.

> Reputation signals pulled live **2026-06-02**.

---

## Tier A 🟢 — Canonical

### mcp-builder (official skill)
The official Anthropic skill for scaffolding an MCP server end-to-end.
- **source:** https://github.com/anthropics/skills/tree/main/skills/mcp-builder
- **reputation:** Official Anthropic · in the 145k★ skills repo
- **last_validated:** 2026-06-02 (path confirmed via API)
- **assumes:** Claude Code; Node or Python toolchain for the server
- **adapt:** fork to pin your preferred language/transport defaults.

### skill-creator (official skill)
Meta-skill: authoring new skills correctly. Use it to build your private forks.
- **source:** https://github.com/anthropics/skills/tree/main/skills/skill-creator
- **reputation:** Official Anthropic
- **last_validated:** 2026-06-02
- **assumes:** Claude Code
- **adapt:** none — it's the tool you adapt *with*.

### MCP reference servers
The canonical example servers from the protocol authors.
- **source:** https://github.com/modelcontextprotocol/servers
- **reputation:** Official MCP org · **86,590★** · pushed 2026-05-30
- **last_validated:** 2026-06-02
- **assumes:** MCP-compatible client
- **adapt:** copy a reference server as your skeleton.

---

## Tier B 🔵 — Community-proven (high rep + maintained)

### punkpeye/awesome-mcp-servers
The largest curated directory of existing MCP servers — check here before building, the
integration you need may already exist.
- **source:** https://github.com/punkpeye/awesome-mcp-servers
- **reputation:** **88,324★** · pushed 2026-05-27 (both halves: high stars + recent commit)
- **last_validated:** 2026-06-02
- **assumes:** nothing — it's an index
- **adapt:** none; use it to avoid rebuilding an existing server.

### obra/superpowers
A skills + methodology framework that packages agent workflows as installable plugins
across Claude Code, Codex, Cursor, opencode, Gemini, and Kimi.
- **source:** https://github.com/obra/superpowers
- **reputation:** 229,971★ · 20,449 forks · pushed 2026-06-17 (actively maintained; created 2025-10)
- **last_validated:** 2026-06-17
- **assumes:** Claude Code or another supported agent harness
- **adapt:** fork the skills you actually use; pin your own house rules/voice — don't run its defaults blind.

### mattpocock/skills
A curated set of engineering skills published straight from the author's `.claude` directory — practical, TS-leaning.
- **source:** https://github.com/mattpocock/skills
- **reputation:** from Matt Pocock's `.claude` directory · 132,081★ · pushed 2026-06-12
- **last_validated:** 2026-06-17
- **assumes:** Claude Code
- **adapt:** cherry-pick skills into your private set; his conventions are his — retune to yours.

### Anthropic Cookbook
Working code recipes for the Claude API, tool use, and agents. Authoritative code, but
it's examples not a packaged skill — read and adapt.
- **source:** https://github.com/anthropics/anthropic-cookbook
- **reputation:** Official Anthropic repo · **44,779★** · pushed 2026-05-30
- **last_validated:** 2026-06-02
- **assumes:** Claude API key
- **adapt:** lift the recipe you need into your own tool.

### affaan-m/ECC
An "agent harness performance optimization system" — skills, instincts, memory, and security
layers spanning Claude Code, Codex, opencode, Cursor, and more. Broad and ambitious.
- **source:** https://github.com/affaan-m/ECC
- **reputation:** 216,779★ · 33,293 forks · pushed 2026-06-16 — BUT created 2026-01 (young; very broad scope, real-world track record still thin → verify before trusting)
- **last_validated:** 2026-06-17
- **assumes:** a supported agent harness
- **adapt:** read the specific layer you want before adopting; don't install the whole system on faith.

---

## Tier C 🟡 — Useful, verify

### farion1231/cc-switch
A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes Agent. Only official website: 
- **source:** https://github.com/farion1231/cc-switch
- **reputation:** 102,782★ · pushed 2026-06-16 (auto-added 2026-06-17 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-17
- **assumes:** Rust toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### lobehub/lobehub
🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI t
- **source:** https://github.com/lobehub/lobehub
- **reputation:** 78,755★ · pushed 2026-06-17 (auto-added 2026-06-17 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-17
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### ComposioHQ/awesome-claude-skills
A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows
- **source:** https://github.com/ComposioHQ/awesome-claude-skills
- **reputation:** 65,056★ · pushed 2026-05-22 (auto-added 2026-06-18 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-18
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### gsd-build/get-shit-done
A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.
- **source:** https://github.com/gsd-build/get-shit-done
- **reputation:** 64,328★ · pushed 2026-05-31 (auto-added 2026-06-18 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-18
- **assumes:** JavaScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### addyosmani/agent-skills
Production-grade engineering skills for AI coding agents.
- **source:** https://github.com/addyosmani/agent-skills
- **reputation:** 62,593★ · pushed 2026-06-16 (auto-added 2026-06-18 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-18
- **assumes:** Shell toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### sansan0/TrendRadar
⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS
- **source:** https://github.com/sansan0/TrendRadar
- **reputation:** 59,601★ · pushed 2026-06-13 (auto-added 2026-06-18 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-18
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### upstash/context7
Context7 Platform -- Up-to-date code documentation for LLMs and AI code editors
- **source:** https://github.com/upstash/context7
- **reputation:** 57,603★ · pushed 2026-06-17 (auto-added 2026-06-18 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-18
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### VoltAgent/awesome-openclaw-skills
The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.🦞
- **source:** https://github.com/VoltAgent/awesome-openclaw-skills
- **reputation:** 50,348★ · pushed 2026-06-16 (auto-added 2026-06-18 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-18
- **assumes:** unknown toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### jeecgboot/JeecgBoot
AI 低代码平台「低代码 + 零代码」双驱动！低代码可一键生成前后端代码;零代码可 5 分钟搭建系统;AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合
- **source:** https://github.com/jeecgboot/JeecgBoot
- **reputation:** 46,775★ · pushed 2026-06-16 (auto-added 2026-06-18 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-18
- **assumes:** Java toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### zhayujie/CowAgent
Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-model, mul
- **source:** https://github.com/zhayujie/CowAgent
- **reputation:** 45,394★ · pushed 2026-06-18 (auto-added 2026-06-18 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-18
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### ChromeDevTools/chrome-devtools-mcp
Chrome DevTools for coding agents
- **source:** https://github.com/ChromeDevTools/chrome-devtools-mcp
- **reputation:** 43,958★ · pushed 2026-06-18 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### sickn33/antigravity-awesome-skills
Installable GitHub library of 1,500+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and more. Includes speciali
- **source:** https://github.com/sickn33/antigravity-awesome-skills
- **reputation:** 41,073★ · pushed 2026-06-18 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### wshobson/agents
Multi-harness agentic plugin marketplace for Claude Code, Codex CLI, Cursor, OpenCode, GitHub Copilot, and Gemini CLI
- **source:** https://github.com/wshobson/agents
- **reputation:** 36,940★ · pushed 2026-06-17 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### bytedance/UI-TARS-desktop
The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra
- **source:** https://github.com/bytedance/UI-TARS-desktop
- **reputation:** 36,876★ · pushed 2026-06-18 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### github/awesome-copilot
Community-contributed instructions, agents, skills, and configurations to help you make the most of GitHub Copilot.
- **source:** https://github.com/github/awesome-copilot
- **reputation:** 35,275★ · pushed 2026-06-19 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### github/github-mcp-server
GitHub's official MCP Server
- **source:** https://github.com/github/github-mcp-server
- **reputation:** 30,801★ · pushed 2026-06-18 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** Go toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### assafelovic/gpt-researcher
An autonomous agent that conducts deep research on any data using any LLM providers
- **source:** https://github.com/assafelovic/gpt-researcher
- **reputation:** 27,777★ · pushed 2026-05-28 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### oraios/serena
A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities  - the IDE for your agent
- **source:** https://github.com/oraios/serena
- **reputation:** 25,530★ · pushed 2026-06-16 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### OthmanAdi/planning-with-files
Persistent file-based planning for AI coding agents and long-running agentic tasks. Crash-proof markdown plans that survive context loss and
- **source:** https://github.com/OthmanAdi/planning-with-files
- **reputation:** 23,591★ · pushed 2026-06-16 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### activepieces/activepieces
AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents
- **source:** https://github.com/activepieces/activepieces
- **reputation:** 22,816★ · pushed 2026-06-19 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### JimLiu/baoyu-skills
(no description provided)
- **source:** https://github.com/JimLiu/baoyu-skills
- **reputation:** 21,960★ · pushed 2026-06-18 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### czlonkowski/n8n-mcp
A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you
- **source:** https://github.com/czlonkowski/n8n-mcp
- **reputation:** 21,845★ · pushed 2026-06-18 (auto-added 2026-06-19 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-19
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### phuryn/pm-skills
PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, execution, launch, and growth.
- **source:** https://github.com/phuryn/pm-skills
- **reputation:** 20,310★ · pushed 2026-06-06 (auto-added 2026-06-22 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-22
- **assumes:** unknown toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### DeusData/codebase-memory-mcp
High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 langu
- **source:** https://github.com/DeusData/codebase-memory-mcp
- **reputation:** 19,684★ · pushed 2026-06-29 (auto-added 2026-06-29 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-29
- **assumes:** C toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### danny-avila/LibreChat
Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, Open
- **source:** https://github.com/danny-avila/LibreChat
- **reputation:** 40,370★ · pushed 2026-07-06 (auto-added 2026-07-07 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-07-07
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### sickn33/agentic-awesome-skills
Installable GitHub library of 1,935+ agentic skills for Claude Code, Cursor, Codex CLI, Autohand Code, Gemini CLI, Antigravity, and more. In
- **source:** https://github.com/sickn33/agentic-awesome-skills
- **reputation:** 42,643★ · pushed 2026-07-08 (auto-added 2026-07-09 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-07-09
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### blader/humanizer
Agent skill that removes signs of AI-generated writing from text
- **source:** https://github.com/blader/humanizer
- **reputation:** 30,865★ · pushed 2026-07-22 (auto-added 2026-07-25 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-07-25
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### microsoft/ai-agents-for-beginners
18 Lessons to Get Started Building AI Agents
- **source:** https://github.com/microsoft/ai-agents-for-beginners
- **reputation:** 71,131★ · pushed 2026-07-29 (auto-added 2026-08-04 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-04
- **assumes:** Jupyter Notebook toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### Panniantong/Agent-Reach
Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero AP
- **source:** https://github.com/Panniantong/Agent-Reach
- **reputation:** 65,727★ · pushed 2026-07-25 (auto-added 2026-08-04 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-04
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### headroomlabs-ai/headroom
Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JS
- **source:** https://github.com/headroomlabs-ai/headroom
- **reputation:** 64,363★ · pushed 2026-08-04 (auto-added 2026-08-04 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-04
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### ComposioHQ/composio
Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that 
- **source:** https://github.com/ComposioHQ/composio
- **reputation:** 29,534★ · pushed 2026-08-04 (auto-added 2026-08-05 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-05
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### agentscope-ai/agentscope
Build and run agents you can see, understand and trust.
- **source:** https://github.com/agentscope-ai/agentscope
- **reputation:** 28,564★ · pushed 2026-08-04 (auto-added 2026-08-05 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-05
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### google-labs-code/design.md
A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent, structured understanding of a
- **source:** https://github.com/google-labs-code/design.md
- **reputation:** 26,954★ · pushed 2026-07-27 (auto-added 2026-08-05 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-05
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### modelcontextprotocol/python-sdk
The official Python SDK for Model Context Protocol servers and clients
- **source:** https://github.com/modelcontextprotocol/python-sdk
- **reputation:** 23,899★ · pushed 2026-08-05 (auto-added 2026-08-06 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-06
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### browser-use/video-use
Edit videos with coding agents
- **source:** https://github.com/browser-use/video-use
- **reputation:** 19,733★ · pushed 2026-07-01 (auto-added 2026-08-06 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-06
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### ayghri/i-have-adhd
A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **source:** https://github.com/ayghri/i-have-adhd
- **reputation:** 17,290★ · pushed 2026-08-05 (auto-added 2026-08-06 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-06
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### HKUDS/DeepCode
"DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)"
- **source:** https://github.com/HKUDS/DeepCode
- **reputation:** 16,198★ · pushed 2026-08-04 (auto-added 2026-08-06 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-06
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### XiaomiMiMo/MiMo-Code
MiMo Code: Where Models and Agents Co-Evolve
- **source:** https://github.com/XiaomiMiMo/MiMo-Code
- **reputation:** 12,667★ · pushed 2026-08-06 (auto-added 2026-08-07 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-07
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### cobusgreyling/loop-engineering
Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (insp
- **source:** https://github.com/cobusgreyling/loop-engineering
- **reputation:** 9,956★ · pushed 2026-08-07 (auto-added 2026-08-08 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-08
- **assumes:** JavaScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### EvoMap/evolver
The GEP-powered self-evolving engine for AI agents. Auditable evolution with Genes, Capsules, and Events. | evomap.ai
- **source:** https://github.com/EvoMap/evolver
- **reputation:** 8,949★ · pushed 2026-07-27 (auto-added 2026-08-08 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-08
- **assumes:** JavaScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### siyuan-note/siyuan
An open-source, privacy-first, self-hosted knowledge workspace where humans and AI agents work together 开源、隐私优先、自托管的知识工作空间，让人与智能体在此协作
- **source:** https://github.com/siyuan-note/siyuan
- **reputation:** 45,677★ · pushed 2026-08-08 (auto-added 2026-08-09 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-09
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### trycompai/crm
Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.
- **source:** https://github.com/trycompai/crm
- **reputation:** 7,790★ · pushed 2026-08-08 (auto-added 2026-08-09 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-09
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### ifixai-ai/iFixAi
Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most crucial question in the AI Agent Economy. Is the age
- **source:** https://github.com/ifixai-ai/iFixAi
- **reputation:** 7,366★ · pushed 2026-08-07 (auto-added 2026-08-09 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-09
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### strands-agents/harness-sdk
Build an agent harness and control it end-to-end. Open-source SDK for production AI agents in Python & TypeScript - any model, any cloud.
- **source:** https://github.com/strands-agents/harness-sdk
- **reputation:** 6,844★ · pushed 2026-08-07 (auto-added 2026-08-09 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-09
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### kangarooking/cangjie-skill
把书、长视频、播客等高价值内容蒸馏成可执行的 Agent Skills
- **source:** https://github.com/kangarooking/cangjie-skill
- **reputation:** 6,664★ · pushed 2026-08-07 (auto-added 2026-08-09 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-09
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### opensquilla/opensquilla
OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density
- **source:** https://github.com/opensquilla/opensquilla
- **reputation:** 6,584★ · pushed 2026-08-08 (auto-added 2026-08-09 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-09
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.
