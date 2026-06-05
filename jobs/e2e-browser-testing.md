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

*The private skill is your app's auth + critical user flows encoded as reusable fixtures, so a new test starts from your real login, not a blank page. See [webapp-testing in mcp-and-agent-tools] and [javascript-testing](javascript-testing.md).*
