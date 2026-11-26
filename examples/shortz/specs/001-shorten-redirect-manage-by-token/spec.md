# Spec 001: Shorten, redirect, manage by token

- **Status:** Approved
- **Track:** Full
- **Last updated:** 2026-11-26

## 1. Goal

People who share long URLs (for example on social media) need a short, reliable link. This feature lets anyone create a short link that redirects to an allowed original URL, keep several links under one management token without an account, and view, add, or permanently delete those links. It is the first deliverable of Shortz v1.

## 2. User stories

- **US1.** As a visitor, I want to paste a long http(s) URL and get a short link so that I can share it easily.
- **US2.** As anyone who opens a short link, I want to be taken to the original URL so that the short link is useful.
- **US3.** As a creator, I want a management token shown after creation (with copy and optional download, plus a clear warning that it cannot be recovered) so that I can manage my links later.
- **US4.** As a creator with a management token, I want to list, add, and permanently delete links tied to that token so that I can keep my set of short links under control without an account.
- **US5.** As a creator, I want to reuse the same management token when I create another link so that all my links stay in one list.

## 3. Requirements

| ID | Requirement | Story |
|----|-------------|-------|
| R1 | The system MUST let a visitor submit an original URL and, when it is accepted, create a short link that resolves to that URL. | US1 |
| R2 | The system MUST accept only original URLs whose scheme is `http` or `https` (case-insensitive). | US1 |
| R3 | The system MUST reject an original URL that is empty, only whitespace, not a URL, or uses any other scheme, and MUST show a clear English error without creating a short link. | US1 |
| R4 | Before validating the URL, the system MUST trim leading and trailing whitespace from the submitted original URL. | US1 |
| R5 | The system MUST reject an original URL longer than 2048 characters after trimming (length counted in Unicode code points) and MUST NOT create a short link. | US1 |
| R6 | Opening a valid short link MUST redirect the visitor to the stored original URL. | US2 |
| R7 | Opening a short link that does not exist or has been deleted MUST show a clear English “not found” result and MUST NOT redirect to an original URL. | US2 |
| R8 | After a successful creation without a management token, the system MUST show a new management token, the short link, a way to copy the token, an optional way to download the token, and an explicit English warning that a lost token cannot be recovered. | US3 |
| R9 | The management token MUST be a secret capability: possession alone authorises listing, adding, and deleting links for that token; the system MUST NOT provide any recovery path for a lost token. | US3, US4 |
| R10 | When the visitor submits a valid original URL together with a valid existing management token, the system MUST create the short link under that token and MUST NOT issue a different management token for that creation. | US5 |
| R11 | When the visitor submits a management token that is not recognised, the system MUST refuse creation (or management actions) with a clear English error and MUST NOT create a short link under a silently substituted new token. | US4, US5 |
| R12 | Given a valid management token, the system MUST show the list of short links tied to it, each with at least: short link, original URL, and creation date/time. | US4 |
| R13 | Given a valid management token, the system MUST allow adding a new short link (same acceptance rules as R2–R5) under that token. | US4 |
| R14 | Given a valid management token, the system MUST allow permanently deleting a short link tied to that token after an explicit confirmation step in the UI; after deletion, that short link MUST behave as in R7. | US4 |
| R15 | The system MUST NOT allow listing, adding, or deleting links for a token without presenting that token (or an equivalent secret proof of possession established for the current management session). | US4 |
| R16 | Short links MUST remain reachable by anyone who knows them until deleted; management status MUST NOT be required to open a short link. | US2 |
| R17 | Short links and management tokens MUST have no expiry time in this feature (they remain valid until deleted or until a later product decision changes retention). | US2, US4 |
| R18 | User-facing text for this feature MUST be in English. | US1–US5 |
| R19 | The system MUST protect management-token guessing and bulk creation with limits on repeated attempts (exact thresholds deferred to the plan; behaviour when limited: clear English error, no silent success). | US4 |
| R20 | Application logs MUST NEVER contain a full management token. Short codes MAY be logged. Full original URLs MUST NOT be written to routine application logs. | US3, US4 |
| R21 | Creating the same original URL more than once MUST produce a distinct short link each time (no silent reuse of an existing short link). | US1 |
| R22 | For unknown or disallowed management actions, the system MUST NOT reveal whether a different token or short link exists beyond what is needed for the clear error of the attempted action (invalid token → same class of error whether or not other tokens exist). | US4 |

## 4. Acceptance criteria

| ID | Criterion | Covers | Test |
|----|-----------|--------|------|
| AC1 | Given a visitor on the create view with a valid `https` URL within length limits and no management token, when they submit, then a short link is created and they see the short link, a new management token, a copy control, an optional download control, and a warning that the token cannot be recovered if lost. | R1, R2, R8, R18 | |
| AC2 | Given a visitor submitting a valid `HTTP` URL (uppercase scheme) after accidental leading/trailing spaces, when they submit, then the URL is accepted (scheme treated case-insensitively; spaces trimmed) and a short link is created. | R2, R4 | |
| AC3 | Given a visitor submitting an empty field or only spaces, when they submit, then they see a clear English error and no short link is created. | R3, R4 | |
| AC4 | Given a visitor submitting a string that is not a URL or uses a non-http(s) scheme (for example `javascript:alert(1)`), when they submit, then they see a clear English error and no short link is created. | R2, R3 | |
| AC5 | Given a visitor submitting a trimmed URL longer than 2048 Unicode code points, when they submit, then they see a clear English error and no short link is created. | R5 | |
| AC6 | Given an existing non-deleted short link, when anyone opens it, then they are redirected to the stored original URL. | R6, R16 | |
| AC7 | Given a short code that never existed, when anyone opens it, then they see a clear English not-found result and are not redirected. | R7 | |
| AC8 | Given a short link that was permanently deleted, when anyone opens it, then they see a clear English not-found result and are not redirected. | R7, R14 | |
| AC9 | Given a valid management token from a prior creation, when the visitor creates another valid URL while providing that token, then the new short link appears under that token’s list and no different management token is shown as newly issued for that creation. | R10, R12, R13 | |
| AC10 | Given an unrecognised management token on create, when the visitor submits a valid URL with that token, then creation is refused with a clear English error and no short link is created. | R11 | |
| AC11 | Given a valid management token, when the visitor opens management with that token, then they see each tied link’s short link, original URL, and creation date/time. | R12, R15 | |
| AC12 | Given a valid management token and a confirmation to delete one tied short link, when they confirm delete, then that short link is permanently removed from the list and opening it yields not-found (AC8). | R14 | |
| AC13 | Given a delete action without confirmation, when the visitor cancels or does not confirm, then the short link remains listed and still redirects. | R14 | |
| AC14 | Given no management token (and no equivalent management session), when a visitor tries to list or delete links, then the action is refused. | R15 | |
| AC15 | Given two successful creations of the identical original URL without forcing reuse, when both complete, then two distinct short links exist. | R21 | |
| AC16 | Given repeated invalid management-token attempts beyond the plan’s limit, when the visitor tries again, then they receive a clear English rate-limit (or equivalent) error and do not gain access. | R19 | |
| AC17 | Given successful or failed management operations, when logs are inspected for those operations, then no full management token appears in application logs. | R20 | |
| AC18 | Given a short link and its management token that were created earlier and never deleted, when time has passed with no expiry action, then the short link still redirects and the token still lists that link (no automatic expiry in this feature). | R17 | |
| AC19 | Given two different invalid management tokens, when each is used for a management attempt, then both receive the same class of clear English invalid-token error (no difference that reveals whether any other token exists). | R22 | |
| AC20 | Given repeated successful or attempted link-creation requests beyond the plan’s bulk-creation limit, when the visitor tries again, then they receive a clear English rate-limit (or equivalent) error and no additional short link is created for that refused attempt. | R19 | |
| AC21 | Given successful or failed create or management operations that involve an original URL, when routine application logs for those operations are inspected, then no full original URL appears in those logs. | R20 | |

## 5. Critical flows

- **Create without token → receive short link and new token** — core value; e2e required (C5).
- **Open short link → land on original URL** — core value; e2e required.
- **Create with existing token → link appears in that token’s list** — multi-link management; e2e required.
- **Manage with token → list → delete with confirmation → short link not found** — destructive path; e2e required.

## 6. UI behavior (only if the feature has an interface)

Screens (names are descriptive, not routes):

1. **Create** — Field for original URL; optional field for existing management token; submit control.
   - **Empty:** URL field empty; no result yet; optional token field empty.
   - **Loading:** Submit disabled or busy state while creation runs; no duplicate submit success.
   - **Error:** Inline or page English error for validation, invalid token, or rate limit; previous input preserved where sensible (URL and token fields).
   - **Offline:** N/A for product behaviour beyond a clear English failure if the network is unavailable (offline mode / PWA out of scope).

2. **Creation result** — Shows short link (copy), management token when newly issued (copy + optional download), recovery warning when a new token is shown. When creation used an existing token, show short link and confirmation it was added to that token (no new token).
   - **Empty / Loading / Error / Offline:** as above for any follow-on actions.

3. **Manage** — Enter management token (or continue a management session); list of links; add (same URL rules); delete with confirmation.
   - **Empty:** No token yet, or token valid with zero links after deletions.
   - **Loading:** While listing or mutating.
   - **Error:** Invalid token, rate limit, validation on add, delete failure.
   - **Offline:** Same as Create.

4. **Not found (short link)** — Clear English message; no redirect.
5. **Generic server error** — Clear English message; no internal detail (W10).

Creation date/time in the list: shown in a human-readable form in the user’s locale/timezone where the platform allows; stored value is unambiguous (plan may store UTC).

## 7. Security and privacy

- **Access:** Anyone may create (within limits) and open short links. Listing, adding, and deleting require the management token (R9, R15). Short links are public (R16).
- **Abuse:** Repeated-attempt limits on token guessing and bulk creation (R19); thresholds in the plan.
- **Information leaks:** Invalid token errors do not disclose other tokens’ existence (R22). Not-found for short links does not disclose whether a code existed before deletion vs never existed (same not-found experience, R7).
- **Token lifetime:** No expiry in this feature (R17); secrecy of the token is the access control.
- **Input limits:** Schemes http/https only (R2); max 2048 code points after trim (R5); trim (R4).
- **Logging:** R20; no full management tokens; no full original URLs in routine application logs.
- **Secrets:** Management tokens MUST be stored only in a form that is not reversible to the raw token from a data dump alone (e.g. one-way verification), or an equivalent plan-approved approach that meets C6; raw token shown only at issuance and when the user pastes it. Transmission only over encrypted transport in deployed environments (plan).
- **Personal data:** No accounts or emails. Original URLs may contain personal data; they are stored for redirect and listing until deleted. **Retention:** no automatic expiry in this feature (R17). Privacy policy text and legal retention details: deferred to profile D8 (not blocking product behaviour of this spec).
- **Accepted risk:** Loss of the management token permanently loses management access; short links keep working (product decision). Creator is responsible for copying/storing the token.
- **Threat baseline:** OWASP Top 10 (web); OWASP API Security Top 10 for HTTP operations (backend module).

## 8. Out of scope

- Registration, login, magic link, or any account system
- Editing an original URL in place (delete + add only)
- Custom short codes or vanity paths chosen by the user
- Analytics dashboards, click charts, or non-essential trackers
- Custom branding / custom domains (profile D2)
- Public API for third-party integrations
- Offline / installable PWA
- Automatic expiry or scheduled deletion of links
- Recovery of a lost management token
- Team / multi-user organisations

## 9. Open questions

- [ ] Exact numeric thresholds for rate / abuse limits (R19) — **deferred to plan** (operational tuning; behaviour when limited is specified).
- [ ] Exact storage/verification scheme for management tokens — **deferred to plan** (must satisfy Section 7 / C6).
- [ ] Privacy policy wording and legal retention (profile D8) — **deferred**; does not change R17 behaviour.
- [ ] Numeric performance targets (profile D6) — **deferred to plan** if still unset.
- [ ] Supported browsers and viewport range (profile D7) — **deferred to plan** if still unset; UI still MUST meet WCAG 2.2 AA per module web.

## 10. Edge cases (optional)

- Empty / whitespace-only URL → R3, R4, AC3
- Non-http(s) scheme → R2, R3, AC4
- URL > 2048 code points after trim → R5, AC5
- Leading/trailing spaces → R4, AC2
- Uppercase `HTTP`/`HTTPS` scheme → R2, AC2
- Unknown short code → R7, AC7
- Deleted short code → R7, R14, AC8
- Invalid management token on create or manage → R11, AC10
- Cancel delete confirmation → AC13
- Duplicate original URL twice → R21, AC15
- Create with valid token when list was empty after prior deletes → R10, R13 (allowed)
- Double submit on create → UI loading / busy MUST prevent duplicate success from double click (Section 6); if two requests both succeed, R21 allows two links — prefer single success per intentional submit (plan/tests)
- Bulk create beyond plan limit → R19, AC20
- Routine logs must omit full original URL → R20, AC21

## 11. Success measures (optional)

- A new visitor can create a short link and open it successfully without help.
- A creator who saved the token can list and delete a link without an account.

## 12. Impact on existing specs (only if this spec extends or changes another)

N/A – first feature spec; no prior specs.

## 13. Approval

- Approved by: Luca Lanzano
- Date: 26/11/2026
