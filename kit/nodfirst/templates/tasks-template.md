<!--
TASKS TEMPLATE v0.1 — copy to specs/NNN-feature-name/tasks.md
Rules:
- Derive tasks from the approved spec and plan. Do not add behavior that is not in the spec (C1, C3).
- Each task is small: one coherent change that leaves the project building, linted, typed and tested (C9).
- Tests come first or together with the code, never after "later" (C5).
- Every task cites requirement IDs (R) and acceptance criteria (AC). Every R and AC must be covered by at least one task (C4).
- Order tasks by dependency, tests included (a test cannot depend on something built later). Prefer vertical slices that can be demonstrated.
- One deliverable per task: two forms with different rules or limits are two tasks.
- If the feature changes behaviour already covered by tests, the task that updates those tests comes first and stays green before and after.
- "Done when" must be provable inside the task.
- Every task has "Depends on". Add "Requires human action" when the task needs something outside the repository.
- Plain characters, no HTML entities.
- Remove all <!-- comments -->.
-->

# Tasks NNN: <Feature name>

- **Spec:** `specs/NNN-feature-name/spec.md`
- **Plan:** `specs/NNN-feature-name/plan.md`
- **Status:** Draft | Approved

## Legend
- `[ ]` to do · `[~]` in progress · `[x]` done · `[!]` blocked (add a note)
- `[P]` can run in parallel with the previous task (no shared files or dependencies)
- **Requires human action:** work outside the repository (consoles, accounts, secrets, keys); listed under the task

## Phase 1 — Setup / foundation
<!-- Only what later tasks need (config, scaffolding, migrations, shared helpers). Keep minimal. -->

- [ ] **T1** <Short imperative title>
  - **Covers:** R1 · AC1
  - **Depends on:** —
  - **Requires human action:** <only if needed>
  - **Files / areas:** 
  - **Tests:** <tests to write, with level>
  - **Done when:** <observable result + quality gates pass>

## Phase 2 — Story slices
<!-- One group per user story, in priority order. Each group delivers something usable end to end. -->

### US1 — <title>
- [ ] **T2** 
  - **Covers:** 
  - **Depends on:** 
  - **Files / areas:** 
  - **Tests:** 
  - **Done when:** 

## Phase 3 — Hardening
<!-- Edge cases from the spec, accessibility pass, security checks from the plan, offline/error states, documentation updates. -->

- [ ] **T-n** 

## Traceability check
<!-- Fill before approval. No empty cell allowed. -->
| Requirement / AC | Tasks | Test |
|------------------|-------|------|
| R1 / AC1 | T1, T2 | |

## Notes / blockers
- 

## Open questions
<!-- Plan or spec gaps found while writing tasks: report them, do not invent a mechanism. -->

## Interpretations
<!-- Every reading of an ambiguous instruction. -->

## Approval
- Approved by: 
- Date: 
