# Changelog

All notable changes to NodFirst. Format: one section per version, newest first.
Versioning: `0.x` until the criteria in `ROADMAP.md` are met; until then any minor version may change files.
Categories: **Added**, **Changed**, **Fixed**, **Removed**. Each entry names the files that changed (paths inside `kit/`), so users can replace only those; when only `nodfirst/` changed, replacing that folder is enough.

## [Unreleased]
<!-- Add entries here as you work; move them under a version when you tag it. -->

### The repository
- **Added** `examples/shortz/`: the documents of the first real project run with NodFirst 0.1.0 (a URL shortener, one feature from `init` to `verify`, three verification runs by another model, deployed), with a README on how it went and what it taught the kit. Hosts and account names replaced. No kit file changed.
- **Changed** `examples/README.md` (the new example) and `maintainers/tools/build_site.py` (site pages for it).

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
