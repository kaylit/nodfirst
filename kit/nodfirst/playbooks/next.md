# Playbook: Next (where are we, what now?)

**Version:** 0.3 (not yet proven)
**Purpose:** read the project files and tell the human, in a few lines, where the project stands and what to do next. Safe to run at any time.
**Prompt:** `/nodfirst-next` (or mention `nodfirst/playbooks/next.md`), or simply ask "where are we?".
**Output:** a short answer in the chat. **No file changes.**

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `project/profile.md`, `project/roadmap.md` if it exists, and for every folder in `specs/`: the header (status, approval) of `spec.md`, `design.md`, `plan.md`, `tasks.md`, `analysis.md`, `verification.md`, and the task checkboxes in `tasks.md`.

## Instructions for the agent

Follow the working profile's language (constitution, Section 2). Read only; change nothing.

1. **Set-up.** If `project/profile.md` is still the empty skeleton: the next step is `/nodfirst-init` (new project) or `/nodfirst-adopt` (existing code); say which one fits. If it is filled in but not `Approved`: the human reviews and approves the profile. In both cases, answer (step 5) and stop.
2. **Find the active feature** (profile, Section 0). If none is set, list the features in `specs/` with their state, and the first idea in `project/roadmap.md`.
3. **Work out the state of the active feature** from the files, in this order, and stop at the first gap:
   - **light track** (`Track: Light` in the spec): spec `Draft` → review and approval; approved but not implemented → `/nodfirst-fix` in a new chat to implement it; implemented but the report not yet accepted → the human reviews it; accepted and security-relevant, no verification → `/nodfirst-verify` in a new chat; verification without **Closure** → the human closes it (`/nodfirst-verify close`); otherwise → finished. Skip the rest of this list.
   - no spec → `specify`;
   - spec `Draft` with open questions → answer them or `clarify`;
   - spec `Draft` or `Clarified` without open questions → the human reviews and approves the spec;
   - spec approved, feature with screens, and no `project/design-system.md` → `design-system` first (optional, recommended once per project);
   - spec approved, feature with screens, no design and the human has not skipped it → `design` (optional);
   - no plan → `plan`; plan `Draft` → review and approval;
   - no tasks → `tasks`; tasks `Draft` → review and approval;
   - no analysis, or an analysis older than the latest change to spec, plan or tasks → `analyze`;
   - analysis with Critical or High findings not accepted → fix them (`specify` Mode B, `plan` or `tasks` revision), then `analyze` again;
   - tasks not all `[x]` → `implement` (name the next task, and any task marked `[!]` with its blocker or "Requires human action");
   - all tasks done, no verification → `verify` in a new chat;
   - verification with Critical or High findings and no **Closure** section → the human decides: fix them (`tasks` revision, then `verify` again in a new chat) or close the feature accepting them (`/nodfirst-verify close` with the findings accepted and their reasons);
   - verification with no Critical or High finding and no **Closure** section → the human does the open "Needs a human" checks (name them), then closes the feature (`/nodfirst-verify close`);
   - **Closure** recorded → the feature is finished: suggest the next roadmap item, and mention the follow-ups of accepted findings.
4. **Look for warnings:** a file changed after its approval stamp (changes to Section 0 of the profile do not count); a task in progress `[~]` with no report; a change request that nobody has answered; a "Requires human action" item ahead; Commands still TBD after the scaffolding task.
5. **Answer** in at most ten lines:
   - **Where we are:** one sentence.
   - **What is waiting for you** (decisions, approvals, actions outside the computer), if anything.
   - **Next step:** the command to type, ready to copy, and whether to start a new chat.
   - **Warnings**, if any.

6. **Stop.**

## Do not
- Change any file, start the next phase, or approve anything.
