<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="media/nodfirst-logo-dark.svg">
    <img src="media/nodfirst-logo-light.svg" alt="NodFirst" width="400">
  </picture>

  <h3>Nothing gets built until you say yes.</h3>

  <p>A Spec-Driven Development kit for any AI coding agent.<br>
  You decide and approve; the agent writes, checks, reports and stops.</p>

  <p>
    <img alt="Version 0.1.0" src="https://img.shields.io/badge/version-0.1.0-1B4A7A">
    <img alt="MIT licence" src="https://img.shields.io/badge/licence-MIT-177A4F">
    <img alt="No install" src="https://img.shields.io/badge/install-copy%20a%20folder-0D2240">
  </p>

  <p><a href="https://kaylit.github.io/nodfirst/"><strong>Read the documentation →</strong></a></p>
</div>

---

## What it is

NodFirst turns "build me an app" into a sequence of short documents you can read and approve: **what** you want (spec), **how** it will be built (plan), **small steps** (tasks), then **one step at a time** with tests, and finally an **independent check** of the result. After every phase the agent stops and waits for your nod.

It is plain Markdown: no program to install, no account, works with Claude Code, Cursor, GitHub Copilot, OpenAI Codex and any agent that can read and edit files. The kit is written in English; you can talk to the agent, and write your specs, in any language.

## Who it is for

| | You… | NodFirst gives you |
|---|---|---|
| **Guided** | have an idea but do not write code | everyday language, one question at a time, a saved copy at every approval, a command that tells you where you are |
| **Solo** | are a developer working alone | short documents, technical language, several tasks in a row when you ask |
| **Team** | work with reviewers | approvals by role, a branch and a pull request per feature, checks in CI |

## Quick start

1. Copy **everything inside** [`kit/`](kit/) into your project folder.
2. Open the folder in your coding tool and write:
   ```
   follow nodfirst/playbooks/init.md
   A web app where a small gym books classes. Italian and English.
   ```
   For a project that already has code, use `nodfirst/playbooks/adopt.md` instead.
3. Answer the questions (or say "your suggestion"). At the end the agent installs the commands for your tool, and from then on:
   ```
   /nodfirst-specify   /nodfirst-clarify  /nodfirst-design   /nodfirst-plan
   /nodfirst-tasks     /nodfirst-analyze  /nodfirst-implement /nodfirst-verify
   /nodfirst-fix       /nodfirst-next     /nodfirst-design-system
   ```
   (in Codex: `$nodfirst-…`).

The documentation site, **[kaylit.github.io/nodfirst](https://kaylit.github.io/nodfirst/)**, has the full manual (written for non-technical readers, with a step-by-step start in Claude and Cursor), a reference page for every command, and the examples. The same manual is in the kit as [`kit/nodfirst/manual.md`](kit/nodfirst/manual.md), so it travels with your project.
To see what the documents look like, and how to review a first draft, open [`examples/`](examples/).

## The cycle

```
init / adopt → specify → (clarify) → (design) → plan → tasks → analyze → implement → verify
                  ▲ your nod      ▲ your nod        ▲ your nod  ▲ your nod  ▲ each task  ▲ new chat
```
`/nodfirst-next` tells you at any moment where you are and what to type next. Small fixes take the light track: `/nodfirst-fix`.

## What makes it different

- **Approval gates are the method, not an option.** Every phase ends with the human's explicit approval, recorded in the file.
- **No silent decisions.** Every report lists the agent's *interpretations*: each place where your words could be read two ways and which reading it chose.
- **Independent verification.** `verify` runs in a fresh chat (ideally another model), reads only the files and the code, and classifies every requirement as met, partial, missing, contradicting or untested — including anything nobody asked for.
- **Tests first, always.** Every task starts with a test that fails for the right reason.
- **Plain language by default**, with every technical term explained once.
- **Honest about maturity.** Every playbook and module says whether it has been used on a real project.
- **Safe updates.** The kit (`nodfirst/`) and your project (`project/`, `specs/`) live in separate folders: updating means replacing one folder.

## NodFirst and GitHub Spec Kit

[Spec Kit](https://github.com/github/spec-kit) is GitHub's open-source toolkit for the same idea, and the reference in this space. They make different trade-offs:

| | NodFirst | Spec Kit |
|---|---|---|
| Install | copy a folder | a command-line tool (Python and uv) |
| Primary reader | someone who may not write code; profiles for solo developers and teams | developers |
| Approval between phases | built into every playbook | available through workflows and extensions |
| Tests | required in every task, written first | generated when the spec or the user asks for them |
| Check of the code against the spec | `verify`, in a separate session | `converge` |
| Screens and design system | `design`, `design-system` | through extensions |
| Ecosystem | small and new | large: many agent integrations, extensions and presets |

If you are a developer who wants the widest integration and a large community, Spec Kit is the mature choice. NodFirst aims at people who want the agent to stop, explain and wait.

## Status

Version **0.1.0**, an early release. Its core was run on two projects before release (a web project and a sandbox library), and on a first real project after it, built and deployed from `init` to `verify` ([Shortz](examples/shortz/)). What has been used for real, and what has not (including changes not yet released):

| Part | State |
|---|---|
| `init` (interview and profile), `specify` (new and revise), `plan`, `tasks`, `analyze`, `implement` | used on three projects |
| Working profile Solo, Git checkpoints, command files for Cursor, `design`, `verify` | used on one project (Shortz) |
| Working profiles Guided and Team, command files for other tools, `init update`, `adopt`, `next`, `fix`; closing a feature and the new `verify` verdict rules (unreleased) | new, not yet used |
| `specify` from your material, `clarify`, `design-system` | written, not yet used |
| Module `library` | proven (sandbox) · module `web`: partly proven, on two projects |
| Module `backend` | used once (Shortz), line-by-line review still to do |
| Modules `mobile`, `desktop` | written from standard practice, not yet used |

Next steps are in [`ROADMAP.md`](ROADMAP.md); changes in [`CHANGELOG.md`](CHANGELOG.md).

## Repository layout

```
kit/              what you copy into your project
  AGENTS.md  CLAUDE.md
  nodfirst/       the kit: constitution, playbooks, templates, modules, adapters, manual
  project/        your project's profile and lessons (skeletons)
  specs/  docs/decisions/
examples/         illustrative documents and how to review them
media/            logo
site/             configuration of the documentation site (pages are generated from the files above)
maintainers/      notes and tools for whoever develops NodFirst
```

## Contributing

Lessons from real use are the most valuable contribution: what the agent got wrong, which rule was vague, which section was useless. Open an issue with the **Lesson from real use** template. To propose changes, read [`CONTRIBUTING.md`](CONTRIBUTING.md). Maintainers: start from [`maintainers/CONTEXT.md`](maintainers/CONTEXT.md).

## Licence

[MIT](LICENSE) © 2026 Luca Lanzano'
