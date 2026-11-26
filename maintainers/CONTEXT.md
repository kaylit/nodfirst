# Context for whoever maintains NodFirst (human or agent)

Read this first, then `README.md` (this folder), `../ROADMAP.md` and `../CHANGELOG.md`.
**Important:** `kit/AGENTS.md` is part of the **kit** (it is copied into user projects). It is not the instruction file for maintaining this repository. Maintenance rules are in `maintainers/`.

## What NodFirst is
A Spec-Driven Development kit that works with any AI coding agent: a constitution (core rules and working profiles), playbooks (one per phase), templates, modules (rules by kind of project), command files for coding tools, and a manual. The human decides and approves; the agent writes, checks, reports and stops at every gate.

## Who it is for
Three working profiles: **Guided** (people who do not write code), **Solo** (a developer alone), **Team** (several people with review). It must be replicable, clear and short: one-line prompts or commands, rules live in the playbooks ("Context to read"), examples help.

## Decisions taken with the author (keep unless the author changes them)
- **Name:** NodFirst ("nothing gets built until you say yes").
- **Licence:** MIT, © Luca Lanzano'.
- **Language:** framework files, manual, prompts and identifiers in **English only**. The author talks to agents in Italian; product specs may be in any language (C12).
- **Markdown only:** no CLI, no script required in user projects. A document checker may be evaluated after real use (ROADMAP backlog). Maintainer tools (`maintainers/tools/`) may use Python's standard library.
- **Layout:** `kit/` is what users copy. Inside it, `nodfirst/` belongs to the kit (replaced on update), `project/`, `specs/`, `docs/` belong to the user's project. A kit update never needs the user to merge text by hand.
- **Role of the human:** decide and approve. The agent never approves, never starts the next phase, never decides silently (C2, C3). Profiles change tone, length and batching, never the gates, the tests or the security rules.
- **Plain language** by default (Guided); technical language only when the profile says Solo or Team.
- **Git:** follows the project profile. Guided: checkpoint commits after approvals, with the human's agreement; never push unless asked.
- **Independent verification (C14):** `verify` runs in a new session, ideally another model.
- **Secrets:** never read, printed or committed.
- **Versions:** NodFirst starts at 0.1.0 on 2026-11-26. `0.x` until the criteria in `ROADMAP.md` are met.
- **Proven state is honest:** anything not used on a real project is marked "not yet proven" (playbook version line, module `State` line and banner), and `init` asks the human to confirm before using such a module.
- **Sandbox first, then real use:** rules are added only with the defect that justified them (see `lessons-origin.md`).

## How it was built
Two proving grounds before the first release, run with an AI coding agent under the author's review:
1. A web project (email and password accounts; spec, plan, tasks and first implementation tasks; paused after the third task). It produced the security and privacy rules, the handoff list in `plan`, the dependency and human-action rules in `tasks`, and the web module.
2. A Python library parsing Italian deadline phrases (two features, 15 tasks, 160 tests, all gates green from a clean environment). It produced the boundary-input checklist, the revision mode and its three lists (Changes, Interpretations, Downstream impact), the severity rule of `analyze`, the final verification in `implement`, and the library module.
After the release, a first real project (Shortz, a URL shortener; Solo profile, Cursor, modules `web` and `backend`) ran one feature from `init` to `verify` and deployment: see `examples/shortz/` and the Shortz entries in `lessons-origin.md`.

Version 0.1.0 of NodFirst had added, before that real use: the kit/project separation, working profiles, Git checkpoints, command files, `adopt`, `next`, `verify`, `fix`, C13 and C14. These came from a comparison with GitHub Spec Kit (its `converge` command, brownfield guide, agent integrations, and the common criticism of verbose Markdown).

## Known open items
See `../ROADMAP.md`. In short: use NodFirst 0.1 on a real project from `init` to `verify`; test the manual with a non-technical reader; try `adopt`, `verify`, `clarify`, `design`, `design-system` and `specify` Mode C; review `backend`, `mobile`, `desktop` on their first real project.

## Starting prompt for a new agent
> Read `maintainers/CONTEXT.md`, `maintainers/README.md`, `ROADMAP.md` and `CHANGELOG.md`. I want to work on NodFirst: <what you want>. Follow the rules for editing the kit. Show me what you intend to change before editing, and add a line under `[Unreleased]` in the changelog for every change.
