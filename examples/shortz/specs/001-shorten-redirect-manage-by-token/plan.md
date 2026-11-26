# Plan 001: Shorten, redirect, manage by token

- **Spec:** `specs/001-shorten-redirect-manage-by-token/spec.md`
- **Design:** `specs/001-shorten-redirect-manage-by-token/design.md`
- **Status:** Approved
- **Last updated:** 2026-11-26

## 1. Summary

Greenfield Next.js App Router app on Vercel Hobby, data on Turso (libSQL) via Drizzle. Visitors create short links and manage them with a high-entropy management token (selector + hashed verifier); Manage stays open via an HttpOnly session cookie (7 days). Mutations use Server Actions; short-link opens use a Route Handler with HTTP 302. Tests: Vitest (unit/integration against Turso), Playwright Chromium e2e + axe; one local `quality` script mirrored in GitHub Actions.

## 2. Constitution check

| Rule | Compliance / note |
|------|-------------------|
| C1 Spec is source of truth | Plan implements only Approved spec 001 + design 001; no extra product behaviour |
| C2 Human approval gates | Gate respected: no later step before human approval |
| C3 Do not invent requirements | Product rules from spec; tech from recorded decisions below |
| C4 Traceability | Interfaces and tests cite R/AC IDs |
| C5 Tests | see Section 8 |
| C6 Security & privacy | see Section 7 |
| C7 Accessibility | WCAG 2.2 AA; axe in e2e + manual keyboard check (profile gate 6); design §6 |
| C8 Simplicity / dependencies | see Section 10; pinned versions; no Redis |
| C9 Small verifiable increments | Section 15 steps leave quality green |
| C10 Architectural decisions | Section 4 |
| C11 Specs stay alive | Behaviour changes require spec Mode B first |
| C12 Language | UI EN (design keys); identifiers EN; agent may speak IT |
| C13 Brevity | Template sections kept; no duplication of design copy |
| C14 Independent verification | `verify` after the last task |

## 3. Technical context

- **Touched areas:** new app root (Next.js), DB schema/migrations, Server Actions, redirect route, UI screens from design, i18n catalogue, privacy page, quality/CI scripts.
- **Existing code/modules reused:** none (greenfield).
- **Constraints:** Node ≥ 22, npm, Vercel Hobby, Turso Free, profile modules web+backend.
- **Machine tools (verify before implement):**
  - `node -v` (≥ 22)
  - `npm -v`
  - `git --version`
  - After scaffold: `npx tsc --version`, `npx playwright --version`
- **Env secrets (never committed):** `TURSO_DATABASE_URL`, `TURSO_AUTH_TOKEN`, `RATE_LIMIT_SECRET`, `SESSION_SECRET` (for signing/session ids as needed).

## 4. Decisions

### Decision: D1 Data store on Vercel
- **Context:** No persistent local SQLite on serverless; profile wants SQLite-compatible + remote later.
- **Options:** A) Turso/libSQL B) Neon Postgres C) Local file only
- **Decision:** A — Turso Free, SQL over HTTP; `@libsql/client` (`/web` in serverless). Same remote kind in local/CI/prod (test DB allowed).
- **Consequences:** Human creates Turso DB + Vercel env; migrations via drizzle-kit dialect `turso`.
- **Verified:** 2026-11-26 — turso.tech/pricing, docs.turso.tech/integrations/vercel

### Decision: D9 ORM
- **Context:** Typed access + migrations on Turso.
- **Options:** A) Drizzle B) Prisma C) raw client
- **Decision:** A — `drizzle-orm@0.45.4`, `drizzle-kit` compatible (candidate `0.31.11`, confirm with `npm view` at install), `@libsql/client` pinned at install.
- **Consequences:** Schema in TS; `db:generate` / `db:migrate` scripts.
- **Verified:** 2026-11-26 — docs.turso.tech/sdk/ts/orm/drizzle, npm drizzle-orm 0.45.4

### Decision: Management token storage (A2)
- **Context:** R9/C6 non-reversible storage; high-entropy token.
- **Options:** A) selector+verifier B) full-token SHA-256 C) Argon2
- **Decision:** A — CSPRNG; token shown as `selector.verifier`; store `selector` + SHA-256(verifier); `timingSafeEqual`.
- **Consequences:** Lookup by selector; ≥128-bit verifier entropy.

### Decision: Manage session (R15)
- **Context:** Design unlock without re-displaying full token.
- **Options:** A) HttpOnly cookie session B) resend token C) localStorage
- **Decision:** A — cookie `HttpOnly; Secure; SameSite=Lax; Path=/`; Max-Age **7 days**; server row session id → management_token_id; mutations via **Server Actions** (Origin/Host CSRF). Lifetime choice: 7 days.
- **Consequences:** Cookie is not the capability alone; validate session server-side every action.

### Decision: Rate limiting (R19)
- **Context:** Shared counters on serverless.
- **Options:** A) Turso counters B) Upstash Redis C) memory only
- **Decision:** A — fixed window; key = HMAC-SHA256(IP, `RATE_LIMIT_SECRET`); create **30/hour**; invalid/unlock token **10/15 min**; fail closed if limiter unavailable. Which value is the client IP: decision “Trusted request metadata (CR-1)” below.
- **Consequences:** `rate_limits` table; opportunistic cleanup of expired rows.

### Decision: Trusted request metadata (CR-1)
- **Context:** Verification 001 run 1, finding F1. The caller can send the first hop of `X-Forwarded-For`, `X-Forwarded-Proto`, and `X-Forwarded-Host`. On Vercel those platform headers are rewritten, but the app must not treat the first caller hop as the client.
- **Options:** A) `x-real-ip` only B) last `X-Forwarded-For` hop C) the rule below
- **Decision:** C — Rate-limit IP is the last address of `x-vercel-forwarded-for` when that header is present; otherwise `x-real-ip` when present; otherwise the last address of `X-Forwarded-For`; otherwise `unknown`. Never the first address of a list. The manage cookie `Secure` flag is true only when the last `x-forwarded-proto` value is `https`. When that header is missing, `Secure` is true only if `NODE_ENV` is `production`. The short-link host is the `host` header only, never `x-forwarded-host`.
- **Consequences:** One shared helper for create, add, unlock, and list. End-to-end tests may keep a single `x-forwarded-for` address per worker when `x-vercel-forwarded-for` is absent, because that single address is the last hop. No new dependency.
- **Decided by:** Luca Lanzano · Date: 26/11/2026

### Decision: Short codes
- **Context:** Unique public codes (R1, R21).
- **Options:** A) crypto.randomInt Base62 len 8 B) nanoid C) sequential
- **Decision:** A — UNIQUE + retry ≤5 then 500.
- **Consequences:** Path `/r/[code]`; no new dep.

### Decision: D7 Browsers
- **Options:** A) e2e 3 engines B) support 3, e2e Chromium C) Chromium only
- **Decision:** B — support Chromium/Firefox/WebKit evergreen last 2 majors; viewport 360–1440; e2e Chromium desktop + one mobile emulation; Firefox/WebKit gap until added to `quality`.
- **Verified:** 2026-11-26 — Playwright 1.65.1 browsers

### Decision: D6 Performance
- **Decision:** A — redirect p95 TTFB &lt; 500 ms in test/deploy region; Create LCP soft &lt; 2.5 s mid-range lab; JS transfer soft &lt; 300 KB gzip. Gate 9: document + optional smoke; e2e asserts 302 within 500 ms in test env.

### Decision: D8 Privacy
- **Decision:** A — English `/privacy` page; retention = until user delete; sessions 7d; rate-limit rows for window; no trackers; Turso Free PITR ~1 day accepted risk.
- **Note:** Not legal advice; operator (Luca Lanzano) owns final wording.

### Decision: D3 CI
- **Decision:** A — `npm run quality` locally and on GitHub Actions (push/PR); Vercel deploy separate.
- **Requires human action:** GitHub remote + Actions enable if missing.

### Decision: Test tooling + download + redirect status
- **Decision:** Vitest `5.1.1` (prefer over 5.1.2 &lt;7d), Playwright `@playwright/test@1.65.1`, `@axe-core/playwright@4.13.0`; token download `shortz-management-token.txt` (one line); redirect **302**.
- **Verified:** 2026-11-26 — npm vitest/playwright/axe dates as cited in plan interview.

### Decision: App framework pin
- **Decision:** `next@16.4.6`, matching `eslint-config-next@16.4.6`, React 19.x pinned together at scaffold (`npm view` for exact react patch). App Router + Server Actions + Route Handler for redirect only.
- **Verified:** 2026-11-26 — npm next 16.4.6

### Decision: Security headers (W9)
- **Decision:** Middleware/headers: HTTPS on Vercel; `Content-Security-Policy` (default-src self; tighten as UI needs); `X-Frame-Options: DENY`; `X-Content-Type-Options: nosniff`; `Referrer-Policy: strict-origin-when-cross-origin`; `Permissions-Policy` minimal. No non-essential third-party scripts.
- **Interpretation:** Chosen as plan defaults for W9; approving this plan accepts them.

### Decision: UI kit
- **Decision:** shadcn/ui (profile) on light theme; map design components to shadcn primitives; exact shadcn CLI component set chosen in implement tasks (Button, Input, Label, Alert, Dialog, etc.).

## 5. Data model

**management_tokens**
- `id` (PK)
- `selector` (unique text)
- `verifier_hash` (blob/text hex of SHA-256)
- `created_at` (UTC)

**links**
- `id` (PK)
- `short_code` (unique, 8 base62)
- `original_url` (text, ≤2048)
- `created_at` (UTC)
- `management_token_id` (FK → management_tokens)
- Hard delete on user delete (R14)

**manage_sessions**
- `id` (PK, random session id stored in cookie)
- `management_token_id` (FK)
- `expires_at` (UTC, now+7d)
- `created_at`

**rate_limits**
- `key` (PK, hex HMAC)
- `count` (int)
- `reset_at` (UTC)

Ownership: rows “belong” to the management token secret; no user accounts. Migrations: versioned SQL via drizzle-kit; apply on empty DB in CI; rollback = restore Turso backup / re-migrate forward (document in tasks).

## 6. Interfaces and contracts

Machine error codes (EN): `INVALID_URL`, `URL_TOO_LONG`, `INVALID_TOKEN`, `RATE_LIMITED`, `NOT_FOUND`, `INTERNAL`.

| Interface | Purpose | Input → Output / errors | Auth | Covers |
|-----------|---------|--------------------------|------|--------|
| Server Action `createLink` | Create short link | `{ url, managementToken? }` → `{ shortUrl, managementToken? issued, addedToExisting }` / validation, INVALID_TOKEN, RATE_LIMITED | Public + optional token | R1–R5, R8, R10–R11, R18–R19, R21 |
| Server Action `unlockManage` | Start manage session | `{ managementToken }` → set cookie / INVALID_TOKEN, RATE_LIMITED | Token | R11, R15, R19, R22 |
| Server Action `listLinks` | List links | (session) → `{ items: [{ shortUrl, originalUrl, createdAt }] }` | Session | R12, R15 |
| Server Action `addLink` | Add under session | `{ url }` → new item / validation, RATE_LIMITED | Session | R2–R5, R13 |
| Server Action `deleteLink` | Permanent delete | `{ shortCode }` + confirm client-side → ok / NOT_FOUND | Session | R14 |
| Server Action `logoutManage` | Clear session | → clear cookie | Session optional | R15 |
| GET `/r/[code]` | Redirect or not found | → **302** Location original / Not found page | Public | R6, R7, R16 |
| Pages `/`, `/manage`, result UI, `/privacy`, error | UI | per design | — | design + R18 |
| GET token download | Optional download | text/plain attachment filename `shortz-management-token.txt` | Issued token in client only (blob from UI) | R8 |

Caller example (create): submit URL without token → response includes `shortUrl` and new `managementToken` once.

## 7. Security and privacy

| Spec point | Mechanism | How tested |
|------------|-----------|------------|
| Access create/open public; manage by token/session | Actions check session/token server-side; cookie HttpOnly | integration + e2e AC11–AC14 |
| R19 abuse | Turso rate_limits; HMAC IP key | integration AC16 (token guess), AC20 (bulk create); unit keying |
| R22 / R7 leaks | Same invalid-token message; same not-found page | e2e AC7–AC8, AC19 |
| R17 no expiry | No TTL job on links | AC18 integration |
| Input limits R2–R5 | Server validation after trim; max 2048 code points | unit + AC3–AC5 |
| R20 logging | Structured logs: short_code, error codes, correlation id; never full token or full original URL | unit/integration AC17 (token), AC21 (original URL) |
| Token secrets | SHA-256 verifier; CSPRNG; Secure cookie | unit hash/verify |
| Transport | Vercel HTTPS | deploy checklist |
| Headers | Section 4 decision | smoke / header assert in e2e optional |
| Personal data | Privacy page; delete removes link row | manual + e2e delete |
| OWASP Top 10 / API | Validation, rate limit, CSP, no SSRF via blocking non-http(s); redirect only to stored URL | review + tests |
| Client-controlled values | IP/UA never sole authz; session id looked up server-side | review |
| CSRF | Server Actions Origin/Host | rely on Next 16.4.6; pin version |

## 8. Test strategy

Infrastructure: Vitest 5.1.1; Playwright 1.65.1; axe 4.13.0; Turso test database (same driver as prod).

| AC | Level | Test description (fails if…) |
|----|-------|------------------------------|
| AC1 | e2e | Create https URL → missing short link, token, copy, warning, or download control |
| AC2 | integration/unit | Uppercase scheme + spaces not accepted / not trimmed |
| AC3 | unit + e2e | Empty/whitespace creates a link |
| AC4 | unit + e2e | `javascript:` or non-URL accepted |
| AC5 | unit | URL length 2049 code points accepted |
| AC6 | e2e | Valid short link does not 302 to original |
| AC7 | e2e | Unknown code does not show not-found / redirects |
| AC8 | e2e | After delete, short link still redirects |
| AC9 | e2e | Create with token issues a different new token or omits from list |
| AC10 | e2e | Invalid token still creates link |
| AC11 | e2e | Unlock does not list short/original/created |
| AC12 | e2e | Confirm delete leaves link working |
| AC13 | e2e | Cancel delete removes link |
| AC14 | e2e | List/delete without session succeeds |
| AC15 | integration | Two creates same URL share short_code |
| AC16 | integration | Over-limit invalid-token attempts still succeed |
| AC17 | integration | Logs contain full management token |
| AC18 | integration | Artificial “time passed” still allows redirect+list (no expiry field enforced) |
| AC19 | integration | Two invalid tokens get different error classes |
| AC20 | integration | Over-limit create attempts still create a short link or omit English rate-limit error |
| AC21 | integration | Routine logs for create/manage contain a full original URL |

Critical flows (spec §5) = Playwright e2e. Axe on Create, Manage, Not found (wcag2a/aa tags). Manual keyboard checklist recorded once per UI task.

## 9. UI and UX

Follow `design.md` (Approved). Routes: `/` Create; success state on same flow or `/created` (implementer picks one; prefer same-flow result view); `/manage`; `/r/[code]`; `/privacy`; generic error UI. i18n: design §5 keys in a message module (EN only v1). shadcn light theme. Offline: network error strings only.

## 10. Dependencies

| Dependency | Why | Alternatives considered |
|------------|-----|-------------------------|
| `next@16.4.6` | App + hosting target | Remix, plain Node |
| `react` / `react-dom` 19.x (pin) | Next 16 | — |
| `drizzle-orm@0.45.4` + `drizzle-kit` | ORM/migrations Turso | Prisma, raw SQL |
| `@libsql/client` (pin) | Turso driver | — |
| shadcn/ui + tailwind (pins from CLI) | Profile UI | raw CSS |
| `vitest@5.1.1` | Unit/integration | Jest |
| `@playwright/test@1.65.1` | E2E | Cypress |
| `@axe-core/playwright@4.13.0` | A11y automation | manual only |
| `eslint` + `eslint-config-next@16.4.6` | Lint gate | — |
| `typescript` (pin with Next) | Types | — |

No nanoid, no Redis.

## 11. Risks and mitigations

| Risk | Likelihood / impact | Mitigation |
|------|---------------------|------------|
| Turso/libSQL write contention | Med / med | Single DB; short transactions; monitor |
| Session fixation / CSRF | Low / high | HttpOnly cookie; Server Actions; regenerate session id on unlock |
| Short code enumeration | Low / med | 8 char base62; rate limit |
| Lost token | Accepted | Warning + download; no recovery (spec) |
| W7 Firefox/WebKit untested in CI | Med / low | Documented gap (D7 B); add later |
| Secrets in Vercel | Med / high | Human action checklist; never commit `.env` |

## 12. Rollout and migration

1. Human: Turso DB, tokens, Vercel project, GitHub remote, env vars.  
2. Migrate schema on Turso.  
3. Deploy Hobby.  
4. Smoke: create → open → manage → delete; privacy page.  
5. Rollback: revert deploy on Vercel; DB restore via Turso PITR if migration bad.

## 13. Open questions

None — all handoff deferrals resolved in Section 4 (or accepted as plan defaults for headers).

## 14. Approval

- Approved by: Luca Lanzano
- Date: 26/11/2026

## 15. Planned steps (indicative; tasks may split)

1. Scaffold Next 16.4.6 + TS + ESLint + Tailwind/shadcn; scripts `lint`, `typecheck`, `test`, `test:e2e`, `build`, `quality` (all gates).  
2. Wire env validation; Turso client; Drizzle schema + first migration; migrate empty DB.  
3. Domain: URL validate, short code, token hash/verify, rate limit.  
4. Server Actions + redirect route + session cookie.  
5. UI screens + i18n keys from design + privacy page.  
6. Tests for AC mapping; axe; manual keyboard note.  
7. Security headers middleware.  
8. GitHub Actions workflow = `quality`.  
9. Human deploy + smoke; document commands in `project/profile.md` §5.

## 16. Impact on other specs and plans

N/A — first feature.

## 17. Change log

| Date | Change |
|------|--------|
| 2026-11-26 | Align to spec Mode B: AC20 (bulk create rate limit), AC21 (no full original URL in routine logs) in §7–§8; status Draft pending re-approval |
| 2026-11-26 | CR-1 option C: trusted request metadata for rate-limit IP, cookie Secure, and short-link host. Decided by Luca Lanzano |
