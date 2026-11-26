# Example: Shortz (a real run)

**Real.** These are the documents of a real project built with NodFirst 0.1.0, from `init` to `verify`, and deployed. They are copied as they were when the feature closed, with only these changes: the production host is `production-host.example`, the database host is `database-host.example`, and the repository name and database account are removed. The code is in a private repository and is not included; the documents name its files (`src/…`, `tests/…`, `e2e/…`) as they were.

## The project
Shortz shortens long URLs. Anyone can create a short link without an account; a one-time **management token**, shown once, lets its owner list, add and delete their links. No recovery if the token is lost.

| | |
|---|---|
| Kit | NodFirst 0.1.0, unchanged |
| Working profile | Solo, Git checkpoints by the agent |
| Modules | `web` (partly proven) and `backend` (first use on a real project) |
| Coding tool | Cursor, with the NodFirst commands installed by `init` |
| Implementation | Cursor "Auto" (the model is chosen by the tool, so which one wrote the code is not known) |
| Verification | Grok 4.7 High in Cursor, in a separate chat (C14) |
| Stack (chosen in the plan) | Next.js, Turso (libSQL), Drizzle, shadcn/ui, Vitest, Playwright, deployed on Vercel |
| Size | 1 feature, 22 requirements, 21 criteria, 32 tasks, 67 unit and integration tests, 52 end-to-end tests |
| Duration | one afternoon and evening (26/11/2026), 43 commits |

## What to read, in order
| File | Look at |
|---|---|
| [`project/profile.md`](project/profile.md) | Open decisions D1–D10: each says *when* it is decided, and most are closed by the plan |
| [`spec.md`](specs/001-shorten-redirect-manage-by-token/spec.md) | Section 7 (security and privacy) and R22: the error for an invalid token must not reveal whether other tokens exist |
| [`design.md`](specs/001-shorten-redirect-manage-by-token/design.md) | Screens, states and exact texts, before any code |
| [`plan.md`](specs/001-shorten-redirect-manage-by-token/plan.md) | One decision at a time, with options; exact pins with the date they were checked; decision CR-1 and the change log |
| [`tasks.md`](specs/001-shorten-redirect-manage-by-token/tasks.md) | "Requires human action" (accounts, secrets, deploy); Phase 4, the tasks added after the first verification |
| [`analysis.md`](specs/001-shorten-redirect-manage-by-token/analysis.md) | Approval status kept apart from findings; the traceability matrix |
| [`verification.md`](specs/001-shorten-redirect-manage-by-token/verification.md) | The requirement table, 14 findings, "Needs a human", and how the human closed the feature |
| [`verification-prep.md`](specs/001-shorten-redirect-manage-by-token/verification-prep.md), [`keyboard-check.md`](specs/001-shorten-redirect-manage-by-token/keyboard-check.md) | Two notes the agent created for checks the kit has no file for |

## How it went (from the commits)
| Time (CET) | Step |
|---|---|
| 15:21 | `init`: profile approved (Solo, Git, modules `web` and `backend` accepted with their warning) |
| 15:35 – 15:52 | spec, design, plan and tasks approved, one after the other |
| 15:57 – 16:00 | `analyze` found that two requirements (bulk-creation limit, no URLs in logs) had no criterion that proves them. AC20 and AC21 were added; spec, then plan and tasks, approved again |
| 16:01 – 19:08 | T1–T27 implemented, one commit per accepted task |
| 19:08 – 19:34 | `verify` run 1, in a new chat: 4 findings. The main one: rate limits trusted the first address of `X-Forwarded-For`, which the caller controls |
| 19:34 | The human chose option C of change request CR-1 (plan, change log); tasks T28–T32 added and approved |
| 19:36 – 19:48 | T28–T32 implemented |
| 20:11 | `verify` run 2: **partly verified**, 10 findings; `analyze` run 3 |
| 22:14 – 22:31 | CI test fixed; deploy on Vercel; production smoke recorded by the agent |
| 22:41 | `verify` run 3: **not verified**, 14 findings (2 Critical). The human accepted F1–F14 and closed the feature |

## Why it is done this way
- **The gates worked as designed.** `analyze` stopped implementation until two MUST requirements had a criterion that would fail without them (C4). The first `verify` found a real security hole the implementer's own tests did not see (C14), and the fix went through the normal path: a decision in the plan, new tasks, a new approval. Nothing was patched silently.
- **The plan records what was checked, and when.** Every pinned version has a "Verified" date; every choice has its options. A reader can tell a decision from a guess.
- **The verdict got stricter, not looser.** Run 3 found more than run 2 on similar code, and says why: it applied the severity scale of `verify` literally. See the next section.
- **"Not verified" with accepted findings is an honest close.** The human chose to ship knowing the 14 findings, and wrote that decision in the file. The findings stay visible.

## What this run taught the kit
First real use of: working profile Solo, Git checkpoints, the Cursor command files, `design`, `verify` (three runs, another model), a task revision after `verify`, a plan change request, the `backend` module. What it showed, to be turned into kit changes one at a time (see `ROADMAP.md`):
1. **No way to close a feature with accepted findings.** `verify` knew only "verified" or "fix and verify again". The agent invented a `Last closed` line in the profile, and `next` would still say "run `verify`". *Addressed in 0.2.0: `verify` now has a "Closing the feature" step.*
2. **Checks only a person can do block the verdict.** "No GitHub Actions run observed" and "production smoke not repeated" became High findings (F9, F10), so `verified` is out of reach whatever the code does, although `verify` already has a "Needs a human" list for them. *Addressed in 0.2.0: such checks now go only to Needs a human, and the verdicts have exact rules.*
3. **The verdict is not stable across runs.** Runs 2 and 3 classified similar issues differently (`partly verified` → `not verified`). *Partly addressed in 0.2.0: a re-run must list every previous finding as closed, still open or reclassified, with a reason.*
4. **No lessons were recorded.** `project/lessons.md` stayed empty: the profile said "not a proving ground", and the lessons log is described as part of that loop only. *Addressed in 0.2.0: in every project the agent now proposes lessons, and up to three when a feature is closed.*
5. **The skeletons were too narrow.** The agent added a package-manager row and a standing approval-record rule to the profile, created two notes the kit does not name, and `next dev` appended its own block to `AGENTS.md`.
6. **A late fix skipped the light track.** The CI test fix after the last task was committed directly; there is no light spec for it.
