# Module: Web application

> **PARTLY PROVEN.** Used on one real project for specify, plan, tasks, analyze and the first implement tasks. Rules W7–W11 and the items under "Not yet proven" have never been used: `init` says so and asks for confirmation.

**Version:** 0.1
**Scope:** projects with a browser UI: websites, web apps, installable web apps (PWA), with or without a server side (sign-in, stored data, hosting). Framework-neutral: server-rendered, single-page or mixed.
**State:** partly proven on one real project (see the end). Rules not tied to that project are written from standard practice and marked *not yet proven* in the final section.

## Rules (in addition to the constitution)

- **W1 – Trusted side (C6).** The server decides. Input is validated on the server; authentication and authorization are enforced on the server for every protected operation; users reach only their own data unless a spec says otherwise. Baseline checklist: OWASP Top 10 (and OWASP ASVS level 1 for apps with accounts). User-supplied rich content is sanitized before storage and before rendering.
- **W2 – Accessibility (C7).** WCAG 2.2 level AA: keyboard operable, visible focus, sufficient contrast, labelled controls, no information by colour alone, text resizable to 200%, respect reduced motion, meaningful page titles and landmarks, errors announced to assistive technology.
- **W3 – Design system.** Mobile-first (about 360 px first); touch targets at least 44×44 CSS px for primary controls; every screen and data-driven component defines empty, loading, error and (if offline matters) offline states; light and dark theme through tokens; no hard-coded colours, spacing or font sizes outside tokens; subtle motion, disabled under reduced motion.
- **W4 – Text and locale.** All user-facing text comes from a message catalogue; layouts tolerate longer translations and right-to-left if the spec lists such a language; dates, numbers and currencies use the platform's internationalization APIs; time zones are stored in UTC and shown in the user's zone.
- **W5 – Privacy.** Where EU users are involved: GDPR (data minimization, privacy policy, deletion, export, documented retention, consent for non-essential cookies and trackers). Prefer an EU data location when hosting allows. Analytics and third-party scripts are decisions, not defaults.
- **W6 – Offline and installable apps (if the spec asks).** The offline and synchronization strategy is a decision record before any plan that depends on it; installability and offline behaviour are verified, not assumed.
- **W7 – Browsers and devices.** The profile lists the supported browsers (engine and minimum version) and the smallest and largest viewport. A feature is verified on at least one engine of each family named there (Chromium, Firefox, WebKit) or the gap is recorded as an exception.
- **W8 – Performance budget.** The profile or the spec states measurable targets for the main flows (for example loading time on a mid-range phone, page weight). A plan without a target says so; the target is not invented by the agent.
- **W9 – Delivery safety.** Security headers (CSP, frame, referrer, content-type options) and HTTPS-only transport are decided in the plan. Dependencies are pinned and audited for known vulnerabilities in a gate. Configuration and secrets differ per environment and never live in the repository.
- **W10 – Failure is visible and safe.** Every error the user can reach has a page or message that says what happened and what to do, reveals nothing internal, and is logged with a correlation identifier. Unknown routes, forbidden access and server errors are specified, not left to defaults.
- **W11 – Forms and input.** Each form defines its fields, limits, validation rules (client for comfort, server for truth), error text per rule, behaviour on double submission and on reload, and what is preserved after an error.

## Typical quality gates (copy into `project/profile.md`, Section 6)
1. Lint, 2. type check, 3. unit and integration tests, 4. end-to-end tests of the critical flows of the current spec, 5. production build, 6. accessibility checks (automated plus a manual keyboard check for new UI), 7. dependency audit with no known high-severity issue, 8. for installable or offline changes: installability and offline behaviour, 9. performance target check when W8 sets one.

## Checklists

**Specify.** States for every screen (empty, loading, error, offline). Roles and who may do what. Security and privacy: access rules, repeated-attempt limits, information leaks (does anything reveal that an account or record exists?), session and token lifetime, input limits, what is logged and what never is, personal data and retention, how credentials are stored (never reversibly) and transmitted (only encrypted). Browser and device support (W7). Performance targets (W8). Every form (W11). Pages for not found, forbidden, server error and maintenance (W10). Language(s) and time zone behaviour (W4).

**Design.** Run the design playbook when the spec has screens that are not trivial. Check each screen against W2, W3, W4; proportion of text to colour for contrast; focus order; behaviour at 200% zoom.

**Plan.** Rendering model (server, client, mixed) and its consequence for security, SEO and offline. Handoff mechanisms to look for: credential storage, session handling and cookie attributes, request-forgery protection, route protection, uniform responses and timing where existence must not leak, logging, transport, rate limiting and where its counters live in stateless or serverless hosting, offline behaviour, file uploads (type, size, storage, scanning), email and other outbound messages, background jobs. Security checks for every mechanism:
- Client-controlled values (User-Agent, headers, cookies, local storage) are never the key of a security control.
- For every client-side mechanism, state who can read and write it (page script, server, service worker). An HttpOnly cookie cannot be read or deleted by script; the server cannot read local storage.
- Cookies and flags have an explicit lifetime and attributes (Secure, SameSite, HttpOnly) with the reason.
- Low-entropy identifiers stored for matching or logs use a keyed hash (HMAC with a server secret), never a plain hash; say what happens at key rotation.
- List what the chosen authentication library stores by default (for example IP and User-Agent in a session table) and justify or disable each item.
- Counters: window type (fixed or sliding), atomic increments, cleanup of expired rows.
- Say how each mechanism is tested **locally and in CI with the same component as in production** (a different database driver or service in test is a decision to take).
- State what happens to data on migration, rollback and backup restore.

**Tasks.** Include a CI task, how migrations run in production, secrets provisioning and external accounts (each marked "Requires human action"), route protection before the tasks that need it, and any role or key before the workflow that uses it. Tests that need a signed-in user, a page or an endpoint depend on the task that builds it. A task never needs a console or account that no earlier task or human action provides. Release or deployment is its own task with a rollback step.

## Typical open decisions
Rendering model, database and hosting, ORM, authentication, UI component library, rich-text editor and storage format, offline and synchronization strategy, PWA tooling, date model, test tooling and browsers, quality and performance targets, deletion and retention, analytics, email provider, CI, error monitoring.

## Proven and not yet proven
- **Proven (one project, partly):** spec with security and privacy section, plan with the handoff list and the security checklist (five review rounds), tasks with dependencies and human-action marking, analysis, and the first implement tasks (scaffolding, text catalogue, test runner).
- **Not yet proven:** end-to-end tests and the multi-browser rule (W7), automated accessibility checks, tasks that need human action in consoles (accounts, buckets, secrets), database-backed tests, offline and installable behaviour, the design phase and the design system, W8–W11 (written from standard practice).
