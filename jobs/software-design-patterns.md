# Job: Software Design Patterns

**You're about to:** apply a design pattern, refactor toward one, or study OOP/architectural
patterns. Useful community references — but note the best ones are **aging**, so verify.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier C 🟡 — Useful but aging (verify against current language idioms)

### Design Patterns for Humans
The most approachable plain-language intro to the classic GoF patterns with code examples.
- **source:** https://github.com/kamranahmedse/design-patterns-for-humans
- **reputation:** **47,855★** BUT pushed **2024-12-02** (>6mo → C; concepts don't rot, examples might)
- **last_validated:** 2026-06-03
- **assumes:** basic OOP
- **adapt:** learn the pattern, then implement in your language's idiom (Go favors composition over inheritance — many GoF patterns simplify).

### awesome-design-patterns
Curated index of pattern resources across languages and paradigms.
- **source:** https://github.com/DovAmir/awesome-design-patterns
- **reputation:** **47,594★** BUT pushed **2024-10-25** (>12mo → aging index; spot-check links)
- **last_validated:** 2026-06-03
- **assumes:** nothing
- **adapt:** none — use as a jumping-off index.

---

## Tier A 🟢 — The better approach for *learning* patterns

For understanding when/why to apply a pattern (not memorizing UML), the highest-trust route
is **the agent as a design reviewer**: describe your problem, ask which pattern fits and the
tradeoffs, then have it critique your implementation. LLMs reason about design patterns
reliably — this is squarely in scope. Build a private `design-review` skill (relevant
pattern + the *cost* of applying it + a smell check) with the official **skill-creator**
(https://github.com/anthropics/skills/tree/main/skills/skill-creator).

> Caveat worth encoding in that private skill: patterns are easy to over-apply. The senior
> move is often *not* introducing a pattern. Make the skill push back, not just suggest.
