# Job: React Native (Mobile)

**You're about to:** build a cross-platform mobile app with React Native + Expo.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### React Native + docs
Meta's cross-platform framework — reuse React knowledge for iOS/Android.
- **source:** https://github.com/facebook/react-native (docs: https://reactnative.dev)
- **reputation:** Official Meta · **125,960★** · pushed 2026-06-04
- **last_validated:** 2026-06-05
- **assumes:** React/JS toolchain
- **adapt:** fork your navigation + state conventions.

### Expo
The batteries-included RN toolchain — build, OTA updates, native APIs without Xcode wrangling.
- **source:** https://github.com/expo/expo (docs: https://docs.expo.dev)
- **reputation:** Official Expo · **49,879★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** Node
- **adapt:** fork your EAS build/submit config.

---

## How to use this job

Start with **Expo** unless you have a hard reason not to — the managed workflow + EAS Build give you OTA updates, native APIs, and CI builds without touching Xcode/Gradle directly, and config plugins now cover most native needs. Drop to bare **React Native** only when you need a native module Expo can't wrap or fine-grained build control; the decision hinges on whether your native dependency set fits Expo's plugin model.

## Pitfalls

- **Native module / version mismatches:** a native lib built against a different RN version (or expecting an old/new architecture) crashes at startup with cryptic linker errors. Match each native dependency to your RN version and rebuild the dev client after adding one — JS-only reloads won't pick up native changes.
- **JS engine vs JSC behavior:** the default RN engine differs from JSC in `Date`/`Intl`, regex, and `console` timing; code that works in a JSC debug build can misbehave in a release build. Test on the real engine, not just the JS debugger.
- **Debugger ≠ device runtime:** running JS in Chrome/remote debug uses V8, not the on-device engine, masking timing bugs. New Architecture (Fabric/TurboModules) also changes threading assumptions — verify on a release build.

---

*See [mobile-development](mobile-development.md) for the cross-framework picture and [react-development](react-development.md) for the React layer. Private skill = your app's nav + build pipeline.*
