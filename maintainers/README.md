# Maintainers' notes

Files here are about **evolving NodFirst**. They are not copied into user projects.

## How we work
- Work on short branches merged into `main`. Versions `0.x`, tagged `v0.1.0`, `v0.2.0`, …
- Small changes: edit the file, add a line under `[Unreleased]` in `CHANGELOG.md` naming the files (paths inside `kit/`).
- A lesson from a project (something an agent got wrong, a rule that was vague) becomes: (1) a line in that project's `project/lessons.md`; (2) if general, a change to a playbook, template, module or the constitution here; (3) a line in `CHANGELOG.md`; (4) the playbook's `Version` bumped.
- To release: move `[Unreleased]` entries under a new version with the date, update `kit/nodfirst/VERSION`, the version badge in `README.md` and the manual's version line, write `releases/vX.Y.Z.md`, then `git tag vX.Y.Z`.
- Next steps live in `ROADMAP.md`.

## Rules for editing the kit
- Keep playbooks short and one-line-prompt friendly: rules in the playbook, not in the prompt.
- Keep the constitution free of stack or project-kind specifics; those belong in modules.
- Anything that belongs to a user's project goes in `kit/project/` (skeletons only); anything in `kit/nodfirst/` must be replaceable as a whole on update.
- When a playbook is added, renamed or its purpose changes: update `COMMANDS` in `tools/build_adapters.py` and run `python3 maintainers/tools/build_adapters.py`; update the manual (Appendix C), `next` if the phase order changed, and the README.
- When the profile skeleton (`kit/project/profile.md`) changes, describe the change in the changelog so `init update` can propose it to existing projects; never rename or renumber existing sections without a MAJOR change.
- A rule is added only with the defect that justified it (see `lessons-origin.md` for the format).
- Mark anything never used on a real project as "not yet proven" (playbook version line, module `State` line and banner).
- The manual (`kit/nodfirst/manual.md`) must stay readable by non-technical people: plain words, an example per concept.

## Releasing an update to users
Tell users which files changed (the changelog lists them). They replace `nodfirst/` (and `AGENTS.md`, `CLAUDE.md` if listed), keep `project/`, `specs/` and `docs/`, and run `/nodfirst-init update`.

## Files
- `CONTEXT.md`: what NodFirst is, decisions taken with the author, how it was built, and a starting prompt for a new agent.
- `lessons-origin.md`: lessons from the two proving projects that shaped the rules.
- `tools/build_adapters.py`: regenerates `kit/nodfirst/adapters/` (standard library only).
- `tools/build_site.py`: generates the documentation site (`.site-build/`) from README, manual, kit, examples and project files; run by `.github/workflows/pages.yml` on every push to `main`. The site's configuration and colours are in `site/`. It fails if a page links to a site page that does not exist.
- `releases/`: release notes, one file per version, to paste into the GitHub release.
