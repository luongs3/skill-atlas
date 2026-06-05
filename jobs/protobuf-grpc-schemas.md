# Job: Protobuf & gRPC Schemas

**You're about to:** define service schemas and message types with Protocol Buffers + gRPC.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Protocol Buffers
The schema language + codegen for typed, versioned messages across languages.
- **source:** https://github.com/protocolbuffers/protobuf (docs: https://protobuf.dev)
- **reputation:** Official Google · **71,320★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** protoc or buf
- **adapt:** fork your proto style + versioning rules.

### gRPC
The RPC framework that uses protobuf for service-to-service calls.
- **source:** https://github.com/grpc/grpc (docs: https://grpc.io/docs)
- **reputation:** Official · **44,858★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** protobuf
- **adapt:** see [api-design](api-design.md) for the design layer.

---

## How to use this job

Treat **Protocol Buffers** as the schema/contract layer and **gRPC** as the transport that consumes it — you almost always adopt both together, defining messages and services in `.proto` files and generating typed stubs per language. The real decision is tooling: use `buf` over raw `protoc` for linting, breaking-change detection, and remote codegen; reach for gRPC-Gateway or Connect when you also need a REST/JSON edge.

## Pitfalls

- **Never reuse or renumber field tags:** wire format is keyed on field numbers, not names. Reusing a retired tag for a new field silently corrupts data for old clients. `reserve` removed numbers and names so they can't be reassigned.
- **`required` is gone, and proto3 defaults hide:** in proto3 scalar fields default to zero/empty and (historically) couldn't distinguish "unset" from "zero" — use `optional` or wrapper types when presence matters, or you'll mistake a real `0` for missing.
- **Breaking changes sneak through codegen:** changing a field type, renaming an enum value's number, or moving a field into/out of `oneof` breaks wire or API compat even when codegen succeeds. Gate every `.proto` change with `buf breaking` against the published schema.

---

*See [api-design](api-design.md). The private skill is your org's proto conventions (package naming, field-numbering rules, breaking-change policy).*
