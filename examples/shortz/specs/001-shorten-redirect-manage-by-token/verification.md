# Verification 001: Shorten, redirect, manage by token

- **Feature:** `specs/001-shorten-redirect-manage-by-token/`
- **Status:** Approved
- **Date:** 26/11/2026
- **Run:** 3
- **Verified by:** Grok 4.7 (Cursor agent)
- **Independent:** yes (this chat did not implement the feature)
- **Quality command:** `npm run quality` (profile §5: lint → typecheck → test → test:e2e → audit → build)
- **Quality result:** the passing run is exit 0, with network so Turso resolved. Lint pass. Typecheck pass. Vitest **67 passed** (17 files). Playwright **52 passed** (Chromium desktop + Pixel 5). `npm audit --audit-level=high` exit 0 (**0 high / 0 critical**, 4 moderate, esbuild via drizzle-kit). Production build pass (Next.js 16.4.6). Routes: `/`, `/_not-found`, `/link-not-found`, `/privacy` static; `/manage` partial prerender; `/r/[code]` dynamic.
- **Same command, earlier this run:** one network attempt failed before e2e. `tests/create-link.test.ts` AC20 expected `count(*)` of `links` to rise by 30 and saw +32 (`1798` vs `1800`). The 31st create for that IP had already been rejected. A later full run passed. A sandboxed attempt before that could not resolve `database-host.example` (18 failed, 49 passed); e2e, audit, and build did not run. That attempt is an environment block, not a product result.
- **Not a fresh install:** `npm ci` after wiping `node_modules` was not run.

## Summary

Create, redirect, list, add, delete, and session resume match the numbered requirements, and a full `npm run quality` then passed (67 unit tests, 52 end-to-end tests, no high-severity audit findings, build ok). The same command failed once just before that, because the bulk-create test counts every row in the shared `links` table. The list still formats creation time as British UTC while the spec asks for the user’s zone, and three tool packages use a caret instead of an exact pin. Offline add/delete, an atomic rate-limit update, a tighter content-security policy, and several checks (full production smoke, GitHub Actions) are partial or were not run here.

**Verdict: not verified**

## Requirement and criterion table

| Requirement / criterion | Status | Code | Test |
|---|---|---|---|
| R1 Create a short link | met | `src/lib/create-link.ts`, `src/components/create-form.tsx` | `e2e/create.spec.ts` AC1; `tests/create-link.test.ts` |
| R2 http(s) only, case-insensitive | met | `src/lib/url.ts` | `tests/url.test.ts`; `e2e/create.spec.ts` AC4 |
| R3 Reject empty, non-URL, other schemes; English error; no link | met | `src/lib/url.ts`, `src/lib/create-link.ts` | `tests/url.test.ts`; `e2e/create.spec.ts` AC3, AC4 |
| R4 Trim before validation | met | `src/lib/url.ts` (trim first) | `tests/url.test.ts` AC2; `tests/create-link.test.ts` AC2 |
| R5 Reject over 2048 Unicode code points | met | `src/lib/url.ts` | `tests/url.test.ts` AC5 |
| R6 Redirect to stored URL | met | `src/app/r/[code]/route.ts` 302 | `e2e/redirect.spec.ts` AC6 (status, Location, &lt;500 ms after warm-up) |
| R7 Unknown or deleted code: English not-found, no redirect to an original URL | met | `src/app/r/[code]/route.ts`, `src/app/link-not-found/page.tsx` | `e2e/redirect.spec.ts` AC7; `e2e/manage-delete.spec.ts` AC12. Live `GET /r/nosuchcd` → 302 `https://production-host.example/link-not-found` |
| R8 New token, short link, copy, download, recovery warning | met | `src/components/create-form.tsx` | `e2e/create.spec.ts` AC1 (filename only — F8) |
| R9 Token is the capability; no recovery path | met | `src/lib/management-token.ts`; no recovery route | `tests/management-token.test.ts`; warning in AC1 |
| R10 Valid existing token: add under it, do not issue another | met | `src/lib/create-link.ts` (`addedToExisting`) | `e2e/create-with-token.spec.ts` AC9 |
| R11 Unknown token: refuse, no new token, English error | met | `src/lib/create-link.ts` | `e2e/create-with-token.spec.ts` AC10 |
| R12 List short link, original URL, created time | met | `src/lib/list-links.ts`, `src/components/manage-form.tsx` | `e2e/manage.spec.ts` AC11. Display zone: F4 |
| R13 Add under the token, same URL rules | met | `src/lib/add-link.ts` | `e2e/manage-add.spec.ts` |
| R14 Confirm then hard-delete; cancel keeps redirect; afterwards R7; other token cannot delete | met | `src/lib/delete-link.ts` filters on `managementTokenId` | `e2e/manage-delete.spec.ts` AC12, AC13; `tests/manage-authz.test.ts` foreign delete |
| R15 No list/add/delete without token or session; resume a valid session | met | `requireManageSession`; `src/app/manage/page.tsx` loads the cookie | `tests/manage-authz.test.ts`; `e2e/manage.spec.ts` AC14; `e2e/manage-resume.spec.ts` |
| R16 Public redirect without a management session | met | `src/app/r/[code]/route.ts` | `e2e/redirect.spec.ts` AC6 (`request.get`, no session cookie) |
| R17 No expiry of links or tokens | met | `src/db/schema.ts` (no link/token TTL) | `tests/no-link-expiry.test.ts` AC18 (clock +400 days) |
| R18 User-facing text English | met | `src/messages/en.ts` | End-to-end asserts English copy on the flows above |
| R19 Limits on token guessing and bulk create | partial | `src/lib/rate-limit.ts` (30/hour create, 10/15 min token, fail-closed); `src/lib/request-meta.ts` last hop | `tests/rate-limit.test.ts` AC16, AC20; `tests/create-link.test.ts` AC20; `tests/request-meta.test.ts`. Counter race: F2 |
| R20 Logs: no full token, no full original URL | met | `src/lib/logger.ts`; create and unlock log short code / error code / correlation id | `tests/logger.test.ts`; `tests/logging-actions.test.ts` AC17, AC21. Add and delete do not log the URL |
| R21 Same URL twice → two short links | met | `src/lib/create-link.ts`, `src/lib/short-code.ts` | `tests/create-link.test.ts` AC15 |
| R22 Same invalid-token error class | met | `src/lib/manage-session.ts`, `src/lib/create-link.ts` | `tests/manage-session.test.ts` AC19. Same not-found page for unknown and deleted |
| AC1 | met | Create result UI | `e2e/create.spec.ts` |
| AC2 | met | `validateOriginalUrl` + create | `tests/url.test.ts`, `tests/create-link.test.ts` |
| AC3 | met | empty / whitespace | unit + `e2e/create.spec.ts` |
| AC4 | met | `javascript:` and non-URL | unit + `e2e/create.spec.ts` |
| AC5 | met | length 2049 | `tests/url.test.ts` (plan assigns unit only) |
| AC6 | met | 302 to original | `e2e/redirect.spec.ts` |
| AC7 | met | not-found page | `e2e/redirect.spec.ts` |
| AC8 | met | deleted code | `e2e/manage-delete.spec.ts` AC12 |
| AC9 | met | create with token | `e2e/create-with-token.spec.ts` |
| AC10 | met | bad token on create | `e2e/create-with-token.spec.ts` |
| AC11 | met | unlocked list columns | `e2e/manage.spec.ts` |
| AC12 | met | confirm delete | `e2e/manage-delete.spec.ts` |
| AC13 | met | cancel delete | `e2e/manage-delete.spec.ts` |
| AC14 | met | session required for list, add, delete | `tests/manage-authz.test.ts` (would fail if the session or owner check were removed); `e2e/manage.spec.ts` locked page; `e2e/manage-resume.spec.ts` |
| AC15 | met | two codes | `tests/create-link.test.ts` |
| AC16 | met | token bucket | `tests/rate-limit.test.ts`; header unit `tests/request-meta.test.ts` |
| AC17 | met | log redaction | `tests/logging-actions.test.ts` |
| AC18 | met | no link TTL | `tests/no-link-expiry.test.ts` |
| AC19 | met | same error class | `tests/manage-session.test.ts` |
| AC20 | met | create bucket, no extra row for that IP | `tests/create-link.test.ts`, `tests/rate-limit.test.ts`. The global `count(*)` assertion is racy (F8). The limit itself is not atomic (F2) |
| AC21 | met | URL redaction on create/unlock logs | `tests/logging-actions.test.ts` |
| Plan D1 / D9 schema | met | `src/db/schema.ts` matches plan §5 | `tests/db/migrate.test.ts` |
| Plan token storage | met | selector + SHA-256 verifier, `timingSafeEqual` | `tests/management-token.test.ts` |
| Plan session cookie | met | HttpOnly, SameSite=Lax, Path=/, 7-day Max-Age; Secure from last proto or production when the header is absent | `tests/manage-session.test.ts`; `tests/request-meta.test.ts`; resume e2e |
| Plan CR-1 trusted metadata | partial | `src/lib/request-meta.ts` wired from create, add, list, unlock, logout, and `/manage`. IP and host match option C | `tests/request-meta.test.ts` (fails if the first hop is trusted). Short-link scheme is the raw last proto token (F14) |
| Plan D3 CI | partial | `.github/workflows/quality.yml`; `origin` is the private repository (SSH remote) | `tests/ci-workflow.test.ts` asserts the file. No Actions run observed (F10) |
| Plan D6 redirect timing | met | e2e budget in test env | `e2e/redirect.spec.ts` AC6. LCP and JS transfer not measured |
| Plan D7 browsers | partial | Playwright Chromium + Pixel 5 | This run. Firefox/WebKit not run (accepted plan gap) |
| Plan D8 privacy | met | `src/app/privacy/page.tsx` | `e2e/privacy.spec.ts`. Live `GET /privacy` returned 200 |
| Plan W9 headers | partial | `next.config.ts` | `e2e/security-headers.spec.ts` checks presence. Live CSP includes `'unsafe-inline'` and `'unsafe-eval'` (F3) |
| Plan §12 production smoke | untested | `verification-prep.md` records five passes by another agent at ~21:29 UTC | This run did not repeat create → open → manage → delete (F9). Spot check only |
| Spec §6 offline, create and unlock | met | catch sets `create.errorOffline` / `manage.errorOffline` | `e2e/offline.spec.ts` (fails if the sentence is absent) |
| Spec §6 offline, Manage add and delete | partial | `onAdd` and `confirmDelete` have no catch | No test (F1) |
| Spec §6 generic server error | met | `src/app/error.tsx` | `tests/error-screen.test.ts` (fails if the internal string is shown or a design sentence is removed). Next 16 passes `retry` |
| Spec §6 double submit | met | submit `disabled` while pending | `e2e/create.spec.ts` asserts the button is disabled after one click (F8) |
| Spec §6 keep URL and token after an error | untested | controlled inputs are not cleared on error | No assert (F7) |
| Spec §6 creation time in the user’s locale and zone | contradicts | `formatCreatedAt` uses `en-GB` and `timeZone: "UTC"` in a client component | No test of the zone (F4) |

## Plan and constitution

Pinned product dependencies in `package.json` match the plan: `next@16.4.6`, `eslint-config-next@16.4.6`, `react@19.3.0`, `react-dom@19.3.0`, `typescript@5.9.3`, `drizzle-orm@0.45.4`, `drizzle-kit@0.31.11`, `@libsql/client@0.18.0`, `vitest@5.1.1`, `@playwright/test@1.65.1`, `@axe-core/playwright@4.13.0`. Data model matches plan §5. Error codes match plan §6. No recovery, analytics, accounts, or vanity codes were found. `.env.example` has empty values; `.env` and `.env.local` are gitignored.

Run 1 findings on forwarded headers, session resume, the error screen, and list/add/delete authorisation stay closed in the code and in tests.

C1: numbered requirements above are implemented except the rows marked partial, untested, or contradicts. C4/C5: those rows have a test that can fail, except where the table says otherwise. C6 review is below. C7: automated axe on three screens passed inside `quality`; a person has not signed the keyboard or screen-reader pass. C8 exact pins: F5. C2/C11: this run did not change approved specs. Profile exceptions: none. Backend B5 (every list has a page size) is F6; the approved plan contract returns the full `items` array. `logoutManageAction` exists and no screen calls it; the approved design screens do not include a logout control, and the plan names the action.

Severity used here is the verify playbook’s scale: contradicting behaviour and a constitution violation are Critical; partial, untested, and unrequested behaviour are High; a weak test or stale text is Medium; cosmetic is Low. That is why this verdict is `not verified` rather than `partly verified`.

## Security and privacy review

Checked against spec §7, plan §7, OWASP Top 10 (web), and OWASP API Security Top 10.

- **Boundary validation.** `validateOriginalUrl` trims, caps Unicode code points at 2048, and allows only `http:` / `https:`. `javascript:`, other schemes, and a non-URL become `INVALID_URL`. The server does not fetch the URL (no SSRF). Redirect uses the stored URL only.
- **Access control.** List, add, and delete read the session id from the HttpOnly cookie on the server. `requireManageSession` rejects a missing or expired row. Delete also matches `management_token_id` and returns `NOT_FOUND` for a foreign code. `tests/manage-authz.test.ts` calls those functions and would fail if the checks were removed.
- **Trusted metadata (CR-1).** Rate-limit IP is the last `x-vercel-forwarded-for`, else `x-real-ip`, else the last `X-Forwarded-For`, else `unknown`. `Secure` uses the last `x-forwarded-proto`, or production when that header is missing. The short-link host is the `host` header, never `x-forwarded-host`. Unit tests cover a spoofed first hop. The short-link scheme is the raw last proto token, not limited to `http` or `https` (F14).
- **Token storage.** 16-byte CSPRNG selector and verifier; only SHA-256 of the verifier is stored; compare uses `timingSafeEqual` on the digests. Raw token is returned once from create. `SESSION_SECRET` is required at startup and is not used after that. The session id is 32 random bytes stored as the cookie value and the row id, which matches the plan’s lookup model.
- **Abuse limits.** Fixed windows, English `RATE_LIMITED`, fail-closed when the database throws (the sandboxed run turned DNS failure into that error). The count is read and then written in separate statements, and a conflicting insert sets the count back to 1 (F2). Add uses the create bucket.
- **CSRF.** Mutations are Server Actions on Next.js 16.4.6, which the plan names as the Origin/Host check. This run did not re-read the framework’s Origin implementation.
- **Headers.** Live and local config send `X-Frame-Options: DENY`, `nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, CSP, and `Permissions-Policy`. Vercel also sent HSTS. CSP `script-src` includes `'unsafe-inline'` and `'unsafe-eval'` on `https://production-host.example/` (F3). No `dangerouslySetInnerHTML` in `src/`. React text rendering is used for the original URL in the list. Live HTML also sent `access-control-allow-origin: *`; that header is not set in this repository. This run did not trace which layer adds it.
- **Open redirect.** Unknown codes 302 to `/link-not-found`. On the live host the Location was the same host, not an original URL. This run did not send a spoofed `x-forwarded-host` to production.
- **Logging and echoes.** Create and unlock logs are covered by AC17/AC21. Error strings shown to the user are fixed English; they do not include the submitted URL or token. Add and delete do not log.
- **Secrets.** Not printed. Example file has blanks. Audit: 4 moderate, below the high gate. Not waived.
- **Not checked.** A stolen `x-vercel-forwarded-for` on the real host, Turso restore (backend B9), and whether Next derives `request.url` from a caller-supplied host when the platform does not rewrite it.

## Accessibility

`e2e/a11y.spec.ts` ran axe with tags `wcag2a` and `wcag2aa` on Create, locked Manage, and `/link-not-found` in both Playwright projects; those tests passed inside the green `quality` run. Smoke also asserts no critical axe violations on the home page. Tags do not include `wcag22aa`. Creation result, unlocked Manage, the delete dialog, and the server-error screen were not scanned. Buttons use `min-h-11`. Alerts use `role="alert"`. No `prefers-reduced-motion` rule was found; the dialog animates (F12). `keyboard-check.md` records an agent pass, not a person’s. Screen reader, 200% zoom, and contrast were not done here (needs a human).

## Findings

### F1 — High
- **Kind:** partial
- **Where:** `src/components/manage-form.tsx` `onAdd`, `confirmDelete`
- **What:** Spec §6 says Manage offline is the same English failure as Create. Create and unlock show “You appear to be offline. Check your connection and try again.” when the call does not arrive. Add and delete have no `catch`, so a dropped request does not show that sentence.
- **Smallest fix:** Use the same `manage.errorOffline` catch on add and delete, with an e2e that aborts those posts.
- **Belongs in:** a new task

### F2 — High
- **Kind:** partial
- **Where:** `src/lib/rate-limit.ts` `assertWithinRateLimit`
- **What:** The window is fixed and expired rows are deleted, as the plan says. The count is read and then written in separate statements. Overlapping requests can both pass under the limit. A conflicting insert sets the count to 1. Sequential AC16/AC20 still reject once the stored count is over the limit.
- **Smallest fix:** One conditional update that increments only while `count` is still under the limit.
- **Belongs in:** a new task

### F3 — High
- **Kind:** partial (security)
- **Where:** `next.config.ts` `CONTENT_SECURITY_POLICY`; live response on `https://production-host.example/`
- **What:** Plan W9 asks for a CSP with `default-src 'self'`, tightened as the UI needs. `script-src` also allows `'unsafe-inline'` and `'unsafe-eval'`. The e2e test only checks that a CSP header is non-empty. The live home response carries the same policy.
- **Smallest fix:** Drop `'unsafe-eval'` if the production build does not need it, and assert the CSP value in the e2e test.
- **Belongs in:** a new task

### F4 — Critical
- **Kind:** contradicts
- **Where:** `src/components/manage-form.tsx` `formatCreatedAt`
- **What:** Spec §6 says show the creation time in the user’s locale and zone where the platform allows. The list formats with `en-GB` and `timeZone: "UTC"` inside a client component, so the browser zone is available and unused. Stored `createdAt` is still UTC, which the spec allows.
- **Smallest fix:** Format with the runtime locale and zone, or record a spec change that accepts UTC `en-GB`.
- **Belongs in:** a spec change request (if UTC stays) or a new task (if the user’s zone is required)

### F5 — Critical
- **Kind:** constitution (C8)
- **Where:** `package.json` `eslint`, `@types/react`, `@types/react-dom`
- **What:** C8 says pin exact versions. Those three ranges use `^`. Named runtime dependencies are exact. Profile exceptions: none.
- **Smallest fix:** Pin the three ranges to the versions already installed.
- **Belongs in:** a new task

### F6 — High
- **Kind:** constitution (backend module B5)
- **Where:** `src/lib/list-links.ts`, `src/db/repositories/links.ts` `listLinksByManagementTokenId`
- **What:** B5 says every list has a default and a maximum page size. `listLinks` returns every row for the token, ordered by `created_at`. The approved plan contract also returns the full `items` array, and the profile records no exception.
- **Smallest fix:** Record a profile exception or a plan page size. Do not add a silent cap.
- **Belongs in:** a plan revision or a profile exception, then a task if a cap is chosen

### F7 — High
- **Kind:** untested
- **Where:** `src/components/create-form.tsx`, `src/components/manage-form.tsx`
- **What:** Spec §6 says keep the URL and token after an error where that is sensible. The controlled fields are not cleared when validation fails. No test asserts that.
- **Smallest fix:** An e2e that submits an invalid URL and asserts the field values are unchanged.
- **Belongs in:** a new task

### F8 — Medium
- **Kind:** weak test
- **Where:** `e2e/create.spec.ts`; `e2e/a11y.spec.ts`; `tests/create-link.test.ts`; `specs/001-shorten-redirect-manage-by-token/keyboard-check.md`
- **What:** AC1 checks the download filename, not that the file contains the token. The loading test clicks once and then expects the button to be disabled. Axe does not cover the result view, unlocked Manage, the dialog, or the server-error screen, and does not use WCAG 2.2 tags. AC20’s final assert is `count(*)` of the whole `links` table. This run saw that assert fail (`+32` instead of `+30`) while other tests were writing rows, then pass on a later `npm run quality`. The keyboard note was written by an agent.
- **Smallest fix:** Assert the download body, count only the rows for that test IP or token, and extend axe to the result and the open dialog.
- **Belongs in:** a new task

### F9 — High
- **Kind:** untested
- **Where:** `specs/001-shorten-redirect-manage-by-token/verification-prep.md`; plan §12
- **What:** The prep note now records all five smoke steps as passed by another agent at about 21:29 UTC on `https://production-host.example/`. This run did not repeat create, open, manage, or delete. It is not a pass. This run did see `GET /` 200, `GET /privacy` 200, and `GET /r/nosuchcd` 302 to the same host’s `/link-not-found`.
- **Smallest fix:** A person repeats the five steps on that host and signs the prep note.
- **Belongs in:** human action already described on T26

### F10 — High
- **Kind:** untested
- **Where:** `.github/workflows/quality.yml`
- **What:** The workflow file is present and a unit test checks its contents. `git remote` now shows `origin` → the private repository (SSH remote). `gh` is not installed here. An unauthenticated GitHub API call for Actions runs returned 404. No green Actions run was observed. That check is not a pass.
- **Smallest fix:** Confirm one green Actions run on that repository.
- **Belongs in:** human action already described on T7

### F11 — High
- **Kind:** unrequested
- **Where:** `next.config.ts` `cacheComponents: true`, `partialPrefetching: true`
- **What:** The plan does not name these switches. The passing build reports both enabled. No `use cache` appears under `src/`. The redirect route stayed dynamic.
- **Smallest fix:** Remove them, or name them in a plan revision.
- **Belongs in:** a plan revision if they stay

### F12 — High
- **Kind:** partial
- **Where:** `src/components/ui/dialog.tsx`; `src/app/globals.css`
- **What:** Web W3 says motion is disabled under reduced motion. The dialog fade/zoom classes have no `prefers-reduced-motion` override.
- **Smallest fix:** Skip those animations when the user prefers reduced motion.
- **Belongs in:** a new task

### F13 — Medium
- **Kind:** stale text
- **Where:** `src/app/layout.tsx` title; `src/lib/create-link.ts`; `src/lib/add-link.ts`
- **What:** The home title is `Shortz`. Design §6 gives “Shorten a URL · Shortz” as the example Create title. Manage and the short-link not-found page already use the design examples. Server validation text duplicates `src/messages/en.ts` instead of calling `t()`. The English sentences match.
- **Smallest fix:** Set the Create title to the design example. Point server messages at the catalogue.
- **Belongs in:** a new task

### F14 — High
- **Kind:** partial (security)
- **Where:** `src/lib/request-meta.ts` `requestBaseUrl`
- **What:** The short-link scheme is the last `x-forwarded-proto` token, whatever it is. A value other than `http` or `https` is copied into the short URL. CR-1 restricts that header for the cookie `Secure` flag and forbids `x-forwarded-host` for the host. It does not allowlist the scheme. The unit test checks `http, https`, not a non-http token.
- **Smallest fix:** Accept only `http` and `https`; otherwise use `http`. Assert that in the unit test.
- **Belongs in:** a new task

## Needs a human

1. Repeat the five production steps on `https://production-host.example/` and sign `verification-prep.md` (create → open → manage → delete → `/privacy`). The current note is another agent’s record.
2. Confirm one green GitHub Actions `quality` run on the private repository (secrets already named in the workflow).
3. On that production host, confirm a client-supplied first hop does not choose the rate-limit IP, the cookie `Secure` flag, or the short-link host (CR-1).
4. Keyboard pass on a production build by a person: Create, result, Manage locked and unlocked, delete dialog (Tab, visible focus, Escape cancels). `keyboard-check.md` is an agent note.
5. Screen-reader pass on those same screens (errors announced, dialog name, list columns).
6. At 200% zoom and about 360 px width, check that text does not clip and that primary buttons stay at least 44×44 px.
7. Open the app once in current Firefox and once in current WebKit (plan D7 gap; not part of `quality`).

## Interpretations

- A 302 to `/link-not-found` counts as meeting R7 and AC7: the visitor is not sent to an original URL, and the page shows the specified English not-found copy. AC7’s e2e follows that redirect and asserts the heading. The live unknown code did the same, on the same host.
- The 7-day manage session may expire without expiring links or tokens (R17). AC18 and the schema match that reading.
- Plan rate-limit notation is implemented as HMAC-SHA256 with `RATE_LIMIT_SECRET` as the key and `scope:ip` as the message.
- Packages pulled by the shadcn CLI (`@base-ui/react`, `class-variance-authority`, `clsx`, `lucide-react`, `tailwind-merge`, `tw-animate-css`) are the plan’s “shadcn/ui + tailwind (pins from CLI)”, not extra product features. `vite@8.4.0` is the Vitest peer named in task T3.
- Add and delete do not write routine logs. AC21 is met for them because no full original URL is written. The tests cover create and unlock only.
- Design §6 page titles are introduced with “e.g.”, so F13 is stale text, not a contradiction of a fixed string. The timezone sentence in spec §6 is not an example, so F4 is a contradiction.
- F9 and F10 are checks that did not run. They are findings and they are not passes. On this playbook’s scale they are High, so they block `verified` and they also block `partly verified`.
- Severity was not lowered to keep the run-2 verdict. Partial, untested, and unrequested items are High. Contradicting behaviour and C8 are Critical.

## Not done

- No file other than this one was edited. No task was re-marked. Nothing was approved.
- Firefox, WebKit, screen reader, personal keyboard pass, 200% zoom, LCP, and JS transfer size were not run.
- The five-step production smoke was not repeated. GitHub Actions was not observed.
- A spoofed forwarding header was not sent to the live host.
- A clean `npm ci` was not run.
- `npm audit fix` was not run.

## Approval
- **Status:** Approved
- **Approved by:** Luca Lanzano
- **Date:** 26/11/2026
- **Close:** Feature 001 is closed. Findings F1–F14 are accepted. The verdict stays `not verified`.
