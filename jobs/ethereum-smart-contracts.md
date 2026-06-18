# Job: Ethereum Smart Contracts

**You're about to:** write, test, and deploy Solidity smart contracts on Ethereum.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### go-ethereum (geth)
The reference Ethereum execution client. Official source + docs.
- **source:** https://github.com/ethereum/go-ethereum (docs: https://geth.ethereum.org/docs)
- **reputation:** Official Ethereum Foundation · **51,071★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** a node or RPC endpoint
- **adapt:** none — reference.

### OpenZeppelin Contracts
The audited, standard library of secure contract building blocks (ERC-20/721, access control). Do NOT roll your own.
- **source:** https://github.com/OpenZeppelin/openzeppelin-contracts (docs: https://docs.openzeppelin.com/contracts)
- **reputation:** Official OpenZeppelin · **27,121★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** Solidity toolchain
- **adapt:** inherit from these; fork only your contract-specific logic.

---

## Tier B 🔵 — Community-proven

### Foundry
The modern Solidity dev toolchain — fast testing, fuzzing, deployment.
- **source:** https://github.com/foundry-rs/foundry (docs: https://book.getfoundry.sh)
- **reputation:** **10,380★** · pushed 2026-06-05 (de-facto standard)
- **last_validated:** 2026-06-05
- **assumes:** Rust-installed CLI
- **adapt:** fork your test/deploy script conventions.

---

## Tier C 🟡 — Useful, verify

### CherryHQ/cherry-studio
AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to frontier LLMs
- **source:** https://github.com/CherryHQ/cherry-studio
- **reputation:** 47,498★ · pushed 2026-06-18 (auto-added 2026-06-18 by dev-scout; tier C until reviewed)
- **last_validated:** 2026-06-18
- **assumes:** TypeScript toolchain — verify before trusting
- **adapt:** read the repo before adopting; promote on the weekly re-tier if it proves out.

*Security is the whole game here: don't roll your own crypto/auth/token logic. The atlas points at audited libraries; an LLM-written contract is where reentrancy and overflow bugs live. See [security](security.md).*
