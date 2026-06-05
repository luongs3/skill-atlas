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

*See [api-design](api-design.md). The private skill is your org's proto conventions (package naming, field-numbering rules, breaking-change policy).*
