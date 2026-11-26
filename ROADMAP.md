# NodFirst roadmap

Update this file whenever a step is done or a new one appears; record finished work in `CHANGELOG.md`.
Status: `[ ]` to do · `[~]` in progress · `[x]` done.

## Toward 1.0 (criteria)
- [ ] Used end to end on at least one real web project and one real library, with lessons applied.
- [ ] A non-technical person follows the manual alone in the Guided profile and completes `init` and one feature up to `verify`.
- [ ] A team uses the Team profile on one feature, with approvals by role and a pull request.
- [ ] All playbooks and modules marked "not yet proven" have been used once, or are removed.

## Next
- [ ] **First real project with NodFirst 0.1:** run `init` to `verify`; check the working profile, Git checkpoints and command files in at least two tools.
- [ ] **Manual test with a non-technical reader:** record where they get stuck; fix the manual.
- [ ] **Try `adopt`** on an existing code base.
- [ ] **Try `verify` with a different model** from the one that implemented; compare its findings with a human review.
- [ ] **Try `clarify`, `design`, `design-system` and `specify` Mode C** on a real feature, with images and a design-tool file.
- [ ] **First `mobile`, `desktop` or `backend` project:** review the module line by line; change its state.

## Backlog
- [ ] Optional document checker (stdlib-only script, or CI action): IDs, traceability, leftover `TBD` or `[NEEDS CLARIFICATION]` in approved files, statuses. Decided for 0.1: Markdown only; re-evaluate after real use.
- [ ] Command files for more tools (Gemini CLI, Windsurf, others) once their formats are checked.
- [ ] Module for features built on AI models (prompts, models, evaluation, safety). Write only after a real project needs it.
- [ ] `examples/`: a small **real** feature (spec, plan, tasks, analysis, verification) with "why it is done this way" notes, taken from a real run. (0.1.0 has an illustrative first draft and its review.)
- [ ] Optional light mode of `init` for tiny projects (fewer questions).
- [ ] Open items from the origin web project: browser coverage in end-to-end tests (Firefox); database-backed tests need a proxy container with a pinned image tag.
- [ ] Manual in other languages (decision so far: English only).

## Done
- [x] Flow proven on a web project (partly) and on a library (fully), before the first release.
- [x] Modules `web`, `library`, `backend`, `mobile`, `desktop` written.
- [x] Manual for non-technical readers.
- [x] Documentation site (GitHub Pages), generated from the repository files.
- [x] 0.1.0: name, licence, kit/project separation, working profiles, `adopt`, `next`, `verify`, `fix`, command files.
