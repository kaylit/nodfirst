# Playbook: Init (new project)

**Version:** 0.2 ("after a kit update" used once; interview and profile tested on three projects; Solo profile, Git checkpoints and command install for Cursor used on one; Guided and Team profiles, other tools not yet proven)
**Purpose:** set up NodFirst in a project: write the project profile, choose how the human wants to work, install the commands for the human's coding tool, and create the supporting files. For a project that already has code, use `adopt` instead.
**Prompt:** `/nodfirst-init` (or mention `nodfirst/playbooks/init.md`) followed by a few lines about the project. After a kit update: `/nodfirst-init update`.
**Output:** `project/profile.md` filled in, `project/roadmap.md`, `project/lessons.md`, folders `specs/` and `docs/decisions/`, and the command files for the human's tool.

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `nodfirst/VERSION`, `nodfirst/CHANGES.md` (for an update), `project/profile.md`, `nodfirst/modules/README.md` and the modules it lists, `nodfirst/adapters/README.md`, and the list of files in the repository.

## What this playbook does not do
- It does not change the constitution. If a rule does not fit, record an **exception** in the profile (Section 10) with the reason and ask for explicit approval.
- It does not choose technology for the human. It proposes options with pros and cons; the human decides. Undecided choices go to "Open decisions".
- It does not write feature specs, code or scaffolding. Scaffolding is a task inside the first feature's plan.

## Instructions for the agent

Follow `nodfirst/constitution.md`, especially C2, C3 and C13. Until the working profile is chosen (step 3), speak as in the **Guided** profile: everyday words, one question at a time.

1. **Check preconditions.**
   - `nodfirst/constitution.md` exists. If not, stop and tell the human to copy the kit (manual, Part 4).
   - **Existing code.** If the repository already contains application code (not only the kit), say so and recommend `adopt` instead. Continue only if the human confirms this is a new project.
   - If `project/profile.md` already has project content, ask whether to continue, replace or amend. Never overwrite silently.
   - **Residue audit (mandatory).** List every file that is not part of the kit and was not created by the human for this project (for example lesson logs, notes, specs or decision records of another project). Ask, for each group, whether to keep, reset or delete. Do not delete anything without the answer. If the human says this is a proving ground or sandbox, propose a clean slate for `project/lessons.md` and for notes of another project.
2. **Restate the project** in 3-4 sentences with your assumptions. Wait for correction. Ask whether the project also serves to test or improve the kit (a proving ground) or is only a product.
3. **Choose the working profile** (constitution, Section 2). Explain the three in one line each and propose one from what you know:
   - **Guided:** "You decide and approve; I explain everything in everyday words and ask one thing at a time."
   - **Solo:** "You are a developer working alone: shorter documents, technical language, fewer pauses."
   - **Team:** "Several people review: approvals by role, a branch and a pull request per feature, checks in CI."
   For Team, ask who approves each phase (role and name).
4. **Git.** Check whether the folder is a git repository (run `git rev-parse --is-inside-work-tree`) and whether `git` is installed.
   - **Guided:** explain in two sentences: "Git keeps a saved copy of every approved step, so we can always go back. I would save a checkpoint after each of your approvals; I never send anything online unless you ask." If the human agrees and the folder is not a repository, ask before running `git init`. If git is missing, tell the human how to install it (in plain steps) or continue without and recommend making a backup copy of the folder before every phase.
   - **Solo:** ask whether checkpoint commits are wanted.
   - **Team:** git is required; ask the branch naming and the review rule.
   Record the answer in the profile, Sections 0 and 2.
5. **Interview the human.** One question at a time (Solo and Team: up to three per message), each with your proposed default and a short reason. Skip what the description already answers. Cover these topics in order:
   1. Product and users: who it is for, core problem, v1 scope, out of scope, future plans.
   2. Platforms and **modules**: web, mobile, desktop, backend only, library; offline needs; installability. Match the answer with `nodfirst/modules/` and propose the modules that apply (several are normal: for example `web` with `backend`, or `mobile` with `backend`).
      - **Proven state.** Read the `State` line of every proposed module. For each module that is **not yet proven or only partly proven**, say plainly, for a not-yet-proven module: "The module <name> has never been used on a real project. Its rules come from standard practice and may be wrong or incomplete; some checks (real devices, signing, store or console work) can only be done by you. Do you want to continue with it?" For a partly proven module: "The module <name> has been used on one real project, but these parts never have: <list>. Do you want to continue with it?" Wait for an explicit yes. Record the module and the date in the profile, Section 1. If the human says no, use the core rules only.
      - If the kind of project has no module (for example features built on AI models), say so: use the core rules only, and record in the profile that no module exists and which checklists you could not apply.
   3. Accounts and data: login, personal data, ownership, sharing.
   4. Language and regions: UI languages now and later; **language of specs and other project documents** (default: the language the human writes in; template headings and IDs stay in English); **language of messages and documentation versus language of identifiers**; legal regimes.
   5. Technology preferences and constraints: preferred stack, skills, existing systems. Record preferences as decisions or as open decisions with criteria.
   6. Hosting, budget, operations: anything that costs money or creates an account is named as such.
   7. Quality: test policy (layers, critical flows), accessibility target, security level, performance. **Without CI, define one single local command that runs all quality gates** (it is written in Section 5 once the project is scaffolded).
   8. UI and design (if any).
   Ask at most 15 questions in total. Anything unanswered becomes an open decision or an explicit assumption, never a silent guess.
6. **Check the machine.** For every runtime or tool the profile requires (language runtime and version, package manager, git), run its version command and report the result. If one is missing or too old, do not change the constraint: tell the human what to install (in plain steps for Guided) and continue only when it is resolved or the human decides otherwise.
7. **Draft `project/profile.md`** from its skeleton (`project/profile.md` as shipped), keeping the section numbers: current state; product summary (modules, accepted unproven modules, proving ground); way of working; v1 scope; technical profile ("DECIDE" for undecided rows); commands (TBD until scaffolding); quality gates (numbered, checkable, starting from the active modules' typical gates); design system rules (only with a UI); data, privacy and security; feedback loop (only for a proving ground); exceptions (for example C7 and end-to-end tests for a library); open decisions (each with *when* it will be decided). Write the kit version from `nodfirst/VERSION` in the header. Cite rule IDs instead of repeating them; every "MUST" must be checkable.
8. **Show a summary and stop for approval** (C2): working profile, Git, decisions, assumptions, open decisions, exceptions, machine check, residue decisions, and the **modules not yet proven** with their warning.
9. **After approval, create the supporting files:**
   - `project/roadmap.md`, in this shape: a title; **Features** as a numbered list (`1. <name> – one line – depends on: <feature or none>`), ordered so that prerequisites come first and, among the rest, the riskiest first; **Open decisions** (ID and when, pointing to the profile, Section 11). Keep it under one page.
   - `project/lessons.md`: keep the empty log unless the human chose to keep entries.
   - `specs/` and `docs/decisions/` with `.gitkeep`.
   - **Commands for the human's tool.** Ask which coding tool the human uses (Claude Code, Cursor, GitHub Copilot, Codex, other). Follow `nodfirst/adapters/README.md` to copy the matching command files. For another tool, say that the playbooks work by mentioning their file, and show one example.
   - Record the approval in the profile header (Status `Approved`, name, date as the human gave them).
   - With git checkpoints: commit the kit (`AGENTS.md`, `CLAUDE.md`, `nodfirst/`), the command files, `project/` and the new folders, with the message `nodfirst: project set up` (constitution, Section 4).
10. **Verify and report:** the profile does not repeat the constitution; every "DECIDE" appears in Open decisions; gates are checkable; Section 0 says `Active feature: none yet`; Commands are TBD; a search finds no names or terms of another project; nothing outside the listed files changed.
11. **Stop.** Suggest the next step in one line: `/nodfirst-specify` with the first feature idea from the roadmap.

## After a kit update (`/nodfirst-init update`)
Use when the human has replaced the `nodfirst/` folder with a newer version.
1. Compare `nodfirst/VERSION` with the version in the profile header. Read `nodfirst/CHANGES.md` for every version between the two, and list what it says to replace (for example `AGENTS.md`): if a listed file still differs from the new kit, tell the human. Ask what changed only if `CHANGES.md` is missing.
2. Compare the profile with the skeleton description in this playbook (step 7): list new sections or fields the new version expects. Propose the additions; never remove or rewrite the human's content.
3. Re-copy the command files for the human's tool (`nodfirst/adapters/README.md`), replacing only files whose name starts with `nodfirst-`.
   **Kit files outside `nodfirst/`** (`AGENTS.md`, `CLAUDE.md`) are replaced only when `CHANGES.md` says so. Before replacing one, keep every block another tool added to it (for example between `<!-- BEGIN:… -->` and `<!-- END:… -->` lines) and put it back at the end; list what you kept.
4. List any playbook or rule that changed in a way that affects work in progress (a feature between phases). Do not change existing specs, plans or tasks.
5. Stop for approval; then update the kit version in the profile header.

## Do not
- Edit the constitution or anything in `nodfirst/`, pick the stack for the human, create specs, plans, tasks or code, or continue past step 8 without approval.
