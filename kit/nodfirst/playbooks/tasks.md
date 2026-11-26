# Playbook: Tasks

**Version:** 0.1 (tested on two projects)
**Purpose:** break an approved plan into small, ordered, verifiable tasks.
**Prompt:** `/nodfirst-tasks` (or mention `nodfirst/playbooks/tasks.md`) (and a feature number only if it is not the active one).
**Output:** `specs/NNN-feature-name/tasks.md`, status `Draft`.

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `project/profile.md`, the modules it lists (`nodfirst/modules/`), `nodfirst/templates/tasks-template.md`, the active feature's `spec.md` and `plan.md` (and `design.md` if any).

## Preconditions
The spec and the plan are `Approved`, with no open questions. If not, stop and say so (C2).

## Instructions for the agent

You are planning the work, not doing it. Follow `nodfirst/constitution.md`, especially C1, C4, C5, C8 and C9.

1. **Derive tasks** from the plan, in dependency order, applying the "Tasks" checklist of every active module:
   - **Phase 1: setup and foundation.** Scaffolding and configuration; the runtimes and tools the plan lists, each checked; the environment (for example installed dependencies in an isolated environment); **a smoke test so the test runner is proven before any task that depends on it**; the **single quality-gate command** and Section 5 (Commands) of `project/profile.md`; CI if the project has one; migrations and how they run in production; shared helpers. Keep it minimal.
   - **Phase 2: one group per user story**, each a vertical slice that delivers something demonstrable. Start with the smallest slice that proves the architecture. Pure logic comes before anything that needs infrastructure.
   - **Phase 3: hardening** only for what the earlier tasks do not cover.
2. **Shape each task:**
   - One coherent change that leaves the project building, linted, typed and tested (C9).
   - **Tests first**, listed in the task (C5). The task's "done when" must be **provable inside the task**; it never relies on a later task to show that it works.
   - Cites the R and AC it covers, the files or areas, and the quality gates in "done when".
   - **Depends on:** the tasks it needs, or "—". **Requires human action:** anything outside the repository (accounts, consoles, secrets, installing a runtime). The agent stops and asks; it never pretends.
   - **Versions:** exact pins, verified on the registry with the date; if a version is less than 7 days old, read its release notes and record the result in the task's notes.
   - **One deliverable per task.** Two forms with different rules, regular expressions or limits are two tasks, even when they look similar (for example "in N days" and "in N weeks" in a date parser).
   - **If the feature changes behaviour that existing tests cover, the first task updates those tests** and stays green before and after the change; the code change follows.
   - A temporary stub is allowed only if the task says so and names the task that replaces it.
   - If an AC is split across tasks, say which part each task covers.
   - `[P]` only when two tasks share no files and no dependency. No task without a source in the spec or plan (C1). No git or commit instructions unless `project/profile.md` says git is used.
3. **Fill the traceability table:** every active R and AC in at least one task; every plan decision implemented by some task; every AC has a named test. **A requirement with no criterion that proves it is reported as a spec change request**, not patched inside a task. Every documentation requirement has a test that keeps the documentation true.
4. **Check:**
   - No task mixes more than one deliverable; nothing vague ("implement authentication").
   - Order respects dependencies, **tests included**: a test that needs a user, a page or an endpoint depends on the task that builds it (seeded data is fine until then, repeated with the real flow later). Test infrastructure comes before the first task that needs it. Anything created for one task but used by an earlier one is moved before its user.
   - Plain characters in the file, never HTML entities.
   - Nothing contradicts the plan or the spec; otherwise write a **change request** and stop. Report plan gaps the same way; never invent a mechanism.
5. **Stop.** Show tasks per phase, the traceability result, assumptions, change requests and **interpretations**. Ask for review. Do not implement.

## Revising existing tasks
Apply only the requested changes, keep untouched tasks identical, update dependencies, traceability and totals (also when the spec's criteria changed, so test names and covers match the current text), and show two lists (changes and interpretations).

## Do not
- Write code or run commands, add behaviour, libraries or decisions the plan does not contain, or mark the tasks `Approved`.

## Extra instructions
<!-- Write below this line when you use the playbook. -->
