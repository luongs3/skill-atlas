#!/usr/bin/env python3
"""Regenerate the README 'Index of jobs' table from all jobs/*.md files.

Title  := the '# Job: <title>' line.
Lead tier := the first '## Tier X' header in the file.
Sorted by display title (case-insensitive), matching the existing table's ordering.
Splices ONLY the table block + the count blurb; leaves all prose untouched.
"""
import os, re, glob

REPO = os.path.expanduser("~/Developer/skill-atlas")
JOBS = os.path.join(REPO, "jobs")
README = os.path.join(REPO, "README.md")

TIER_EMOJI = {"A": "🟢 A", "B": "🔵 B", "C": "🟡 C", "D": "🔴 D"}
title_re = re.compile(r"^#\s*Job:\s*(.+?)\s*$", re.M)
tier_re = re.compile(r"^##\s*Tier\s+([ABCD])\b", re.M)

rows = []
for path in glob.glob(os.path.join(JOBS, "*.md")):
    fn = os.path.basename(path)
    txt = open(path).read()
    tm = title_re.search(txt)
    title = tm.group(1) if tm else fn[:-3]
    lm = tier_re.search(txt)
    lead = lm.group(1) if lm else "C"
    rows.append((title, lead, fn))

rows.sort(key=lambda r: r[0].lower())

table = ["| Job | Best tier | File |", "|-----|-----------|------|"]
for title, lead, fn in rows:
    table.append(f"| {title} | {TIER_EMOJI[lead]} | [`{fn}`](jobs/{fn}) |")
table_str = "\n".join(table)

n_jobs = len(rows)
n_entries = sum(open(p).read().count("\n### ") + open(p).read().startswith("### ")
                for p in glob.glob(os.path.join(JOBS, "*.md")))
# robust entry count
n_entries = 0
for p in glob.glob(os.path.join(JOBS, "*.md")):
    n_entries += len([l for l in open(p).read().split("\n") if l.startswith("### ")])

blurb = (f"_{n_jobs} jobs, {n_entries} skill entries — every GitHub source live-verified via "
         f"`gh api` (2026-06-19 or newer). Tier shown is the lead tier; open a job for the "
         f"full tiered list._")

readme = open(README).read()
lines = readme.split("\n")

# find the blurb line (the italic _NNN jobs...) and the table region
# table starts at '| Job | Best tier | File |' and runs through the last '| ... |' line
start = next(i for i, l in enumerate(lines) if l.startswith("| Job | Best tier"))
end = start
for i in range(start, len(lines)):
    if lines[i].startswith("|"):
        end = i
    else:
        break

# blurb is the nearest italic line above start beginning with '_' and containing 'jobs'
blurb_idx = None
for i in range(start - 1, -1, -1):
    if lines[i].strip().startswith("_") and "jobs" in lines[i]:
        blurb_idx = i
        break

new_lines = lines[:start] + table_str.split("\n") + lines[end + 1:]
if blurb_idx is not None:
    new_lines[blurb_idx] = blurb

open(README, "w").write("\n".join(new_lines))
print(f"README updated: {n_jobs} jobs, {n_entries} entries, table rows={len(rows)}")
