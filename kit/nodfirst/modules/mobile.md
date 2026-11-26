# Module: Mobile app

> **⚠ NOT YET PROVEN.** This module has never been used on a real project. Its rules come from standard practice. `init` asks the human to confirm before using it, and the first project that uses it must review every rule and record corrections in `project/lessons.md`.

**Version:** 0.1
**Scope:** apps installed on phones and tablets: native (iOS, Android) or cross-platform (the framework is a decision of the plan, never assumed). If the app talks to a server you build, also activate `backend`.
**State:** **not yet proven** on any project. Written from standard practice and the stores' published requirements; the first real project must review it and record what it changes.

## Rules (in addition to the constitution)

- **M1 – Platforms and versions are scope.** The profile lists the platforms (iOS, Android, both), the minimum OS version for each, the device classes (phone, tablet, foldable) and orientations. A feature is specified, built and verified for every item on that list, or the exception is recorded.
- **M2 – Permissions are earned.** Every permission (camera, location, notifications, contacts, photos, microphone, tracking) has a reason in the spec, is requested at the moment it is needed with an explanation first, and **the app has a defined behaviour when it is denied, or later revoked.** Ask only for what a requirement needs (C8).
- **M3 – Lifecycle is part of the behaviour.** The app can be interrupted at any time: backgrounded, killed by the system, rotated, interrupted by a call, resumed after days. The spec says what is kept, what is restored, and what is lost. Work in progress is never silently lost.
- **M4 – Connectivity is unreliable.** Each flow states what it does with no network, a slow network and a network that drops mid-operation, and how the user sees it. Offline and sync strategy is a decision record before any plan that depends on it; conflicts have a rule.
- **M5 – Local data and secrets (C6).** Credentials and tokens live in the platform's secure storage (Keychain, Keystore or equivalent), never in plain files or preferences. The plan lists what is stored on the device, what is encrypted, what is wiped at sign-out, and what is excluded from device backups. Nothing sensitive in logs, screenshots of the app switcher, or the clipboard unless the spec says so.
- **M6 – Accessibility (C7).** Screen readers (VoiceOver, TalkBack) can complete every flow; text follows the system's text size and the layout survives the largest size; touch targets meet the platform minimum (44×44 pt on iOS, 48×48 dp on Android); contrast meets WCAG 2.2 AA; no information by colour alone; reduced motion is honoured; every control has a label.
- **M7 – Platform conventions.** Navigation, back behaviour, gestures, system dialogs, share sheets and dark mode follow each platform's guidelines unless the design states a reason. Where a cross-platform framework differs from the platform, the difference is listed and accepted by the human.
- **M8 – Store rules are requirements.** The plan covers what each store demands before release: privacy declarations (data collected and why), permission strings, account deletion if accounts exist, age rating, content rules, payment rules for digital goods, third-party SDK disclosures. Assume a review can reject the app; a rejection is a planned risk, not a surprise.
- **M9 – Old versions stay alive.** Users do not all update. The app tolerates a server that moved ahead (and the server tolerates old app versions, see `backend` B3); the plan states the minimum supported app version, how a too-old app is told to update, and how local data migrates between app versions.
- **M10 – Release is a process.** Signing keys and certificates (who holds them, how they are backed up), build numbers, versioning, release channels (internal, beta, production), staged rollout, a way to halt it, and crash reporting are decided in the plan. Keys and secrets never enter the repository.
- **M11 – Notifications (if any).** Each notification type has a purpose, a trigger, a user control to disable it, content that reveals nothing sensitive on a locked screen, and behaviour when the user has denied permission.
- **M12 – Links into the app (if any).** Every deep link or universal link has a defined target, a defined behaviour when the user is signed out, when the target no longer exists, and validation of its parameters as untrusted input.
- **M13 – Cost to the device.** Battery, data, storage and memory are bounded for the main flows with targets from the spec (start-up time, background activity, download size). A background task needs a requirement.
- **M14 – Text and locale.** All user-facing text comes from the platform's string resources; layouts tolerate longer translations; dates, numbers and currencies use the system's formatters.

## Typical quality gates (copy into `project/profile.md`, Section 6)
1. Lint and format, 2. static analysis or type check, 3. unit tests, 4. UI tests of the critical flows on at least one simulator or emulator **per platform and per minimum OS version** in M1, 5. a run on at least one real device per platform before release, 6. accessibility checks (automated scanner plus a manual screen-reader pass for new screens), 7. release build with signing succeeds, 8. dependency audit, 9. store-requirement checklist (M8) signed off before submission.

## Checklists

**Specify.** Platforms, minimum OS versions, device classes (M1). Every permission and its denied behaviour (M2). Flows interrupted by lifecycle events (M3). Offline, slow and dropped-network behaviour of each flow (M4). What is stored on the device and for how long (M5). Notifications (M11), deep links (M12), accounts and deletion (M8). Language(s), screen reader support, text size (M6, M14). What happens when the app is too old (M9).

**Design.** Run the design playbook. Screens for each form factor in M1, in light and dark, at the largest text size. For each screen: empty, loading, error, offline and permission-denied states. Platform conventions that differ (M7).

**Plan.** Native or cross-platform with the reason (and the escape hatch for platform features the framework lacks). Architecture and where state lives. Local storage, sync and conflict rule (M4, M5). Networking, timeouts and retries. Permissions and their strings (M2). Navigation and deep links (M12). Release pipeline, signing, channels, rollout (M10). Store requirements (M8). Crash and analytics reporting with privacy decisions. How each mechanism is tested without a real network, a real clock or real hardware (fakes), and what only a real device can prove.

**Tasks.** Order: toolchain and runtime check (SDK versions, simulators), scaffolding that builds and runs an empty app on each platform, CI, then navigation shell, text resources and design tokens, then one flow per task with its tests. Developer-account, signing and store-console work are "Requires human action" tasks placed before the first task that needs them. A task for the release build and one for the store-requirement checklist come last.

## Typical open decisions
Platforms and minimum versions, native or cross-platform framework, state management, local database, sync strategy, authentication, push provider, analytics and crash reporting, release channels, signing and key custody, distribution (public store, private distribution), monetisation and payment rules, store accounts.

## Proven and not yet proven
- **Proven:** nothing yet. The generic parts of the flow are proven on other modules.
- **Not yet proven:** every rule above; in particular the test gates on emulators and real devices (a real device run cannot be done by an agent alone: the human does it and reports), M8 and M10 (store process and signing).
