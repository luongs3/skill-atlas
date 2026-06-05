# Job: Columnar Data (Apache Arrow)

**You're about to:** move data between tools fast with a shared columnar format.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Apache Arrow
The cross-language columnar memory format that lets Polars/DuckDB/Spark/pandas share data zero-copy.
- **source:** https://github.com/apache/arrow (docs: https://arrow.apache.org/docs)
- **reputation:** Official ASF · **16,810★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** a data toolchain
- **adapt:** none — it's the interchange layer under your other tools.

---

## How to use this job

You rarely program against **Arrow** directly — its value is as the zero-copy interchange layer beneath Polars, DuckDB, pandas (2.x), and Spark, so data crosses tool boundaries without serialize/deserialize round-trips. Reach for it explicitly when you're moving large columnar data between processes or languages (Arrow IPC/Flight), or building a library that wants to hand data to that whole ecosystem cheaply. The decision hinges on whether interop/zero-copy is the bottleneck; for in-process single-tool work, just use the tool's native frame and let Arrow do its job underneath.

## Pitfalls

- **"Zero-copy" only holds within compatible memory.** The moment you cross a process or language boundary without Arrow IPC/Flight — or convert to pandas with a type Arrow can't map (e.g. object dtypes) — you pay a full copy and conversion cost. Keep data in Arrow buffers end-to-end to actually get the benefit.
- **Arrow ≠ Parquet, and versions matter.** Arrow is the in-memory format; Parquet is the on-disk format Arrow reads/writes. Mixing libraries built against incompatible Arrow C++ ABI versions (common via pyarrow + another wheel) causes segfaults or silent corruption. Pin compatible versions.
- **Type and null semantics differ subtly across tools.** Timestamps with/without timezone, decimal precision, and nested types don't always survive a hop between pandas/Polars/Spark cleanly. Validate schemas at boundaries rather than assuming a clean round-trip.

*Foundational plumbing under [dataframes-polars-duckdb](dataframes-polars-duckdb.md) and [data-engineering](data-engineering.md). You rarely use it directly, but knowing it explains why those tools interop. Private skill = where Arrow sits in your pipeline.*
