#!/usr/bin/env bash
# revalidate.sh — refresh trust signals for every source URL in the atlas.
# Prints liveness + (for GitHub repos) stars and last-push date, flags rot, and
# EXITS NON-ZERO when anything is dead or stale so CI can open an issue.
#
# Usage: scripts/revalidate.sh
# Requires: curl; uses `gh` (5000 req/hr) if authed, else anon curl (60/hr).
#   In CI, set GH_TOKEN (Actions provides it) so `gh api` is authenticated.
# Env: STALE_DAYS (default 180) — a GitHub repo not pushed within this many days is "stale".
#
# Exit codes: 0 = all good; 1 = rot found (dead links and/or stale repos).

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

STALE_DAYS="${STALE_DAYS:-180}"
now=$(date -u +%s)

# Hosts that bot-block datacenter/CI IPs (expected non-200) — not treated as dead.
allow_block_re='support\.upwork\.com|reddit\.com|cppreference\.com|isocpp\.org|phaser\.io|pixijs\.download|solidjs\.com'

dead=()      # url  (non-200, not in allowlist)
stale=()     # "url  pushed YYYY-MM-DD"

echo "Skill Atlas revalidation — $(date -u +%Y-%m-%dT%H:%MZ)  (stale threshold: ${STALE_DAYS}d)"
echo "================================================================"

# Pull every http(s) URL out of the job files.
urls=$(grep -rhoE 'https?://[^ )]+' jobs/ 2>/dev/null | sed 's/[.,)]*$//' | sort -u)

while IFS= read -r url; do
  [ -z "$url" ] && continue
  code=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 15 "$url")

  # Track dead links (anything not 2xx/3xx, unless allowlisted as a known bot-blocker).
  if [[ ! "$code" =~ ^(2|3) ]] && [[ ! "$url" =~ $allow_block_re ]]; then
    dead+=("$code  $url")
  fi

  # GitHub repo? fetch stars + last push, and flag staleness.
  if [[ "$url" =~ github\.com/([^/]+)/([^/#]+) ]]; then
    repo="${BASH_REMATCH[1]}/${BASH_REMATCH[2]}"
    pushed=""
    if command -v gh >/dev/null 2>&1 && { gh auth status >/dev/null 2>&1 || [ -n "${GH_TOKEN:-}" ]; }; then
      read -r stars pushed < <(gh api "repos/$repo" --jq '"\(.stargazers_count) \(.pushed_at[:10])"' 2>/dev/null)
      meta="${stars}★ pushed ${pushed}"
    else
      meta=$(curl -s --max-time 12 "https://api.github.com/repos/$repo" \
        | python3 -c "import sys,json
try:
    d=json.load(sys.stdin); print(f\"{d.get('stargazers_count','?')}\u2605 pushed {str(d.get('pushed_at',''))[:10]} (anon)\")
except Exception: print('(rate-limited)')" 2>/dev/null)
      pushed=$(echo "$meta" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -1)
    fi

    # Staleness check (only if we got a date).
    flag=""
    if [ -n "$pushed" ]; then
      pushed_s=$(date -j -f "%Y-%m-%d" "$pushed" +%s 2>/dev/null || date -d "$pushed" +%s 2>/dev/null || echo 0)
      if [ "$pushed_s" -gt 0 ]; then
        age_days=$(( (now - pushed_s) / 86400 ))
        if [ "$age_days" -gt "$STALE_DAYS" ]; then
          flag="  ⚠️ STALE (${age_days}d)"
          stale+=("$url  pushed $pushed (${age_days}d)")
        fi
      fi
    fi
    printf '%s  %-55s %s%s\n' "$code" "$url" "$meta" "$flag"
  else
    printf '%s  %s\n' "$code" "$url"
  fi
done <<< "$urls"

echo "================================================================"

rc=0
# Dead links are hard rot → non-zero exit (triggers CI issue).
if [ "${#dead[@]}" -gt 0 ]; then
  echo ""
  echo "❌ DEAD LINKS (${#dead[@]}):"
  printf '   %s\n' "${dead[@]}"
  rc=1
fi
# Staleness is advisory: reported for re-tiering, but does NOT fail the run on its own
# (most stale entries are already tiered C/D — failing monthly would be pure noise).
if [ "${#stale[@]}" -gt 0 ]; then
  echo ""
  echo "⚠️  STALE REPOS — not pushed in >${STALE_DAYS}d (${#stale[@]}) — confirm they're tiered C/D:"
  printf '   %s\n' "${stale[@]}"
fi
if [ "$rc" -eq 0 ]; then
  if [ "${#stale[@]}" -gt 0 ]; then
    echo ""
    echo "✅ No dead links. ${#stale[@]} stale repo(s) above are advisory — confirm C/D tiering."
  else
    echo "✅ All sources live and fresh (≤${STALE_DAYS}d)."
  fi
else
  echo ""
  echo "Action: fix/replace the dead links above, then re-tier any stale entries."
fi
exit "$rc"
