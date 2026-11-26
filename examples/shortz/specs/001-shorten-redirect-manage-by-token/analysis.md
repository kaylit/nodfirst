# Analysis 001: Shorten, redirect, manage by token

- **Run:** 3
- **Date:** 2026-11-26
- **Verdict:** ready to implement
- **Prior run:** 2 was `ready to implement` while plan and tasks were still Draft. This run reads the approved plan (CR-1) and tasks T1–T32.

## 1. Approval status (not findings)

| File | Status | Approved by | Date | Modified after approval stamp? |
|------|--------|-------------|------|--------------------------------|
| `spec.md` | Approved | Luca Lanzano | 26/11/2026 | No. The stamp is at the end of the file and follows AC20/AC21. |
| `design.md` | Approved | Luca Lanzano | 26/11/2026 | No later date. §7 still has two unchecked question boxes. |
| `plan.md` | Approved | Luca Lanzano | 26/11/2026 | No. The CR-1 change log and the stamp are the same day; CR-1 sits above the stamp. |
| `tasks.md` | Approved | Luca Lanzano | 26/11/2026 | No. The T28–T32 revision sits above the stamp. |

Open questions: spec §9 checkboxes are still open, each marked deferred; plan §13 says none (F1). Design §7 still asks to confirm the proposed gaps and leaves D7 to the plan; the design file is Approved anyway. Plan and tasks: no open questions. CR-1 is decided (Luca Lanzano, 26/11/2026), not an open change request.

`project/profile.md` is Approved (Luca Lanzano, 26/11/2026). Sections 5 and 6 on disk match task T27 (full `quality` command and gate 9). Those edits are not in the last commit. That is not a finding against spec, plan, or tasks.

## 2. Traceability matrix

### 2.1 Requirement → proving AC → plan → tasks → tests

| R | Proving AC | Plan | Tasks | Named tests |
|---|------------|------|-------|-------------|
| R1 | AC1 | `createLink` | T9, T12, T13 | e2e AC1; integration create |
| R2 | AC2, AC4 | validation | T8, T12, T18 | unit; e2e AC4 |
| R3 | AC3, AC4 | validation | T8, T13 | unit; e2e AC3, AC4 |
| R4 | AC2 | trim then validate | T8, T12 | unit AC2; integration AC2 |
| R5 | AC5 | max 2048 code points | T8 | unit AC5 |
| R6 | AC6 | GET `/r/[code]` 302 | T14 | e2e AC6 |
| R7 | AC7, AC8 | not-found page | T14, T19 | e2e AC7, AC8 |
| R8 | AC1 | result + download file name | T12, T13 | e2e AC1 |
| R9 | AC1 (warning only); AC11–AC14 | token hash + session | T10, T16, T28 | unit token; integration session. No-recovery path: F3 |
| R10 | AC9 | create with token | T15 | e2e AC9 |
| R11 | AC10 | refuse unknown token | T15, T16 | e2e AC10; integration unlock |
| R12 | AC11 | `listLinks` | T17, T29 | e2e AC11; e2e reload |
| R13 | AC9 | `addLink` and create-with-token | T15, T18 | e2e AC9; e2e add from Manage |
| R14 | AC12, AC13, AC8 | `deleteLink` | T19, T28 | e2e AC12, AC13; integration foreign delete |
| R15 | AC14 | session cookie | T16, T17, T28, T29 | integration list/add/delete refusal; e2e locked page; e2e reload. AC14 text omits add: F5 |
| R16 | AC6 | public redirect | T14 | e2e AC6 |
| R17 | AC18 | no link/token TTL | T12, T23 | integration AC18. Session 7 days: F2 |
| R18 | AC1 and the English strings in the other ACs | design §5 catalogue | T13, T17, T20, T30, T31 | e2e copy; offline e2e; error-screen unit |
| R19 | AC16, AC20 | 30/hour, 10/15 min, CR-1 | T11, T12, T16, T32 | integration AC16, AC20; unit forwarded headers |
| R20 | AC17, AC21 | logger redaction | T6, T22 | unit redact; integration AC17, AC21 |
| R21 | AC15 | distinct short codes | T9, T12 | integration AC15 |
| R22 | AC19 | same invalid-token class; one not-found page | T16, T14, T19 | integration AC19; e2e AC7, AC8 |

Withdrawn: none.

### 2.2 Criterion → task → test (really verifies?)

| AC | Task(s) | Test | Really verifies? |
|----|---------|------|------------------|
| AC1 | T13 | e2e: short link, token, copy, download control, warning | Yes. The criterion asks for a download control, not the file body. |
| AC2 | T8, T12 | unit + integration: uppercase scheme and trim | Yes |
| AC3 | T8, T13 | unit + e2e: empty or spaces, English error, no short link | Yes |
| AC4 | T8, T13 | unit + e2e: `javascript:` / non-URL | Yes |
| AC5 | T8 | unit: 2049 code points rejected | Yes |
| AC6 | T14 | e2e: 302 to the stored URL | Yes |
| AC7 | T14 | e2e: unknown code shows the English not-found page | Yes. The hop is a 302 to `/link-not-found`, which plan §6 allows. |
| AC8 | T19 | e2e: deleted code shows that same not-found result | Yes |
| AC9 | T15 | e2e: second create stays on the same token and shows in the list | Yes |
| AC10 | T15 | e2e: bad token, English error, no short link | Yes |
| AC11 | T17 | e2e: short link, destination, created time | Yes. Display zone is F7, not a missing column. |
| AC12 | T19 | e2e: confirm removes the row and the short link is not found | Yes |
| AC13 | T19 | e2e: cancel keeps the redirect | Yes |
| AC14 | T16, T17, T28, T29 | integration refuses list, add, and delete with no session; e2e shows the locked page; e2e reload keeps the list | Yes for list and delete. Add is tested in T28 but not named in the AC (F5). |
| AC15 | T12 | integration: two codes for one URL | Yes |
| AC16 | T11, T32 | integration: over-limit token attempts get the English rate-limit error; unit: last forwarded hop | Yes |
| AC17 | T22 | integration: create/unlock logs omit the full token | Yes |
| AC18 | T23 | integration: link still redirects and lists after a moved clock | Yes, for the link. The session row may expire (F2). |
| AC19 | T16 | integration: two bad tokens, same error class | Yes |
| AC20 | T11, T12, T32 | integration: over-limit create does not add a row and returns the English error; unit header rule | Yes |
| AC21 | T22 | integration: those logs omit the full original URL | Yes |

## 3. Checks run

- **Proof.** Each MUST R1–R22 has a criterion that fails if that behaviour is removed, except the “no recovery path” half of R9 (F3) and the word “adding” inside R15 (F5). AC20 and AC21 still prove R19 and R20.
- **Contradictions.** 2048, Base62 length 8, 302, download file name, error codes, and the 30/hour and 10/15 min limits agree. CR-1 in plan §4 matches task T32. The earlier session sentence still says `Secure` with no exception (F4).
- **Stale text.** Spec §9 (F1). Run 2’s profile “DECIDE D1” and “gate 9 N/A” lines are gone on disk. Plan §15 is indicative and was not compared line by line with the tasks.
- **Parallel wording.** AC16 and AC20 use the same rate-limit shape. `create.errorToken` and `manage.errorToken` are the same sentence.
- **Vacuous tests.** T3’s smoke test is written to always pass (F8). The AC tests above can fail.
- **Order.** Playwright (T4) and the database (T5) come before the tests that need them. T2 is the human secret step before T5. T28–T32 depend on earlier tasks. No task needs an account that a later task creates.
- **Constitution.** C1–C14: no violation that leaves a behaviour unspecified and untested. C8 pins are named in the plan; exact React and driver patches are recorded in the task notes. Profile exceptions: none. Backend B5 is F6.
- **Security.** Spec §7 items have a plan mechanism and a named test: token hash, session, rate limits, CR-1, logging, http(s) only, same error class, no recovery is the weak item (F3). Headers are a plan decision with task T21.

## 4. Findings

### Closed since run 2

- **High F1 / F2 (run 1, still closed).** AC20 and AC21, with tasks and plan rows.
- **F4 (run 2).** Profile §4 names Turso. Gate 9 names the soft D6 targets.
- **F5 (run 2).** Task T31 covers the generic server-error screen and design keys `error.serverTitle`, `error.server`, `error.retry`.

### F1 — Medium
- **Where:** `spec.md` §9
- **What:** The checkboxes still list rate limits, token storage, privacy wording, performance, and browsers as open. Plan §4 and §13 record those decisions.
- **Smallest fix:** Clear or strike those rows in a spec change.
- **File:** `spec.md` (change request)

### F2 — Medium
- **Where:** `spec.md` R17; plan session decision (7 days); `tasks.md` AC18 note
- **What:** Links and management tokens do not expire. The manage session does, after 7 days. The tasks note says that. The spec does not say the session may expire.
- **Smallest fix:** One spec sentence that the session cookie may expire without expiring links or tokens. Or accept this reading.
- **File:** `spec.md` (change request) if the sentence is added

### F3 — Medium
- **Where:** `spec.md` R9; `tasks.md` traceability
- **What:** “No recovery path” is out of scope and the warning is in AC1. No criterion fails if a recovery screen is added while the warning stays.
- **Smallest fix:** An acceptance criterion that a recovery attempt is refused, or an explicit accepted risk in spec §7.
- **File:** `spec.md` (change request)

### F4 — Medium
- **Where:** `plan.md` session decision; later decision CR-1; `tasks.md` T32
- **What:** The session decision still says the cookie is `Secure` with no exception. CR-1 and T32 say `Secure` only when the last `x-forwarded-proto` is `https`, or when that header is missing and `NODE_ENV` is `production`.
- **Smallest fix:** Point the session sentence at CR-1.
- **File:** `plan.md` (plan revision)

### F5 — Medium
- **Where:** `spec.md` R15 and AC14; `tasks.md` T28
- **What:** R15 includes adding. AC14 says “list or delete” only. T28 also refuses add with no session, so the test exists only on the task.
- **Smallest fix:** Add “add” to AC14.
- **File:** `spec.md` (change request)

### F6 — Medium
- **Where:** `plan.md` §6 `listLinks`; backend module B5; profile exceptions: none
- **What:** B5 says every list has a maximum page size. The plan returns the full `items` array. Spec, plan, and tasks agree with each other. The profile does not record an exception.
- **Smallest fix:** A profile exception, or a plan page size. Do not invent a cap in silence.
- **File:** `project/profile.md` or `plan.md`

### F7 — Medium
- **Where:** `spec.md` §6; `tasks.md` T17 note
- **What:** The spec shows creation time in the user’s locale and zone where the platform allows, stored unambiguously. The T17 note records `en-GB` and `UTC`.
- **Smallest fix:** A spec sentence that the list shows UTC, or drop the UTC choice from the task note and format in the user zone.
- **File:** `spec.md` (change request) or `tasks.md`

### F8 — Low
- **Where:** `tasks.md` T3
- **What:** The smoke test is specified to always pass. It only proves the runner starts.
- **Smallest fix:** Leave it. It is a runner probe, not a product proof.
- **File:** none required

### F9 — Low
- **Where:** `plan.md` D6; `project/profile.md` §6 gate 9
- **What:** The less-than sign is written as `&lt;` in the markdown.
- **Smallest fix:** Write a normal `<` when those lines are next edited.
- **File:** `plan.md`, `project/profile.md`

### F10 — Low
- **Where:** `project/profile.md` §1 and §3
- **What:** The summary says the token is used to view links. Spec D4 and the feature also add and permanently delete.
- **Smallest fix:** Say list, add, and delete in those two sentences.
- **File:** `project/profile.md`

## 5. Counts and verdict

| Severity | Count |
|----------|-------|
| Critical | 0 |
| High | 0 |
| Medium | 7 (F1–F7) |
| Low | 3 (F8–F10) |

**Verdict: ready to implement**

Medium items do not block. F4 is the one to fix in the plan so the cookie rule has a single sentence. F5 and F7 are spec wording. This run did not read the code and does not replace verification run 2.
