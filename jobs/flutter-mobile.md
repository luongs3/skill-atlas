# Job: Flutter (Mobile)

**You're about to:** build a cross-platform app with Flutter + Dart — widgets, state, layout.

> Reputation pulled live **2026-06-05** via `gh api`.

---

## Tier A 🟢 — Canonical

### Flutter + docs
Google's cross-platform UI toolkit — one Dart codebase to iOS/Android/web/desktop.
- **source:** https://github.com/flutter/flutter (docs: https://docs.flutter.dev)
- **reputation:** Official Google · **176,648★** · pushed 2026-06-05
- **last_validated:** 2026-06-05
- **assumes:** Flutter SDK
- **adapt:** fork your widget + state-management (Riverpod/Bloc) conventions.

---

## How to use this job

Reach for **Flutter** when you want one Dart codebase rendering its own pixels across iOS/Android (and web/desktop) with a consistent look and near-native performance. The biggest early decision is state management: use `setState`/`InheritedWidget` for trivial local state, and adopt **Riverpod** (compile-safe, testable) or **Bloc** (event-driven, good for complex flows) once state crosses screens — the choice hinges on team familiarity and how much you value compile-time safety vs. explicit event modeling. Commit to one and apply it consistently.

## Pitfalls

- **`setState` rebuilds the whole subtree.** Calling it high in the tree rebuilds everything below every frame, tanking performance. Push state down to the smallest widget that needs it, and use `const` constructors so unchanged widgets are skipped.
- **`BuildContext` used across async gaps.** After an `await`, the widget may be unmounted; touching `context` (for navigation/`Theme.of`) then throws or no-ops. Guard with `if (!mounted) return;` before using context post-await.
- **Platform parity isn't free.** Permissions, deep links, push notifications, and background tasks all need per-platform native config (Info.plist / AndroidManifest); "write once" doesn't mean "configure once". Test on real iOS and Android devices, not just one.

*See [mobile-development](mobile-development.md) for the overview. The private skill is your state-management choice + widget conventions, which an LLM can't infer.*
