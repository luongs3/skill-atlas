# Job: Mobile Development

**You're about to:** build a mobile app — cross-platform or native iOS/Android. All
canonical official sources, very high reputation.

> Reputation pulled live **2026-06-03** via `gh api`.

---

## Tier A 🟢 — Canonical (official framework sources)

### Flutter — cross-platform (Dart)
Google's cross-platform UI toolkit; one codebase → iOS, Android, web, desktop.
- **source:** https://github.com/flutter/flutter (docs: https://docs.flutter.dev)
- **reputation:** Official Google · **176,630★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** Flutter SDK
- **adapt:** fork your widget/state-management conventions (Riverpod/Bloc) into a private skill.

### React Native — cross-platform (JS/TS)
Meta's cross-platform framework; leverage React knowledge for mobile.
- **source:** https://github.com/facebook/react-native (docs: https://reactnative.dev)
- **reputation:** Official Meta · **125,943★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **assumes:** React/JS toolchain
- **adapt:** none — reference.

### Swift — native iOS
Apple's language for native iOS/macOS.
- **source:** https://github.com/apple/swift (docs: https://developer.apple.com/documentation)
- **reputation:** Official Apple · **70,014★** · pushed 2026-06-03
- **last_validated:** 2026-06-03
- **assumes:** Xcode / macOS
- **adapt:** none — reference.

### Now in Android — native Android reference app
Google's official, fully-modern Android sample app — the canonical "how should an Android
app be structured" reference (Compose, architecture, modularization).
- **source:** https://github.com/android/nowinandroid
- **reputation:** Official Google · **21,313★** · pushed 2026-06-02
- **last_validated:** 2026-06-03
- **assumes:** Android Studio / Kotlin
- **adapt:** copy the architecture patterns; it's a teaching reference.

---

*For a backend eng who needs a mobile client: **Flutter** or **React Native** (reuse your
JS) gets you cross-platform fastest. Go native only when you need platform-specific APIs or
peak performance. Encode your choice + conventions in a private skill.*
