# Module: Desktop app

> **⚠ NOT YET PROVEN.** This module has never been used on a real project. Its rules come from standard practice. `init` asks the human to confirm before using it, and the first project that uses it must review every rule and record corrections in `project/lessons.md`.

**Version:** 0.1
**Scope:** applications installed on a computer (Windows, macOS, Linux): native or built with a cross-platform shell (Electron, Tauri, Qt, .NET, JVM and similar; the choice is a decision of the plan). If the app talks to a server you build, also activate `backend`; if it embeds a browser UI built as a web app, parts of `web` (W2, W3, W4) apply to that UI.
**State:** **not yet proven** on any project. Written from standard practice; the first real project must review it and record what it changes.

## Rules (in addition to the constitution)

- **D1 – Platforms are scope.** The profile lists operating systems with minimum versions and processor architectures (for example Windows 10+ x64/ARM, macOS 13+ Intel/Apple silicon, named Linux distributions). Every feature is specified and verified for each item, or the exception is recorded.
- **D2 – Installation, update and removal are features.** The spec says how the app is installed, how it updates (automatic or manual, who is told, can the user postpone), how a failed update recovers, and what uninstalling removes and keeps. An update never loses user data.
- **D3 – Trust the operating system's rules.** Releases are code-signed (and notarised on macOS) with keys whose custody and backup the plan states; an unsigned build is never distributed to users. Keys and certificates never enter the repository.
- **D4 – Files and user data (C6).** The app stores its data where each system expects (not next to the executable), states what it stores, whether it is encrypted, how the user exports or deletes it, and what happens on a corrupted or newer-version data file. Opening, saving and dropping files states supported formats, size limits, and behaviour on unreadable files and on files changed elsewhere. File paths from outside are untrusted input.
- **D5 – Least privilege.** The app asks the operating system for the minimum permissions; any elevated privilege, background service, startup entry or system-wide change needs a requirement and a user choice. A cross-platform shell runs its UI with the strictest isolation the framework offers: no direct system access from content that can load external text or pages, strict content policy, and a short explicit list of operations the UI may request from the native side (for Electron: context isolation on, no Node integration in renderers, sandbox on, narrow preload interface; for Tauri: a minimal allow-list).
- **D6 – Local data migrations.** When a new version changes the local data format, there is a versioned migration, a backup made before it runs, and a defined behaviour when a user opens data from a newer version.
- **D7 – Windows, menus and keyboard.** Window state (size, position, monitor, maximised) is remembered and recovered if the monitor is gone. Menus, shortcuts, dialogs, drag and drop, copy and paste and the quit behaviour follow each platform's conventions unless the design says why not. Every action available by pointer is available by keyboard. State whether multiple windows or multiple instances are allowed; if not, a second launch focuses the first.
- **D8 – Accessibility (C7).** Screen readers of each platform can complete every flow; text and layout respond to system text size and zoom; system high-contrast and dark modes are honoured; keyboard focus is visible and ordered; contrast meets WCAG 2.2 AA; reduced motion is honoured.
- **D9 – Offline is the default.** The app states what works without a network, what needs one, and what it does when the connection drops mid-operation. Sync and conflict handling is a decision record when data is shared between devices.
- **D10 – Diagnostics respect privacy.** Logs are kept locally with rotation and a way for the user to export them; crash and usage reporting are **off until the user opts in**, say what they send, and never include personal data beyond what the profile allows (GDPR where it applies).
- **D11 – Resource use.** Start-up time, memory and idle processor use have targets from the spec; background work needs a requirement. Long operations are cancellable and never freeze the window.
- **D12 – Display and input variety.** The UI works on high-density and multiple displays, at the scaling factors listed in the profile, with mouse, keyboard and (if the spec says) touch or pen.
- **D13 – Distribution.** The channel (website, system store, package manager, enterprise deployment) is a decision; the plan covers each channel's rules (store review, installer format, per-user vs per-machine install) and how a user reports a problem.

## Typical quality gates (copy into `project/profile.md`, Section 6)
1. Lint and format, 2. type check or static analysis, 3. unit tests, 4. integration tests of storage and migrations (D4, D6) against real files, 5. UI tests of the critical flows on each operating system in D1 (CI runners or virtual machines), 6. a run of the installed, signed build on a real machine per platform before release (the human does it and reports), 7. accessibility checks (automated plus a manual screen-reader and keyboard pass), 8. update test (old version → new version keeps data), 9. dependency audit, 10. signed package built and verified.

## Checklists

**Specify.** Operating systems, versions, architectures (D1). Installation, update, uninstall (D2). Every kind of file and folder the app reads or writes (D4). Offline behaviour (D9). What persists between runs and what the user can export or delete. Windows, menus and shortcuts that matter (D7). Opt-in diagnostics (D10). Permissions or privileges needed and why (D5). Languages and accessibility (D8).

**Design.** Run the design playbook. Screens for the smallest supported window, large and multi-display windows, light, dark and high-contrast. Menu structure and keyboard shortcuts per platform; empty, loading, error and offline states.

**Plan.** Native or cross-platform shell with the reason and the isolation model (D5). Where state and data live, file formats, versioning and migrations (D4, D6). Update mechanism and its server (D2). Signing, notarisation and key custody (D3). Packaging per platform and distribution (D13). Process and thread model so the window never freezes (D11). Single-instance behaviour (D7). Logging and opt-in reporting (D10). How each mechanism is tested without the real operating system service (fakes), and what only a real machine can prove.

**Tasks.** Order: toolchain check, scaffolding that builds and launches an empty window on each OS, CI on each OS, text resources and design tokens, storage and migration skeleton, then one flow per task with tests. Developer certificates, accounts and update-server setup are "Requires human action" tasks placed before the first task that needs them. Packaging, signing, update test and the real-machine run come last.

## Typical open decisions
Operating systems and minimum versions, native or cross-platform shell, language, local storage format and encryption, update mechanism, distribution channel, signing and notarisation, single or multiple windows and instances, sync, crash and usage reporting, installer type, licensing.

## Proven and not yet proven
- **Proven:** nothing yet. The generic parts of the flow are proven on other modules.
- **Not yet proven:** every rule above; in particular D2, D3 and D13 (installers, signing, updates, which require human action and real machines) and the multi-OS test gate.
