---
name: apple-platform-guidance
description: Use when designing, implementing, reviewing, debugging, building, signing, distributing, or testing macOS or other Apple-platform software. Requires current Apple documentation and Xcode/SDK facts instead of memory for APIs, availability, HIG, App Store rules, entitlements, or Xcode behavior.
metadata:
  revision: "2026-11-26"
  short-description: Apple 官方文档与 Xcode 开发入口
---

# Apple Platform Guidance

This skill adds Apple-platform facts and sources to GSE. GSE still owns the outcome, implementation discipline, evidence, and delivery; this skill does not grant extra permissions or replace project rules.

## 1. Pin the actual Apple target

Before proposing an API, UI pattern, entitlement, or distribution step, read the project rather than assuming from the current Mac:

- platform and deployment target, especially the macOS minimum;
- Xcode and SDK versions (`xcodebuild -version`, `xcrun --show-sdk-version --sdk macosx`);
- UI stack and runtime (SwiftUI, AppKit, Mac Catalyst, iOS app on Apple silicon, or a mix);
- build configuration, dependencies, architecture, signing identity, sandbox, entitlements, and privacy manifest;
- distribution path (App Store, Developer ID with notarization, internal, or development-only).

An iOS result, a Mac Catalyst result, and a native macOS result are different evidence. If a target fact is absent and cannot be inferred safely, state the exact gap instead of guessing.

## 2. Use current Apple sources

For API signatures and availability, platform behavior, Human Interface Guidelines, Xcode behavior, security, privacy, signing, notarization, and App Store policy:

1. Use Xcode MCP `DocumentationSearch` when the `xcode` server is configured, Xcode is open, and this agent is approved for an Xcode workspace. Search narrowly and pass the framework when known. Treat the returned `uri` as the path to the authoritative page.
2. For an exact API, article, or HIG page, run:

   ```bash
   python3 '<apple-platform-guidance>/scripts/apple_docs.py' fetch 'https://developer.apple.com/documentation/AppKit/NSVisualEffectView'
   ```

   Run the helper from this skill's directory, or replace `<apple-platform-guidance>` with its installed path. It requires an Apple `developer.apple.com` URL and uses Apple's official Markdown representation where available.
3. Read static policy pages directly, such as the App Store Review Guidelines and Apple Developer Program License Agreement. They are not always present in `DocumentationSearch` or the Markdown endpoint.
4. Load Apple's exported Xcode skills when their topic is in play; see the routing table below.

Do not use a blog, mirror, generated summary, or model memory to invent an API name, signature, availability floor, default, HIG rule, entitlement, privacy requirement, or review policy. If sources conflict, prefer the current SDK and the current official page, record their versions, and surface the conflict.

The source map and verified URLs are in [references/sources.md](references/sources.md).

## 3. Apply macOS-specific checks

- Check availability and deprecation against the deployment target, not only the newest SDK.
- Use native macOS conventions for menus, windows, focus, keyboard commands, pointer behavior, multiple displays, appearance, accessibility, localization, and document lifecycle.
- Treat sandboxing, hardened runtime, code signing, notarization, entitlements, usage descriptions, and least-privilege permissions as part of the product contract.
- Separate App Store requirements from direct-distribution requirements; one does not prove the other.
- Prefer public APIs. A capability reachable only through private or underscore-prefixed API is not an acceptable implementation shortcut.
- Measure performance with an appropriate Apple tool and a reproducible workload; a build or a screenshot is not performance evidence.

## 4. Build and verify with the right layer

- Use the Xcode MCP server for workspace inspection, build, diagnostics, tests, and simulator/device interaction when it is available. Otherwise use the project's declared `xcodebuild` or Swift Package Manager command.
- Use the Apple-provided `xctrace` skill for profiling, `modernize-tests` for test migration, and `device-interaction` only for UI verification on a simulator or device.
- Do not use XCTest or XCUITest to launch, activate, or manipulate this Mac's product windows. Follow the host's GUI rules and the project's real acceptance entry.
- Record the deployment target, Xcode/SDK, source URL and access date, build/test command and result, runtime entry, and any unverified item. A successful build is not a release, and a release is not user acceptance.

## 5. Apple-provided Xcode skills

When installed in the active skill root, load only the skill that matches the current problem:

| Topic | Skill |
| --- | --- |
| SwiftUI correctness, data flow, identity, performance | `swiftui-specialist` |
| New SwiftUI 27 APIs and migrations | `swiftui-whats-new-27` |
| Document-based SwiftUI apps and migration | `building-document-based-swiftui-applications` |
| App Intents and current App Intents migrations | `app-intents-specialist`, `app-intents-whats-new-27` |
| XCTest to Swift Testing migration | `modernize-tests` |
| Profiling and hang triage | `xctrace` |
| Xcode security settings and C bounds safety | `audit-xcode-security-settings`, `adopt-c-bounds-safety` |
| App layout and resizability | `app-resizability` |
| Simulator/device UI verification | `device-interaction` |

These skills are exported from Xcode and can be refreshed with:

```bash
xcrun agent skills export --output-dir "$HOME/.agents/skills" --replace-existing
```

They are Apple-authored local guidance, not files to copy into a public repository.

## 6. Degraded paths

- If Xcode MCP is unavailable but Apple documentation is reachable, continue with the official pages and mark the MCP path unverified.
- If a documentation page is inaccessible, report the exact URL and response. Do not replace it with a third-party copy and call it official.
- If an Apple-provided Xcode skill is not installed, say which skill is missing and continue with the official documentation; do not recreate its detailed rules from memory.
- If the project is not an Apple-platform project, do not activate this skill merely because Xcode is installed.
