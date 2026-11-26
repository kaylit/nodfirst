# Tasks 001: Shorten, redirect, manage by token

- **Spec:** `specs/001-shorten-redirect-manage-by-token/spec.md`
- **Plan:** `specs/001-shorten-redirect-manage-by-token/plan.md`
- **Design:** `specs/001-shorten-redirect-manage-by-token/design.md`
- **Status:** Approved
- **Revision:** verification run 1, findings F1–F4. Tasks T1–T27 are unchanged. CR-1 is option C, recorded in the plan.

## Legend
- `[ ]` to do · `[~]` in progress · `[x]` done · `[!]` blocked (add a note)
- `[P]` can run in parallel with the previous task (no shared files or dependencies)
- **Requires human action:** work outside the repository (consoles, accounts, secrets, keys); listed under the task

## Phase 1 — Setup / foundation

- [x] **T1** Verify machine runtimes
  - **Covers:** plan §3 tools (foundation for all R/AC)
  - **Depends on:** —
  - **Requires human action:** Install Node ≥22, npm, or git if a check fails
  - **Files / areas:** report only (no app files yet)
  - **Tests:** none (commands: `node -v`, `npm -v`, `git --version`)
  - **Done when:** Node ≥22, npm, and git reported; versions recorded in the task note when implemented
  - **Note (2026-11-26):** node v22.23.5 · npm 10.9.9 · git 2.54.0 (Apple Git-157) — all OK, no human install needed

- [x] **T2** Provision Turso and local secrets
  - **Covers:** plan D1, env for R1+ (persistence)
  - **Depends on:** T1
  - **Requires human action:** Create Turso account/DB (Free); create auth token; create `.env.local` (gitignored) with `TURSO_DATABASE_URL`, `TURSO_AUTH_TOKEN`, `RATE_LIMIT_SECRET`, `SESSION_SECRET`; optional separate Turso DB for tests
  - **Files / areas:** `.env.example` (names only, no secrets), `.gitignore` entries
  - **Tests:** none yet
  - **Done when:** Human confirms env vars present locally; `.env.example` lists required keys without values
  - **Note (2026-11-26):** Turso account and database created; `.env.local` has all 4 keys set; gitignored; `.env.example` + `.gitignore` added

- [x] **T3** Scaffold Next app, lint/typecheck/test smoke, quality command
  - **Covers:** plan scaffold; enables later AC tests
  - **Depends on:** T1
  - **Files / areas:** app root `package.json`, Next App Router skeleton, ESLint, TypeScript, Tailwind, shadcn init (Button placeholder OK), `project/profile.md` §5 Commands
  - **Tests:** Vitest smoke test `tests/smoke.test.ts` that always passes; prove runner works
  - **Versions (verified in plan 2026-11-26):** `next@16.4.6`, `eslint-config-next@16.4.6`, `vitest@5.1.1`; pin `react`/`react-dom`/`typescript` via `npm view` at install to versions compatible with Next 16.4.6
  - **Done when:** `npm run lint`, `npm run typecheck`, `npm run test`, `npm run build` succeed; `npm run quality` runs gates 1–3 and 5 (lint, typecheck, unit tests, build); profile §5 filled for those commands
  - **Note (2026-11-26):** Scaffold merged; shadcn Button; `vite@8.4.0` for Vitest peer; `typecheck` = `next typegen && tsc --noEmit`; `.npmrc` legacy-peer-deps; `npm run quality` green

- [x] **T4** Add Playwright and axe smoke
  - **Covers:** plan test tooling; foundation for e2e ACs
  - **Depends on:** T3
  - **Files / areas:** Playwright config (Chromium + one mobile project), `@axe-core/playwright`, sample e2e hitting home 200
  - **Tests:** e2e smoke `e2e/smoke.spec.ts`; optional axe on home with zero critical setup
  - **Versions:** `@playwright/test@1.65.1`, `@axe-core/playwright@4.13.0`; `npx playwright install chromium`
  - **Done when:** `npm run test:e2e` passes smoke; `quality` extended to include e2e (gate 4 partial)
  - **Note (2026-11-26):** `@playwright/test@1.65.1`, `@axe-core/playwright@4.13.0`; Chromium installed. Config: Desktop Chrome + Pixel 5. Smoke: home 200 and zero critical axe (4 passed). `quality` runs `test:e2e` before build. Profile §5 left for T27.
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T5** Drizzle schema and first migration on Turso
  - **Covers:** plan §5 data model (R1, R9, R12–R14, R19 persistence)
  - **Depends on:** T2, T3
  - **Files / areas:** `drizzle` schema (`management_tokens`, `links`, `manage_sessions`, `rate_limits`), `drizzle.config.ts` dialect `turso`, migration SQL, `db:generate` / `db:migrate` scripts, DB client using `@libsql/client` (`/web` where required)
  - **Tests:** integration `tests/db/migrate.test.ts` — connect and `SELECT` after migrate (fails if tables missing)
  - **Versions:** `drizzle-orm@0.45.4`; `drizzle-kit` and `@libsql/client` exact pins via `npm view` at install (plan candidates recorded)
  - **Done when:** Migration applied to the human’s Turso DB; integration migrate check green; `quality` still green
  - **Note (2026-11-26):** Pins from `npm view`: `drizzle-orm@0.45.4`, `drizzle-kit@0.31.11` (latest stable, 2026-09-21), `@libsql/client@0.18.0` (2026-09-02). Migration `drizzle/0000_init.sql` applied on Turso. `tests/db/migrate.test.ts` selects the planned columns (1 passed).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T6** Env validation, logger, error codes
  - **Covers:** R20 (logging rules); plan error codes
  - **Depends on:** T3, T5
  - **Files / areas:** env schema (fail fast if secrets missing), logger helper, `AppError` / codes `INVALID_URL` | `URL_TOO_LONG` | `INVALID_TOKEN` | `RATE_LIMITED` | `NOT_FOUND` | `INTERNAL`
  - **Tests:** unit — logger redacts token-like strings; env missing key throws
  - **Done when:** Units pass; no secret values in example logs; `quality` green
  - **Note (2026-11-26):** `readEnv` requires the four keys from `.env.example` and throws the key name only. Logger redacts `selector.verifier`-shaped strings (each side at least 16 of `A-Za-z0-9_-`) to `[redacted]`; short codes stay. `AppError` codes are the plan’s six codes.
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T7** GitHub Actions workflow for `quality`
  - **Covers:** plan D3
  - **Depends on:** T3, T4, T5
  - **Requires human action:** Push repo to GitHub if not remote; add Actions secrets mirroring Turso/test env; enable Actions
  - **Files / areas:** `.github/workflows/quality.yml` running `npm run quality` with secrets
  - **Tests:** workflow file present; documented that first green run is human-verified on GitHub
  - **Done when:** Workflow committed; human confirms first Actions run (or records blocker if remote absent); local `quality` still green
  - **Note (2026-11-26):** Added `.github/workflows/quality.yml` (push/PR, Node 22, `npm ci`, Playwright Chromium, `db:migrate`, then `npm run quality`) and `docs/ci.md` (secrets + first green run is human-verified). Unit `tests/ci-workflow.test.ts` asserts the workflow file. **Blocker:** no git remote yet — first Actions run not run; human must add GitHub remote, secrets, enable Actions, then confirm the first green run.
  - **Blocker (human):** Git remote absent as of 26/11/2026; Actions first green run pending.
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

## Phase 2 — Story slices

### Domain (shared by US1–US5)

- [x] **T8** URL validation (trim, http(s), max 2048 code points)
  - **Covers:** R2, R3, R4, R5 · AC2, AC3, AC4, AC5 (unit parts)
  - **Depends on:** T3
  - **Files / areas:** `lib/url` (or equivalent) pure functions
  - **Tests:** unit table — empty, whitespace, `javascript:`, bad scheme, uppercase `HTTP`, trim, length 2048 ok / 2049 fail (Unicode code points)
  - **Done when:** Units pass; `quality` green
  - **Note (2026-11-26):** `src/lib/url.ts` `validateOriginalUrl` — trim first; empty → `INVALID_URL`; >2048 code points → `URL_TOO_LONG`; parse via `URL` then scheme `http:`/`https:` only (case-insensitive). Returns trimmed input. Units 10 passed; `quality` green (16 unit, 4 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T9** Short-code generator (Base62 length 8, retry hook)
  - **Covers:** R1, R21 (code uniqueness mechanism)
  - **Depends on:** T3
  - **Files / areas:** `lib/short-code` using `crypto.randomInt`
  - **Tests:** unit — length 8, alphabet only, many samples unique with high probability; collision retry helper invoked when forced
  - **Done when:** Units pass; `quality` green
  - **Note (2026-11-26):** `src/lib/short-code.ts` — `generateShortCode` via `crypto.randomInt` Base62 len 8; `generateUniqueShortCode(isTaken)` max 5 attempts then `INTERNAL`. Units 7 passed; `quality` green (23 unit, 4 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T10** Management token issue and verify (selector + SHA-256 verifier)
  - **Covers:** R9 · plan token decision
  - **Depends on:** T3
  - **Files / areas:** `lib/management-token`
  - **Tests:** unit — issue format `selector.verifier`; verify success; verify fail; timing-safe path; raw token not equal to stored hash
  - **Done when:** Units pass; `quality` green
  - **Note (2026-11-26):** `src/lib/management-token.ts` — CSPRNG 16-byte selector+verifier (base64url); store SHA-256 hex of verifier; `verifyManagementToken` uses `timingSafeEqual` on digests. Units 7 passed; `quality` green (30 unit, 4 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T11** Rate limiter (Turso fixed window + HMAC IP key)
  - **Covers:** R19 · AC16, AC20 (integration)
  - **Depends on:** T5, T6
  - **Files / areas:** `lib/rate-limit`
  - **Tests:** integration — under limit allows; over create 30/hour rejects with English rate-limit and no new link (AC20); over token 10/15min rejects `RATE_LIMITED` (AC16); fail-closed when DB forced down (mock/error injection)
  - **Done when:** Integration tests for AC16 and AC20 pass; `quality` green
  - **Note (2026-11-26):** `src/lib/rate-limit.ts` — fixed window create 30/h, token 10/15min; key HMAC-SHA256(secret, `scope:ip`); English `Too many attempts. Try again later.`; fail-closed → `RATE_LIMITED`. Integration AC16/AC20 limiter parts green; persist “no new link” wired in T12. Units/integration 6 new; `quality` green (36 unit, 4 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

### US1 / US3 — Create without token + result

- [x] **T12** Server Action `createLink` without token (persist link + new token)
  - **Covers:** R1, R8 (server issue), R17, R18 (errors EN codes), R21 · AC15, AC2, AC20 (via limiter on create path)
  - **Depends on:** T5, T6, T8, T9, T10, T11
  - **Files / areas:** `createLink` action, repositories
  - **Tests:** integration — valid https creates row + token hash stored not plaintext; duplicate URL yields two codes (AC15); trimmed/uppercase scheme accepted (AC2); create path enforces bulk-creation limit (AC20)
  - **Done when:** Integration tests pass; `quality` green
  - **Note (2026-11-26):** Core `src/lib/create-link.ts` + repos + `createLinkAction`; rate limit before persist; issues token hash-only; `shortUrl` = `{base}/r/{code}`. Integration 4 passed (AC2/AC15/AC20); `quality` green (40 unit, 4 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T13** Create UI, creation result, copy and token download
  - **Covers:** R1, R8, R18 · AC1, AC3, AC4 (e2e UI parts)
  - **Depends on:** T4, T12
  - **Files / areas:** `/` Create + result view (same flow per plan preference), i18n keys from design §5, shadcn Input/Button/Alert, client download `shortz-management-token.txt`
  - **Tests:** e2e AC1 (short link, token, copy, download, warning); e2e AC3 empty; e2e AC4 bad scheme; loading disables double submit
  - **Done when:** Named e2e pass; `quality` green
  - **Note (2026-11-26):** `CreateForm` + `messages/en.ts` + shadcn Input/Alert; result copy/download `shortz-management-token.txt`; action returns `{ok}`; validate-before-rate-limit. e2e create AC1/AC3/AC4 + loading green; `quality` green (40 unit, 12 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

### US2 — Redirect

- [x] **T14** Route Handler GET `/r/[code]` (302 or not-found)
  - **Covers:** R6, R7, R16 · AC6, AC7 · D6 redirect timing in test
  - **Depends on:** T5, T12
  - **Files / areas:** `app/r/[code]/route.ts` (or page), Not found UI page
  - **Tests:** e2e/integration AC6 302 to original within 500 ms in test env; AC7 unknown code not-found no redirect
  - **Done when:** Tests pass; `quality` green
  - **Note (2026-11-26):** `GET /r/[code]` → 302 original; unknown → 302 `/link-not-found` (Route Handlers cannot rewrite). AC6 timing after warm-up &lt;500ms. e2e AC6/AC7 green; `quality` green (40 unit, 16 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

### US5 / US4 — Token reuse and manage session

- [x] **T15** `createLink` with existing management token
  - **Covers:** R10, R11 · AC9, AC10
  - **Depends on:** T12, T13
  - **Files / areas:** extend `createLink` + Create optional token field UI
  - **Tests:** e2e AC9 add under token without new issued token; e2e AC10 invalid token refuses create
  - **Done when:** E2e pass; `quality` green
  - **Note (2026-11-26):** Valid token → add under existing, `addedToExisting`, no new token; invalid → `INVALID_TOKEN` EN + token rate-limit bucket, no link. e2e AC9/AC10 green; `quality` green (40 unit, 20 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T16** Manage session: `unlockManage` + `logoutManage` + cookie
  - **Covers:** R9, R15, R22 · AC14, AC19 (server parts)
  - **Depends on:** T5, T6, T10, T11
  - **Files / areas:** session cookie helpers, `unlockManage`, `logoutManage`, `manage_sessions` rows (7-day expiry)
  - **Tests:** integration — valid unlock sets HttpOnly cookie attributes in test harness; invalid token same error class twice (AC19); no session blocks list (AC14 server)
  - **Done when:** Integration tests pass; `quality` green
  - **Note (2026-11-26):** Cookie `shortz_manage_session` HttpOnly/SameSite=Lax/Path=/ / Max-Age 7d; unlock inserts `manage_sessions`; `requireManageSession` for AC14; AC19 same `INVALID_TOKEN`. e2e IP fixture for rate-limit isolation. Integration 6 passed; `quality` green (46 unit, 20 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T17** `listLinks` + Manage UI (locked/unlocked/empty)
  - **Covers:** R12, R15, R18 · AC11, AC14
  - **Depends on:** T4, T16, T12
  - **Files / areas:** `/manage`, `listLinks` action, design copy keys
  - **Tests:** e2e AC11 list columns; e2e AC14 without session refused; empty list message
  - **Done when:** E2e pass; `quality` green
  - **Note (2026-11-26):** `/manage` locked/unlocked; `listLinks` + action require session; columns short/destination/created (UTC en-GB). e2e AC11/AC14/empty green; `quality` green (46 unit, 26 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T18** `addLink` from Manage
  - **Covers:** R13, R2–R5 · (AC9 path from manage)
  - **Depends on:** T17, T8
  - **Files / areas:** `addLink` action + Manage add form
  - **Tests:** e2e — unlock, add valid URL, appears in list; invalid URL errors
  - **Done when:** E2e pass; `quality` green
  - **Note (2026-11-26):** `addLink` requires session; same URL rules + create rate limit; Manage add form. e2e add valid/invalid green; `quality` green (46 unit, 30 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T19** `deleteLink` with confirmation dialog
  - **Covers:** R14 · AC12, AC13, AC8
  - **Depends on:** T17, T14
  - **Files / areas:** `deleteLink`, Dialog confirm, hard delete
  - **Tests:** e2e AC12 confirm then list gone and `/r/code` not-found; e2e AC13 cancel keeps redirect
  - **Done when:** E2e pass; `quality` green
  - **Note (2026-11-26):** Hard delete owned links only; shadcn Dialog confirm/cancel; Escape closes. e2e AC12/AC13 green; `quality` green (46 unit, 34 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

## Phase 3 — Hardening

- [x] **T20** Privacy page (English)
  - **Covers:** plan D8; supports R17 retention narrative
  - **Depends on:** T3
  - **Files / areas:** `/privacy` static content per plan (data stored, retention until delete, cookie 7d, no trackers, contact)
  - **Tests:** e2e — page loads 200 and states retention/no accounts; link from footer/nav if design allows (add minimal footer link)
  - **Done when:** E2e pass; `quality` green
  - **Note (2026-11-26):** Static `/privacy` (EN) per D8; footer Privacy link in layout. e2e 200 + retention/no accounts + footer; `quality` green (46 unit, 38 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T21** Security headers middleware
  - **Covers:** plan W9 headers
  - **Depends on:** T3
  - **Files / areas:** Next middleware or `headers` in config
  - **Tests:** e2e or integration — response includes `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, CSP present
  - **Done when:** Header assertions pass; `quality` green
  - **Note (2026-11-26):** Headers via `next.config.ts` `headers()` (plan W9; Next 16 middleware→proxy deprecated). e2e assert XFO/XCTO/RP/CSP/Permissions-Policy; `quality` green (46 unit, 40 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T22** Logging AC17/AC21 and correlation id on actions
  - **Covers:** R20 · AC17, AC21
  - **Depends on:** T6, T12, T16
  - **Files / areas:** action logging hooks
  - **Tests:** integration AC17 — captured logs on create/unlock never contain full management token; integration AC21 — same logs never contain full original URL
  - **Done when:** AC17 and AC21 green; `quality` green
  - **Note (2026-11-26):** createLink/unlockManage log success/fail with correlationId + shortCode/errorCode; actions pass logger+UUID. Logger also redacts URL-like strings. Integration AC17/AC21 green; `quality` green (50 unit, 40 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T23** No automatic expiry (AC18)
  - **Covers:** R17 · AC18
  - **Depends on:** T12, T14, T16
  - **Files / areas:** confirm schema has no link TTL; test only
  - **Tests:** integration AC18 — after manipulating clock/session still redirect+list for non-deleted link (sessions may expire at 7d; link itself does not)
  - **Done when:** AC18 green; `quality` green
  - **Note (2026-11-26):** Test-only; schema already has no link/token TTL. Integration: +400d clock — old session expires, fresh unlock+list and redirect still work. `quality` green (52 unit, 40 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T24** Accessibility axe pass + manual keyboard checklist
  - **Covers:** C7 / profile gate 6; R18 UI
  - **Depends on:** T13, T17, T14, T19
  - **Files / areas:** e2e a11y specs; `docs` or `specs/001.../keyboard-check.md` note
  - **Tests:** axe on Create, Manage, Not found (wcag2a/aa); manual checklist file filled (tab order, focus visible, dialog escape)
  - **Done when:** Axe e2e green; checklist committed; `quality` includes a11y e2e; gate 6 satisfiable
  - **Note (2026-11-26):** `e2e/a11y.spec.ts` axe wcag2a/aa on Create/Manage/Not found; `keyboard-check.md` filled (tab/focus/Escape). No UI code change. `quality` green (52 unit, 46 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T25** Dependency audit in `quality`
  - **Covers:** profile gate 7
  - **Depends on:** T3
  - **Files / areas:** `npm audit --audit-level=high` (or equivalent) in `quality`
  - **Tests:** script fails on high severity
  - **Done when:** `quality` runs audit; no known high issues (or waivers documented)
  - **Note (2026-11-26):** `npm run audit` (`--audit-level=high`) in `quality` before build. No high/critical; 4 moderate (esbuild via drizzle-kit) noted, not waived (below gate). Unit script asserts; `quality` green (54 unit, 46 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T26** Deploy to Vercel Hobby and production smoke
  - **Covers:** plan §12 rollout; R6/R1 live
  - **Depends on:** T7, T13, T14, T17, T19, T20, T21, T24, T25
  - **Requires human action:** Create/link Vercel project; set env secrets; run migrate on prod Turso; deploy; optional custom domain later (D2 out)
  - **Files / areas:** brief `docs/deploy.md` or profile note with rollback (revert deploy + Turso PITR)
  - **Tests:** manual smoke checklist: create → open → manage → delete → privacy; record result in verification prep note
  - **Done when:** Human confirms production smoke; rollback steps written
  - **Note (2026-11-26):** `docs/deploy.md` (rollback: Vercel revert + Turso PITR) + `verification-prep.md` template. Human approved T26; **production smoke checklist still blank** in verification-prep (URL/result TBD) — fill before `/nodfirst-verify` if deploy is live.
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T27** Finalize profile Commands and gate 9 note
  - **Covers:** profile §5–6 completeness
  - **Depends on:** T3, T4, T25
  - **Files / areas:** `project/profile.md` §5 full (`quality` = all gates 1–7); §6 gate 9 note for soft D6 targets
  - **Tests:** none (doc); spot-check `npm run quality` listed accurately
  - **Done when:** Profile Commands match scripts; no TBD left for set-up/quality
  - **Note (2026-11-26):** Profile §5 lists quality = lint→typecheck→test→e2e→audit→build (gates 1–7); §6 gate 9 soft D6 targets. No TBD in profile Commands. Spot-check scripts match; `quality` green.

## Phase 4 — Verification run 1

- [x] **T28** Prove list, add, and delete refuse the wrong caller
  - **Covers:** R14, R15 · AC14
  - **Depends on:** T19
  - **Files / areas:** new integration test file under `tests/` only. No production change unless one of these tests fails.
  - **Tests:** integration — `listLinks` with no session id is refused and returns no items; `addLink` with no session id is refused and inserts no row; `deleteLink` with no session id is refused and the link still exists; `deleteLink` with token B’s session and token A’s short code returns `NOT_FOUND` and token A’s link still resolves
  - **Done when:** removing the session check or the owner check makes one of these tests fail; `npm run quality` is green
  - **Note (2026-11-26):** Added `tests/manage-authz.test.ts` (4 integration). Production already had session + owner checks; no production change. `quality` green (58 unit, 46 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T29** [P] Resume Manage when the session cookie is still valid
  - **Covers:** R15 · spec §6 Manage (“continue a management session”)
  - **Depends on:** T17
  - **Files / areas:** `src/app/manage/page.tsx`, `src/components/manage-form.tsx`, new e2e
  - **Tests:** e2e — after unlock, a reload of `/manage` still shows that token’s list and does not show the raw token; a visit with no cookie still shows only the locked form (existing AC14 e2e stays green)
  - **Done when:** the new e2e fails if reload always shows the locked form; `npm run quality` is green
  - **Note (2026-11-26):** `/manage` reads the session cookie in a Suspense child and passes `initialUnlocked` / `initialItems` to `ManageForm`. e2e `manage-resume.spec.ts`. `quality` green (58 unit, 48 e2e). `/manage` is partial prerender.
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T30** Show the English offline message when a request does not reach the server
  - **Covers:** spec §6 Create and Manage offline states · R18
  - **Depends on:** T29
  - **Files / areas:** `src/components/create-form.tsx`, `src/components/manage-form.tsx`, `src/messages/en.ts` (add design key `manage.errorOffline`; `create.errorOffline` is already there)
  - **Tests:** e2e — abort the create request: the visitor sees “You appear to be offline. Check your connection and try again.” and no short link is created; abort the Manage unlock request: the visitor sees “You appear to be offline. Check your connection and try again.”
  - **Done when:** both e2e fail if the catalogue sentence is not shown; `npm run quality` is green
  - **Note (2026-11-26):** Added `manage.errorOffline`; create/unlock catch network failures. e2e `offline.spec.ts` (2). Raised AC20 rate-limit test timeout to 60s (Turso latency; same as create-link AC20). `quality` green (58 unit, 52 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T31** Generic server-error screen with no internal detail
  - **Covers:** spec §6 generic server error · design keys `error.serverTitle`, `error.server`, `error.retry` · R18
  - **Depends on:** T30
  - **Files / areas:** `src/app/error.tsx`, `src/messages/en.ts` (add the two missing design keys; `error.server` is already there)
  - **Tests:** unit — render the error view with `react-dom/server` `renderToStaticMarkup` (already a dependency; do not add a package). Pass an Error whose message is a fake internal string. The HTML contains “Something went wrong”, “Please try again. If the problem continues, try later.”, and “Try again”, and does not contain the fake internal string.
  - **Done when:** the unit test fails if the internal message is shown or a design sentence is removed; `npm run quality` is green
  - **Note (2026-11-26):** `src/app/error.tsx` (Next 16 `retry` prop); keys `error.serverTitle` / `error.retry`. Unit `tests/error-screen.test.ts`. Vitest `@` alias for the unit import. `quality` green (59 unit, 52 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

- [x] **T32** Stop trusting the first forwarded header for IP, Secure, and short-link host
  - **Covers:** R19 · AC16, AC20 · plan session cookie (`Secure`) · plan decision “Trusted request metadata (CR-1)”
  - **Depends on:** T30
  - **Files / areas:** one shared helper, then `src/app/actions/create-link.ts`, `src/app/actions/add-link.ts`, `src/app/actions/manage-session.ts`, `src/app/actions/list-links.ts`, and `e2e/fixtures.ts` in the same task
  - **Rule (CR-1 option C):** Rate-limit IP is the last address of `x-vercel-forwarded-for` when that header is present; otherwise `x-real-ip` when present; otherwise the last address of `X-Forwarded-For`; otherwise `unknown`. Never the first address of a list. `Secure` is true only when the last `x-forwarded-proto` value is `https`; when that header is missing, `Secure` is true only if `NODE_ENV` is `production`. The short-link host is the `host` header only, never `x-forwarded-host`.
  - **Tests:** unit — a caller-supplied first hop in `X-Forwarded-For`, `X-Forwarded-Proto`, or `X-Forwarded-Host` does not choose the rate-limit IP, the cookie `Secure` flag, or the short-link host when a later trusted value is present. Keep distinct rate-limit buckets in parallel e2e: a single `x-forwarded-for` address is already the last hop when `x-vercel-forwarded-for` is absent; change `e2e/fixtures.ts` only if those requests would otherwise share `unknown`.
  - **Done when:** the new unit tests fail if the first hop is trusted; existing e2e still pass; `npm run quality` is green
  - **Note:** no new dependency.
  - **Note (2026-11-26):** `src/lib/request-meta.ts`; wired into create/add/list/manage actions and `/manage` page. e2e fixtures keep a single XFF (last hop). Unit `tests/request-meta.test.ts` (8). `quality` green (67 unit, 52 e2e). Fresh env: `rm -rf node_modules .next && npm ci && npm run quality` green (67 unit, 52 e2e).
  - **Accepted by:** Luca Lanzano · Date: 26/11/2026

## Traceability check

| Requirement / AC | Tasks | Test |
|------------------|-------|------|
| R1 | T12, T13, T9 | integration create; e2e AC1 |
| R2 | T8, T12, T18 | unit AC2/AC4; e2e AC4 |
| R3 | T8, T13 | unit AC3/AC4; e2e AC3/AC4 |
| R4 | T8, T12 | unit/integration AC2 |
| R5 | T8 | unit AC5 |
| R6 | T14 | e2e AC6 |
| R7 | T14, T19 | e2e AC7, AC8 |
| R8 | T12, T13 | e2e AC1 |
| R9 | T10, T16 | unit token; integration session |
| R10 | T15 | e2e AC9 |
| R11 | T15, T16 | e2e AC10; integration unlock |
| R12 | T17 | e2e AC11 |
| R13 | T18 | e2e add from manage |
| R14 | T19, T28 | e2e AC12, AC13, AC8; integration cross-token delete |
| R15 | T16, T17, T28, T29 | e2e AC14; integration; e2e reload keeps the list |
| R16 | T14 | e2e AC6 |
| R17 | T12, T23 | integration AC18 |
| R18 | T13, T17, T20, T30, T31 | e2e copy/UI language; offline e2e; error-screen unit |
| R19 | T11, T12, T16, T32 | integration AC16, AC20; unit forwarded-header |
| R20 | T6, T22 | unit redact; integration AC17, AC21 |
| R21 | T9, T12 | unit; integration AC15 |
| R22 | T16 | integration AC19 |
| AC1 | T13 | e2e AC1 |
| AC2 | T8, T12 | unit + integration |
| AC3 | T8, T13 | unit + e2e |
| AC4 | T8, T13 | unit + e2e |
| AC5 | T8 | unit |
| AC6 | T14 | e2e |
| AC7 | T14 | e2e |
| AC8 | T19 | e2e |
| AC9 | T15 | e2e |
| AC10 | T15 | e2e |
| AC11 | T17 | e2e |
| AC12 | T19 | e2e |
| AC13 | T19 | e2e |
| AC14 | T16, T17, T28, T29 | integration + e2e + reload |
| AC15 | T12 | integration |
| AC16 | T11, T32 | integration; unit forwarded-header |
| AC17 | T22 | integration |
| AC18 | T23 | integration |
| AC19 | T16 | integration |
| AC20 | T11, T12, T32 | integration; unit forwarded-header |
| AC21 | T22 | integration |
| Plan D1 Turso | T2, T5 | migrate test |
| Plan D3 CI | T7 | Actions |
| Plan D6 soft perf | T14 | 500 ms assert |
| Plan D7 browsers | T4 | Chromium (+ mobile project) |
| Plan D8 privacy | T20 | e2e page |
| Plan D9 Drizzle | T5 | migrate |
| Plan headers | T21 | header assert |
| Plan deploy | T26 | manual smoke |
| Spec §6 offline | T30 | e2e aborted create and unlock |
| Spec §6 server error | T31 | unit render, no internal string |
| Verification F1 headers | T32 | unit forwarded-header |

## Notes / blockers
- Firefox/WebKit not in `quality` (plan D7 option B gap).
- T7: workflow is in the repo; first GitHub Actions green run is blocked until a remote exists, Actions secrets are set, and a human confirms the run. Local `quality` is green without that.
- T26 still needs human consoles (Vercel deploy).
- Exact `drizzle-kit` / `@libsql/client` / React patch pins chosen at install with `npm view` and recorded in the implementing commit message or task note.
- Verification F11 (production smoke) and F12 (GitHub Actions run) stay on T7 and T26. No new code task for them.
- T32 follows plan decision “Trusted request metadata (CR-1)”, option C, decided 26/11/2026.

## Open questions
- None. CR-1 is decided: option C, in the plan.

## Interpretations
- Creation result stays in the Create flow (no separate `/created` route required).
- Token download is a client-side blob named `shortz-management-token.txt` (plan), not a authenticated GET API.
- Manage unlocked UI does not re-display the full token (design). The resumed list in T29 follows that: the raw token is not shown again.
- `quality` grows as gates come online; T27 makes profile match the final script.
- AC18 tests link non-expiry; manage session may still expire after 7 days per plan.
- This revision does not add a task for the framework `/_not-found` page. Verification F3 also mentioned it; the request for this revision was only the offline sentence and the generic server-error screen.
- “Offline” in T30 means the create or unlock call is aborted before a normal result. The visitor then sees the design sentence.
- Create and Manage share that one offline rule, so they are one task (T30). The server-error screen is a different screen, so it is T31.
- T28 adds tests only. Production code changes in that task only if a new test fails.
- T31’s render test uses `react-dom/server`, already depended on by Next. No new package.
- T32 implements option C of CR-1. The human chose that rule on 26/11/2026. It is copied in the task and in the plan.

## Approval
- Approved by: Luca Lanzano
- Date: 26/11/2026
