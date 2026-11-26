# Apple Platform Source Map

Verified on 2026-11-26 against Xcode 27.2 (build 27B52) and the Xcode MCP server `xcode-tools` version 25464.

## Source hierarchy

1. The public SDK and Xcode build result for the declared deployment target.
2. Apple Developer Documentation and Human Interface Guidelines at `developer.apple.com`.
3. Apple's current policy and legal pages for App Store review, privacy, licensing, and distribution.
4. Apple-authored Xcode skills for framework-specific implementation guidance.
5. Project source, build settings, and tests.

The first four are authoritative sources; this skill is only a routing and evidence aid.

## Official entry points

| Purpose | URL |
| --- | --- |
| Developer documentation home | https://developer.apple.com/documentation/ |
| macOS technology overview | https://developer.apple.com/macos/ |
| AppKit | https://developer.apple.com/documentation/appkit |
| SwiftUI | https://developer.apple.com/documentation/swiftui |
| Foundation | https://developer.apple.com/documentation/foundation |
| Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ |
| Designing for macOS | https://developer.apple.com/design/human-interface-guidelines/designing-for-macos |
| Xcode documentation | https://developer.apple.com/documentation/xcode |
| Xcode MCP setup | https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode |
| App Store Review Guidelines | https://developer.apple.com/app-store/review/guidelines/ |
| App Sandbox | https://developer.apple.com/documentation/security/app-sandbox |
| Hardened Runtime | https://developer.apple.com/documentation/security/hardened-runtime |
| Code Signing Services | https://developer.apple.com/documentation/security/code-signing-services |
| Notarizing macOS software | https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution |
| Distributing an app | https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases |
| Accessibility | https://developer.apple.com/accessibility/ |
| Privacy | https://developer.apple.com/privacy/ |
| Swift language book | https://docs.swift.org/swift-book/ |

## Markdown representation

Apple's documentation and HIG pages expose a Markdown representation by appending `.md` to the page path. For example:

```text
https://developer.apple.com/documentation/AppKit/NSVisualEffectView.md
https://developer.apple.com/design/human-interface-guidelines/the-menu-bar.md
https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode.md
```

The local helper validates the host, appends `.md`, follows the official response, and prints Markdown. It does not scrape mirrors:

```bash
python3 '<apple-platform-guidance>/scripts/apple_docs.py' fetch 'https://developer.apple.com/documentation/AppKit/NSVisualEffectView'
```

Static pages such as the App Store Review Guidelines may not expose Markdown. Read the official page and cite the original URL.

## Xcode MCP

Apple documents the configuration command as:

```bash
codex mcp add xcode -- xcrun mcpbridge
```

In Xcode, choose **Xcode > Settings > Intelligence** and set **Allow External Agents to Use Xcode Tools** to **While Xcode is Open** (or **Always** only when the task requires it).

Inspection:

```bash
codex mcp list
```

The MCP server exposed these relevant capabilities in the verified environment:

- `DocumentationSearch`: semantic search across Apple documentation and HIG content, with framework filters.
- workspace/project inspection, build, test, diagnostics, and run-destination tools;
- simulator/device interaction tools.

The server connects to a running Xcode instance. Open the target project in Xcode before using project-scoped tools. Xcode may require the external agent to be approved for that workspace. `DocumentationSearch` returns `uri` values relative to `developer.apple.com`.

Do not set "Always" or broaden Xcode's external-agent permission unless the user's task actually requires it. The normal setup is to allow while Xcode is open.

## Xcode-provided skills

Xcode 27.2 exported these Apple-authored skills:

```text
adopt-c-bounds-safety
app-intents-specialist
app-intents-whats-new-27
app-resizability
audit-xcode-security-settings
building-document-based-swiftui-applications
device-interaction
modernize-tests
swiftui-specialist
swiftui-whats-new-27
xctrace
```

On this host they are installed under `$HOME/.agents/skills/<name>`. Verify one with:

```bash
test -f "$HOME/.agents/skills/swiftui-specialist/SKILL.md"
```

Refresh them from the installed Xcode rather than copying cached pages:

```bash
xcrun agent skills export --output-dir "$HOME/.agents/skills" --replace-existing
```

Read a skill's own `SKILL.md` before using it. The descriptions contain the actual trigger and scope; the table in the main skill is only routing.

## Search and citation discipline

- Search by API type, symbol, task, or HIG component; include the framework when known.
- Read the document containing the declaration or rule, not a snippet from the search result alone.
- For availability, read the SDK availability annotation and compare it with the declared deployment target.
- Record the official URL and the date observed in the implementation note or final evidence.
- If an official page changes, prefer the current page and state the observed version. Do not silently preserve an old API as current.
