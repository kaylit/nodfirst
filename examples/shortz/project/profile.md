# Project profile

> Owned by this project. Written by `init` (new project) or `adopt` (existing code). Kit updates never replace this file.
> Section 0 is updated by the playbooks as work moves on; changing it does not undo the approval of the profile.
> Status: Approved · Approved by: Luca Lanzano · Date: 26/11/2026
> Written with NodFirst kit version: 0.1.0

<!--
Rules for whoever fills this in:
- Do not repeat the constitution: cite rule IDs (C1…C14).
- Every MUST is checkable. Undecided rows say DECIDE and appear in Section 11.
- Keep the section numbers. A section that does not apply: "N/A – reason".
-->

## 0. Current state
- **Active feature:** none
- **Last closed:** `specs/001-shorten-redirect-manage-by-token/` (26/11/2026; verification approved; verdict not verified; findings F1–F14 accepted)
- **Working profile:** Solo
- **Git:** used

## 1. Product summary
Shortz is a small web app that shortens long URLs into short links suitable for social media and general sharing. Anyone can create a short link without an account; opening the short link redirects to the original URL. After creation, the user receives a one-time management token to view the links associated with that token. User-facing UI text is English; conversation with the agent may be Italian. Specs and project documents are written in English (template headings and IDs stay in English). Identifiers in code and machine-readable values are English (C12).

- **Modules:** web, backend (`nodfirst/modules/`)
- **Modules not fully proven, accepted by the human:** web (partly proven; unproven parts accepted), backend (not yet proven), 2026-11-26
- **Proving ground for the kit:** no

## 2. Way of working
- **Who approves:** Luca Lanzano
- **Approval record:** when work is accepted, record `Approved by: Luca Lanzano` and `Date:` as `DD/MM/YYYY`. Standing instruction from 26/11/2026: use this name; if no date is repeated, use the calendar date of that acceptance.
- **Language of conversation:** Italian
- **Language of specs and project documents:** English
- **Git checkpoints:** the agent commits after each approval
- **Branches and review (Team):** N/A – Solo profile

## 3. v1 scope
**In scope**
- Paste a long URL and receive a short link
- Opening the short link redirects to the original URL
- After creation, show a one-time management token with a clear copy (and optionally download) affordance and an explicit warning that it cannot be recovered if lost
- With that token, view the list of links tied to it
- No recovery path for a lost management token (by design in v1; short links themselves keep working)
- Minimal web UI (URL field, submit, short link result, management view) using shadcn
- Deployable on Vercel (Hobby plan)

**Out of scope for v1**
- Registration, login, magic link, or any account system
- Advanced analytics, custom branding, public API for third parties
- Offline / installable PWA
- Custom domain (open decision)
- Team / multi-user organisation features

## 4. Technical profile
| Area | Decision |
|---|---|
| Language / runtime (with minimum version) | TypeScript on Node.js ≥ 22 (machine checked: v22.23.5) |
| Package manager | npm (machine checked: 10.9.9; pnpm/yarn/bun not installed) |
| Framework / main libraries | Next.js (frontend and backend in one app); UI: shadcn |
| Data storage | Turso/libSQL remote (SQL over HTTP); design allows later external DB (D1 done) |
| Hosting / distribution | Vercel Hobby |
| Language of messages and documentation vs identifiers | UI and product docs: English. Specs/project docs: English. Code identifiers and machine values: English |

## 5. Commands
- **Set-up:** `npm install` (uses `.npmrc` `legacy-peer-deps=true` because npm 10.9.9 arborist fails resolving some peer sets without it)
- **Single quality command (runs every gate below):** `npm run quality` (= `lint` → `typecheck` → `test` → `test:e2e` → `audit` → `build`; gates 1–7)
- **Other:** `npm run dev` · `npm run lint` · `npm run typecheck` (`next typegen && tsc --noEmit`) · `npm run test` · `npm run test:e2e` · `npm run audit` (`npm audit --audit-level=high`) · `npm run build` · `npm run db:generate` · `npm run db:migrate`

## 6. Quality gates (a task is done only if all pass)
<!-- Without CI, ONE local command (Section 5) MUST run gates 1–7 once scaffolding exists. -->
1. Lint passes
2. Type check passes
3. Unit and integration tests pass
4. End-to-end tests of critical flows of the current spec pass (at least: create short link → open short link → view links with management token)
5. Production build succeeds
6. Accessibility: automated checks pass; new UI has a recorded manual keyboard check
7. Dependency audit reports no known high-severity issues
8. N/A – offline / installability (not in v1 scope)
9. Performance numeric targets (plan D6 / W8): soft — redirect p95 TTFB &lt;500ms (e2e asserts 302 within 500ms in test env); Create LCP soft &lt;2.5s mid-range lab; JS transfer soft &lt;300KB gzip. No hard fail in `quality` beyond the redirect timing e2e; lab LCP/JS optional smoke.
10. When database migrations exist: apply on empty DB (and rollback if promised) as in backend module typical gates

## 7. Design system rules (only if there is a UI)
- Mobile-first; light theme for v1
- Use shadcn components; no elaborate custom design system in v1
- Binding tokens/components beyond shadcn defaults: live in `project/design-system.md` when that file is created (design-system playbook or first UI feature)
- Follow module web W2 (WCAG 2.2 AA) and W3 where applicable
- One primary job per screen: shorten a URL; manage links via token

## 8. Data, privacy and security specifics
- No user accounts in v1; no email or profile data collected for auth
- Stored data (minimum): original URL, short code, creation date, management-token association (exact fields in the first feature spec)
- Management token is a secret capability: treat as untrusted input at boundaries; do not log full tokens (C6)
- Audience: worldwide. Still minimise data; if EU residents use the service, GDPR obligations may apply (privacy policy / retention details: DECIDE in first feature or D8)
- Short links are public: anyone with the short URL can open it
- No non-essential trackers or analytics in v1
- Threat baseline: OWASP Top 10 (web); OWASP API Security Top 10 for HTTP APIs (backend)

## 9. Feedback loop (only if the project is a proving ground)
N/A – not a proving ground for the kit.

## 10. Exceptions to the constitution
- None.

## 11. Open decisions
| # | Decision | When | Candidates / criteria |
|---|---|---|---|
| D1 | How SQLite (or compatible) persists on Vercel serverless | Done in plan 001 (26/11/2026) | Turso/libSQL remote (SQL over HTTP) |
| D2 | Custom domain | After v1 works on Vercel default URL | Optional; cost and DNS |
| D3 | CI (GitHub Actions or other) vs local-only quality command | Done in plan 001 (26/11/2026) | Local `quality` + GitHub Actions |
| D4 | Management token powers | Done in spec 001 (26/11/2026) | List, add, and permanently delete (no in-place edit); confirmed in specify |
| D5 | Future accounts (magic link) and “my links” | After v1 | Out of v1; revisit when needed |
| D6 | Numeric performance targets (W8) | Done in plan 001 (26/11/2026) | Redirect p95 TTFB &lt;500ms; Create LCP soft &lt;2.5s; JS soft &lt;300KB |
| D7 | Supported browsers and viewport range (W7) | Done in plan 001 (26/11/2026) | Chromium/Firefox/WebKit; 360–1440; e2e Chromium (+ mobile emu) |
| D8 | Privacy policy / retention / deletion of URLs and tokens | Done in plan 001 (26/11/2026) | Minimal `/privacy` page; retain until delete |
| D9 | ORM / data-access library | Done in plan 001 (26/11/2026) | Drizzle + @libsql/client |
| D10 | Approver display name | Done (26/11/2026) | Luca Lanzano |
