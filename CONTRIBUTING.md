# Contributing to Skill Atlas

The atlas is only as good as its trust bar. One unvetted entry and it becomes another
link-dump. So entries are cheap to *add* and expensive to *trust* — the schema enforces it.

## Adding a skill to a job

1. Open (or create) `jobs/<job>.md`.
2. Add an entry with **every** field from `_meta/SCHEMA.md`. An entry missing
   `source` / `tier` / `reputation` / `last_validated` is rejected — no exceptions.
3. `reputation` must be a **concrete signal**, not a vibe:
   - ✅ "Official Anthropic repo · 145,275★ · pushed 2026-05-29"
   - ✅ "Maintainer is the MCP spec co-author; 12k installs on Smithery"
   - ❌ "Looks solid", "popular", "well-known"
4. `last_validated` must be a date **you personally re-checked** (URL 200 + reputation
   re-pulled + spot-checked for dead flags). It is **not** the publish date.

## Tiering honestly

- Don't inflate. A 200★ repo with no commits in a year is **D**, not B, no matter how
  nice the README reads.
- Default unknown things to **C**. Tier A is vendor-canonical only. Tier B requires
  *both* a hard reputation number *and* a recent commit.
- A skill that is *instructions an AI follows* and is subtly wrong is worse than nothing.
  When in doubt, tier down.

## Revalidation

Run `scripts/revalidate.sh` (see below) to refresh liveness + star counts for every
linked GitHub source. Any entry whose `last_validated` is >6 months old is treated as
**C until reproven**, regardless of stated tier.

## What does NOT belong here

- **Private/bespoke skills.** The whole model is: public generic skill → fork private →
  adapt. Your private fork is yours and stays out of the atlas.
- **Skills you haven't opened.** If you didn't read it, you can't tier it.
- **Affiliate-bait listicles dressed as skills.** Link the primary source, not the SEO page.
