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

---

## Tier C 🟡 — Useful, verify

### Anthropic Cookbook
Working code recipes for the Claude API, tool use, and agents. Authoritative code, but
it's examples not a packaged skill — read and adapt.
- **source:** https://github.com/anthropics/anthropic-cookbook
- **reputation:** Official Anthropic repo (live, verified 2026-06-02)
- **last_validated:** 2026-06-02 (HTML 200; star count rate-limited at pull time)
- **assumes:** Claude API key
- **adapt:** lift the recipe you need into your own tool.
