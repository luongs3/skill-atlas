# Job: Java Development

**You're about to:** write Java — idiomatic code, the JDK toolchain, and the dominant application framework.
All canonical official sources.

> Reputation pulled live **2026-06-04** via `gh api`.

---

## Tier A 🟢 — Canonical

### OpenJDK + official docs
The reference implementation of the Java SE platform and the official API/language specifications.
The source of truth for the standard library, the Java Language Specification (JLS), and JVM behavior.
- **source:** https://github.com/openjdk/jdk (docs: https://docs.oracle.com/en/java)
- **reputation:** The OpenJDK project · **22,943★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** a JDK installed
- **adapt:** none — reference. Pin your LTS version (e.g. 17/21) per project and match it in CI.

---

## Tier B 🔵 — Community-proven (framework)

### Spring Boot
The de-facto framework for Java backend and web services — autoconfiguration, starters, embedded servers,
and a vast ecosystem; the standard application baseline most enterprise Java teams build on.
- **source:** https://github.com/spring-projects/spring-boot
- **reputation:** spring-projects org · **80,769★** · pushed 2026-06-04
- **last_validated:** 2026-06-04
- **assumes:** a JDK + build tool (Maven/Gradle)
- **adapt:** fork your team's starter set, `application.yml` profiles, and dependency-management BOM into a private baseline. Codify which starters are blessed vs forbidden, and your logging/observability defaults.

---

*Substitution-resistant private skill: your build conventions (Maven vs Gradle, multi-module layout),
your dependency BOM and version catalog, and your CI's checkstyle/spotbugs/jacoco gates. An LLM writes
Java fine; it doesn't know your repo's rules — its package structure, its blessed libraries, or its
release/versioning policy.*
