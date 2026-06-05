# Job: Kotlin Development

**You're about to:** write Kotlin — idiomatic code, the official toolchain, and Android pairing.
All canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### Kotlin compiler + official docs
The reference compiler and the official language/standard-library documentation — coroutines, null safety,
multiplatform (KMP), and the idiom/style guides every Kotlin codebase references.
- **source:** https://github.com/JetBrains/kotlin (docs: https://kotlinlang.org/docs)
- **reputation:** JetBrains · **52,802★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** Kotlin toolchain installed (Gradle/kotlinc)
- **adapt:** none — reference. Pin your Kotlin + Gradle plugin versions per project and match them in CI.

---

## Tier B 🔵 — Community-proven (Android)

### Now in Android
For Android development, pair Kotlin with Google's official sample app demonstrating modern architecture
(Jetpack Compose, modularization, idiomatic coroutines/Flow). Cross-reference
[mobile-development](mobile-development.md) for the full Android stack and its reputation data.
- **source:** see [mobile-development](mobile-development.md) (Now-in-Android)
- **reputation:** Google official sample · maintained
- **last_validated:** 2026-06-04
- **assumes:** Android SDK + Gradle
- **adapt:** fork your app's module boundaries + architecture conventions (MVVM/MVI, DI framework — Hilt/Koin) into a private guide.

---

*Substitution-resistant private skill: your project's Gradle conventions (KMP vs JVM-only, coroutine
scope/dispatcher policy), and your CI's detekt/ktlint gates. An LLM writes Kotlin fine; it doesn't know
your repo's rules — its module graph, its blessed libraries, or its release/versioning policy.*
