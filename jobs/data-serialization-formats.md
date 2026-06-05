# Job: Data Serialization & Query

**You're about to:** work with JSON/YAML on the CLI and pick the right data format.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### jq
The standard command-line JSON processor — filter, transform, query JSON.
- **source:** https://github.com/jqlang/jq (docs: https://jqlang.org/manual)
- **reputation:** **34,813★** · pushed 2026-06-01
- **last_validated:** 2026-06-05
- **assumes:** a shell
- **adapt:** fork your common jq filters as aliases.

### yq
jq-style processor for YAML (and XML/TOML).
- **source:** https://github.com/mikefarah/yq
- **reputation:** **15,480★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** a shell
- **adapt:** none — reference.

---

## How to use this job

Use **jq** for anything JSON and **yq** for YAML/XML/TOML — yq deliberately mirrors jq's filter syntax, so one mental model covers both. The decision is just the input format: reach for yq even on JSON only if you're already in a YAML pipeline and want one tool. For schema'd binary formats (Protobuf, Avro) these don't apply — see the linked job.

## Pitfalls

- **jq numbers are IEEE-754 doubles** — large 64-bit integers (IDs, timestamps in nanoseconds) lose precision silently. Use `tostring`/`tonumber` carefully or keep big IDs as strings end-to-end.
- **yq has two incompatible major tools with the same name** — mikefarah/yq (Go, the one here) vs the Python `yq` wrapper around jq. Filters written for one won't run on the other; pin which binary your scripts assume.
- **yq does not round-trip YAML losslessly by default** — comments, anchors, and key ordering can be dropped or rewritten on edit. Use `-I` indent flags and verify diffs before committing machine-edited YAML.

---

*These show up in every CI script and debugging session. Private skill = your library of common jq/yq filters. See [linux-shell](linux-shell.md) and [protobuf-grpc-schemas](protobuf-grpc-schemas.md) for binary formats.*
