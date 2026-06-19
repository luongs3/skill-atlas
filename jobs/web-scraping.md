# Job: Web Scraping & Crawling

**You're about to:** extract data from sites at scale — async crawling, anti-bot handling, structured output.

> Reputation pulled live **2026-06-19** via `gh api`.

Browser automation overlaps [e2e-browser-testing](e2e-browser-testing.md).

---

## Tier A 🟢 — Canonical

### Scrapy
The mature async crawling framework — spiders, pipelines, throttling. The Python scraping standard.
- **source:** https://github.com/scrapy/scrapy
- **reputation:** **62,319★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** fork your spiders + item pipelines; respect robots/ToS.

### Playwright
Headless-browser automation for JS-heavy sites — when HTTP scraping isn't enough.
- **source:** https://github.com/microsoft/playwright
- **reputation:** **91,235★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** Node/Python + browsers
- **adapt:** fork your selectors; budget for anti-bot.

---

## Tier B 🔵 — Community-proven

### Crawl4AI
LLM-oriented crawler — outputs clean markdown for RAG/agents. Fast-moving; verify before prod.
- **source:** https://github.com/unclecode/crawl4ai
- **reputation:** **68,910★** · pushed 2026-06-18
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** fork your extraction + chunking for your LLM.
