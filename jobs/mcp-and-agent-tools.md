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

---

## Tier C 🟡 — Useful, verify

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
