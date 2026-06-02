#!/usr/bin/env bash
# revalidate.sh — refresh trust signals for every source URL in the atlas.
# Prints liveness + (for GitHub repos) stars and last-push date, so a maintainer can
# bump last_validated dates or downgrade rotted entries.
#
# Usage: scripts/revalidate.sh
# Requires: curl, python3

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

echo "Skill Atlas revalidation — $(date -u +%Y-%m-%dT%H:%MZ)"
echo "================================================================"

# Pull every http(s) URL out of the job files.
urls=$(grep -rhoE 'https?://[^ )]+' jobs/ 2>/dev/null | sed 's/[.,)]*$//' | sort -u)

while IFS= read -r url; do
  [ -z "$url" ] && continue
  code=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 12 "$url")

  # GitHub repo? fetch stars + last push.
  if [[ "$url" =~ github\.com/([^/]+)/([^/#]+) ]]; then
    repo="${BASH_REMATCH[1]}/${BASH_REMATCH[2]}"
    # Prefer `gh api` (authenticated, 5000 req/hr). Fall back to anonymous curl (60/hr).
    if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
      meta=$(gh api "repos/$repo" \
        --jq '"\(.stargazers_count)★ pushed \(.pushed_at[:10])"' 2>/dev/null)
    else
      meta=$(curl -s --max-time 12 "https://api.github.com/repos/$repo" \
        | python3 -c "import sys,json
try:
    d=json.load(sys.stdin); print(f\"{d.get('stargazers_count','?')}\u2605 pushed {str(d.get('pushed_at',''))[:10]} (anon — set up gh for full data)\")
except Exception: print('(rate-limited — run: gh auth login)')" 2>/dev/null)
    fi
    printf '%s  %-55s %s\n' "$code" "$url" "$meta"
  else
    printf '%s  %s\n' "$code" "$url"
  fi
done <<< "$urls"

echo "================================================================"
echo "Review: any non-200, or any GitHub repo not pushed in >3mo, should be"
echo "re-tiered. Bump last_validated only for entries you actually re-checked."
