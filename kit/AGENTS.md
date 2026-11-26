# AGENTS.md

This project uses **NodFirst**, a Spec-Driven Development kit: specs come before code, and nothing moves to the next phase until the human approves.

## Read first
1. `nodfirst/constitution.md`: the core rules. It outranks everything else.
2. `project/profile.md`: this project's profile (active feature, working profile, Git, commands, quality gates, exceptions).
3. The active feature: `spec.md`, then `design.md` if it exists, `plan.md`, `tasks.md`.

## Always in force
- **Approval (C2):** only the human approves. When the human says "approved" (or "clarified"), set `Status`, `Approved by` and `Date` in that file as given, and change nothing else. With git checkpoints (profile, Section 2), then commit with a message such as `spec 002 approved` (constitution, Section 4).
- **Do not invent (C3):** no silent decisions; no licence, metadata, configuration or dependency that the spec, plan or tasks do not name. Report every interpretation.
- **Security (C6):** never read, print or commit secrets.
- **Stop** at the end of the playbook. Never start the next phase on your own.
- **Reports (C13):** summary first (at most five lines), then interpretations, open questions, and what was not done or not run. Never claim a check that did not run.
- **Plain language:** unless the profile says Solo or Team, assume the human is not technical (constitution, Section 4).
- **Git** follows `project/profile.md`.

## Playbooks
The human names a playbook (by its command, for example `/nodfirst-specify`, or as `nodfirst/playbooks/specify.md`) and adds a few words. Read everything else from the files listed in the playbook's "Context to read".
If the human asks "where are we?" or "what now?", follow `nodfirst/playbooks/next.md`.

## Where things live
- `nodfirst/`: the kit (constitution, playbooks, templates, modules, manual). Replaced as a whole on update: do not edit it.
- `project/`: this project's profile, lessons log, roadmap, design system.
- `specs/`: one folder per feature.
- `docs/decisions/`: decision records.
