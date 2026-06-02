# Entry Schema

Every skill listed in a `jobs/*.md` file MUST carry these fields. The point of this
atlas is the trust metadata — an entry missing it is not allowed in.

## Required fields

| Field | What it answers | Rule |
|-------|-----------------|------|
| `name` | What is it? | Human name + short description |
| `source` | Where does it live? | Direct URL to the repo/file/doc |
| `tier` | How much do I trust it? | One of A / B / C / D (see below) |
| `reputation` | *Why* that tier? | The concrete signal: stars, official, maintainer, install count. Not a vibe. |
| `last_validated` | Is it stale? | `YYYY-MM-DD` someone actually re-checked it works against current tools. NOT the publish date. |
| `assumes` | Will it fit me? | Environment/tools it expects (Claude Code? a specific CLI? auth?) |
| `adapt` | What do I change for myself? | One line on what to fork/override in your private copy |

## Trust tiers — exact definitions

### 🟢 A — Canonical
Published by the vendor who defines the thing (Anthropic for Claude/Skills, the spec
author for a format). Trust derives from **authorship**: the source *is* the authority.
Still gets a `last_validated` date — canonical can still go stale across versions.

### 🔵 B — Community-proven
Not official, but carries a **hard reputation signal**: high stars (>1k), high install
count, or a maintainer with a known track record — AND a recent commit (pushed within
~3 months). Both halves required. High stars + dead for a year = downgrade to D.

### 🟡 C — Useful, verify
Plausible, useful-looking, but reputation is low or unknown, or you couldn't confirm
maintenance. **Read the whole thing before trusting it.** Most of the long tail is C.

### 🔴 D — Caution
Stale (>12 months no commits), unmaintained, or confirmed-broken against current tools.
Listed deliberately so you don't waste time rediscovering it's dead.

## Validation rule (the thing that makes this not-a-link-dump)

`last_validated` is a **promise that someone re-checked it**, not a publish timestamp.
A revalidation pass should:

1. Confirm the source URL still 200s.
2. Refresh the reputation signal (re-pull stars / last-push date).
3. Spot-check that instructions don't reference renamed flags / dead tools.
4. Bump the date, or downgrade the tier if it rotted.

An entry whose `last_validated` is >6 months old should be treated as **C until reproven**,
regardless of its stated tier.
