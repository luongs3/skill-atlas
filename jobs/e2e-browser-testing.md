# Job: End-to-End Browser Testing

**You're about to:** automate real-browser tests — clicks, navigation, assertions across pages.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Playwright
The modern cross-browser E2E framework (Chromium/Firefox/WebKit), auto-wait, trace viewer.
- **source:** https://github.com/microsoft/playwright (docs: https://playwright.dev)
- **reputation:** Official Microsoft · **90,313★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** Node + a running app
- **adapt:** fork your page-object + auth-setup conventions.

---

## Tier B 🔵 — Community-proven

### Cypress
Developer-friendly E2E with a live test runner UI.
- **source:** https://github.com/cypress-io/cypress (docs: https://docs.cypress.io)
- **reputation:** Official Cypress · **49,650★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** Node + a running app
- **adapt:** pick Playwright OR Cypress; Playwright is the newer default.

### Puppeteer
Chrome DevTools Protocol automation (scraping, PDFs, headless Chrome).
- **source:** https://github.com/puppeteer/puppeteer (docs: https://pptr.dev)
- **reputation:** Official (Chrome) · **94,427★** · pushed 2026-06-03
- **last_validated:** 2026-06-05
- **assumes:** Node
- **adapt:** use for scraping/automation more than test assertions.

---

## Tier C 🟡 — Useful, verify

### browser-use/browser-use
🌐 Make websites accessible for AI agents. Automate tasks online with ease.
- **source:** https://github.com/browser-use/browser-use
- **reputation:** 107,752★ · pushed 2026-08-03 (auto-added 2026-08-04 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-04
- **assumes:** Python toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### h4ckf0r0day/obscura
The headless browser for AI agents and web scraping
- **source:** https://github.com/h4ckf0r0day/obscura
- **reputation:** 20,008★ · pushed 2026-08-05 (auto-added 2026-08-06 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-06
- **assumes:** Rust toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

### citrolabs/ego-lite
The fastest browser for AI agents to run browser automation, built for sharing your logged-in browser state with your AI agents, like Codex 
- **source:** https://github.com/citrolabs/ego-lite
- **reputation:** 9,238★ · pushed 2026-08-07 (auto-added 2026-08-08 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-08-08
- **assumes:** JavaScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

*The private skill is your app's auth + critical user flows encoded as reusable fixtures, so a new test starts from your real login, not a blank page. See [webapp-testing in mcp-and-agent-tools] and [javascript-testing](javascript-testing.md).*
