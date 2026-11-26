# Playbook: Implement

**Version:** 0.2 (tested on three features, forty-seven tasks)
**Purpose:** carry out one task of an approved task list: tests first, minimal code, quality gates, honest report.
**Prompt:** `/nodfirst-implement` (or mention `nodfirst/playbooks/implement.md`) (next task) or add `T5` (a named task).
**Output:** the code and tests of the task, and `tasks.md` updated.

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `project/profile.md`, the modules it lists (`nodfirst/modules/`), and for the active feature `spec.md`, `plan.md`, `tasks.md`.

## Preconditions
- Spec, plan and tasks are `Approved`. If an analysis exists, it has no Critical or High left (or the human accepted them).
- The task's dependencies are done.
- The tools and runtimes the task needs are installed. If one is missing, mark the task `[!]`, say what the human must do, and stop. **Never lower a version or relax a constraint to continue.**

## Instructions for the agent

Follow `AGENTS.md`, `nodfirst/constitution.md` and `project/profile.md`, especially C1, C2, C3, C5, C6, C8 and C9.

1. **Restate the task:** ID, requirement and criterion IDs, files or areas, "done when". If anything is unclear or conflicts with the plan or spec, stop and ask (C3).
2. **Tests first.** Write or extend the tests the task lists. Run them and show that they fail for the right reason, unless the task is pure setup. If the task's test runner is installed by a later task, say which command you used meanwhile.
3. **Implement the minimum** that passes the tests and satisfies "done when". No extra features, no refactoring outside the task, no dependency, licence, metadata or configuration that the plan or tasks do not name (C8, C3). A tool warning alone is not a reason to add one.
4. **Run the quality gates** with the commands in `project/profile.md`, Section 5 (read the project files if it says TBD). Fix failures. Never weaken, skip or delete a test to make a gate pass. If you must change an earlier task's test because the behaviour legitimately changed (for example a stub is replaced), say so and keep what the test verified.
5. **Update the records:** mark the task `[x]` in `tasks.md`. If the scaffolding task created the project, fill Section 5 (Commands) of `project/profile.md`. If the work shows that the spec or plan is wrong or incomplete, **stop and write a change request**; do not edit the spec or plan yourself and do not work around them.
6. **Report in this form** (a report without "Before" is incomplete, unless the task is setup):
   - **Task** and what it covers.
   - **Before:** which tests failed and why.
   - **Tests added:** names.
   - **Implementation:** files created or changed.
   - **Gates:** each command and its result, with the number of tests passed.
   - **Deviations and interpretations**, and anything left undone.
7. **Stop.** Do not start the next task unless the human said "continue until T<n>" and the working profile allows it (Solo, Team) (C2). When the human accepts the task and the profile uses git checkpoints, commit the task's files with the message `T<n> done (feature NNN)` (constitution, Section 4).

## Final verification (the last task of the feature)
The report of the last task is **incomplete** without all four items:
1. The single quality command run **from a fresh environment** (remove installed dependencies and build outputs, reinstall, rebuild, run; for example a recreated virtual environment, or a deleted `node_modules` folder), with its result.
2. A table of every criterion of the feature and the test that verifies it.
3. A search for `TBD` in the docs and `project/profile.md`, with the result.
4. A list of files that do not belong to the project (leftovers, notes of other projects, editor files).

Then suggest the next step: run `/nodfirst-verify` **in a new chat**, ideally with another model or agent (C14). The feature is finished only when the human closes it after the verification (`verify`, "Closing the feature").

## Safety
- Never run destructive commands (data deletion, force push, dropping tables, mass file removal) without explicit approval.
- Do not touch files outside the task's scope.

## Extra instructions
<!-- Write below this line when you use the playbook. -->
