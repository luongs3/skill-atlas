# Job: C# / .NET Development

**You're about to:** write C# — idiomatic code, the .NET runtime, and the standard web framework.
All canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### .NET runtime + official docs
The reference runtime, base class libraries, and the official .NET/C# documentation — the source of truth
for the language spec, BCL APIs, and the SDK toolchain.
- **source:** https://github.com/dotnet/runtime (docs: https://learn.microsoft.com/dotnet)
- **reputation:** Microsoft / dotnet org · **17,924★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** .NET SDK installed
- **adapt:** none — reference. Pin your target framework (e.g. net8.0) per project.

### ASP.NET Core
The official web framework for .NET — minimal APIs, MVC, Blazor; the standard baseline for backend/web
services and the canonical source for middleware, routing, and DI patterns.
- **source:** https://github.com/dotnet/aspnetcore (docs: https://learn.microsoft.com/dotnet)
- **reputation:** Microsoft / dotnet org · **37,962★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** .NET SDK installed
- **adapt:** fork your team's middleware pipeline + DI registration + configuration conventions into a private baseline.

---

## Tier B 🔵 — Community-proven

*None pinned — the official Microsoft sources above cover the runtime, language, and web framework.
Reach for community libraries only after checking the canonical docs.*

---

*Substitution-resistant private skill: your solution layout (project references, `.editorconfig` style
rules), your NuGet feed and package-version conventions, and your CI's analyzer/format gates. An LLM
writes C# fine; it doesn't know your repo's rules.*
