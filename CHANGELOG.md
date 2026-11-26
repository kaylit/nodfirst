# Changelog

All notable changes to NodFirst. Format: one section per version, newest first.
Versioning: `0.x` until the criteria in `ROADMAP.md` are met; until then any minor version may change files.
Categories: **Added**, **Changed**, **Fixed**, **Removed**. Each entry names the files that changed (paths inside `kit/`), so users can replace only those; when only `nodfirst/` changed, replacing that folder is enough.

## [Unreleased]
<!-- Add entries here as you work; move them under a version when you tag it. -->

## [0.2.1] — 2026-11-26 — light track, end to end

**Updating from 0.2.0:** replace `nodfirst/`; then `/nodfirst-init update` (it now reads `nodfirst/CHANGES.md`). No profile change.

### The kit (`kit/`)
- **Added** `nodfirst/CHANGES.md`: what each version asks a project to replace, profile changes and the effect on work in progress; read by `init update` (`nodfirst/playbooks/init.md`, 0.2) instead of asking for release notes.
- **Changed** how a light fix finishes: accepted report; or, if security-relevant, `verify` in a new chat and then `/nodfirst-verify close`, the fix staying the active feature until then; no roadmap line for light fixes. Files: `nodfirst/playbooks/fix.md` (0.2), `nodfirst/playbooks/next.md` (0.3), `nodfirst/manual.md` (Part 8, Appendix E).
- **Changed** `verify` on a light fix: no `tasks.md`; checks the light spec, the specs and plan decisions it changes, and the commits of the fix; at closure, profile and roadmap are updated only where they name the feature. File: `nodfirst/playbooks/verify.md` (0.3).

### The repository
- **Changed** `README.md` (status), `maintainers/README.md` (release steps include `CHANGES.md`), `maintainers/lessons-origin.md` (three Shortz entries).

## [0.2.0] — 2026-11-26 — lessons from the first real project

**Updating from 0.1.0:** replace `nodfirst/` and `AGENTS.md`; keep `project/`, `specs/`, `docs/`; run `/nodfirst-init update` (it refreshes the commands of your tool). The profile skeleton did not change. A feature in progress continues as it is; when it reaches `verify`, the new verdict rules and the closing step apply.

### The kit (`kit/`)
- **Added** closing a feature: after `verify`, the human either fixes or closes the feature; a closure names every Critical or High finding left with a reason and a follow-up, and the verdict is never changed to fit it. The agent records a **Closure** section in `verification.md`, `Active feature: none` in the profile and the closing line in `project/roadmap.md`. Files: `nodfirst/playbooks/verify.md` (0.2), `nodfirst/playbooks/next.md` (0.2), `nodfirst/playbooks/implement.md` (0.2), `nodfirst/manual.md` (7.8, Appendices B and C), `nodfirst/adapters/*/nodfirst-verify*` (description and hint: `/nodfirst-verify close`). Lesson: Shortz, `maintainers/lessons-origin.md`. Replacing `nodfirst/` is enough; no profile change.
- **Changed** `verify` verdicts: a check that could not be done from here (a device, a console, production, a person) goes to **Needs a human** as a checkbox, never as a finding and never as passed; `partly verified` means no Critical or High finding but human checks still open; `verified` means nothing open. A re-run lists every previous finding as closed, still open or reclassified, with a reason for any change of severity. Closing a feature also needs every open human check done or accepted. Files: `nodfirst/playbooks/verify.md`, `nodfirst/playbooks/next.md`, `nodfirst/manual.md` (7.8). Lessons: Shortz (F9 and F10 blocked the verdict; runs 2 and 3 disagreed).
- **Added** lessons in every project: the agent proposes a `project/lessons.md` entry when the human corrects it or a document, and up to three when a feature is closed; it writes only the entries the human accepts. Files: `AGENTS.md` (replace it too), `nodfirst/playbooks/verify.md`, `nodfirst/manual.md` (Part 13), `project/lessons.md` (new projects only: in an existing project, its header text may stay as it is). No profile change. Lesson: Shortz.
- **Changed** constitution 0.1.1 (wording only: what "proven" means for a module).
- **Changed** maturity after the first real project (Shortz): version lines of `init`, `specify`, `design`, `plan`, `tasks`, `analyze`; `web` partly proven on two projects (what Shortz proved, what is still unproven); `backend` used once, still *not yet proven* until its line-by-line review; *Proven* now means used end to end on a project, real or a sandbox, and the module says which (`library`: sandbox). Files: `nodfirst/playbooks/` (those six), `nodfirst/modules/README.md`, `web.md`, `backend.md`, `library.md`, `nodfirst/constitution.md` (wording of "proven", Section intro), `nodfirst/manual.md` (Appendix E, new 14.3).

### The repository
- **Added** `examples/shortz/`: the documents of the first real project run with NodFirst 0.1.0 (a URL shortener, one feature from `init` to `verify`, three verification runs by another model, deployed), with a README on how it went and what it taught the kit. Hosts and account names replaced. No kit file changed.
- **Changed** `examples/README.md` (the new example) and `maintainers/tools/build_site.py` (site pages for it).
- **Changed** `README.md`: status table after Shortz; the quick start lists every command. `maintainers/CONTEXT.md`: Shortz in "How it was built".

## [0.1.0] — 2026-11-26 — first release (pre-release)

### The kit (`kit/`)
- **Constitution** (`nodfirst/constitution.md`): workflow (set-up, specify, clarify, design, plan, tasks, analyze, implement, verify; light track), working profiles **Guided**, **Solo** and **Team**, core rules C1–C14 (including C13 Brevity and C14 Independent verification), agent conduct and Git checkpoints.
- **Project profile** (`project/profile.md`): active feature, working profile, Git, scope, technical profile, commands, quality gates, exceptions, open decisions. Owned by the project; kit updates never replace it.
- **Playbooks** (`nodfirst/playbooks/`): `init` (with an "after a kit update" mode), `adopt`, `next`, `specify` (Modes A, B, C), `clarify`, `design-system`, `design`, `plan`, `tasks`, `analyze`, `implement`, `verify`, `fix`.
- **Templates** (`nodfirst/templates/`): spec, design, plan, tasks.
- **Modules** (`nodfirst/modules/`): `library` (proven), `web` (partly proven), `backend`, `mobile`, `desktop` (not yet proven).
- **Command files** (`nodfirst/adapters/`) for Claude Code, OpenAI Codex, Cursor and GitHub Copilot, installed by `init` and `adopt`.
- **Manual** (`nodfirst/manual.md`) for non-technical readers, with a step-by-step start in Claude and Cursor, Git in plain words, and examples.
- `AGENTS.md`, `CLAUDE.md`, `nodfirst/VERSION`.

### The repository
- Documentation site at kaylit.github.io/nodfirst (GitHub Pages, Just the Docs v0.12.0), generated from the repository files by `maintainers/tools/build_site.py` and published by `.github/workflows/pages.yml`.
- `examples/book-club/`: an illustrative first draft (profile, roadmap, spec) and its review.
- Logo (`media/`), MIT licence, `CONTRIBUTING.md`, issue templates, maintainer notes and tools (`maintainers/`).

### Before release
The core phases were run on two proving grounds: a web project (account feature, paused after the third task) and a Python library (two features, 15 tasks, 160 tests). An independent dry run of `init`, `next` and `specify` found 19 issues, all fixed in this release. See `maintainers/lessons-origin.md`.
