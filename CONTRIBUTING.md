# Contributing to NodFirst

Thank you for helping. NodFirst improves mostly through **lessons from real use**, so you do not need to write code to contribute.

## Ways to contribute

1. **Share a lesson from real use** (most valuable). An agent misunderstood, skipped a gate, invented something; a rule was vague; a template section was missing or useless. Open an issue with the **Lesson from real use** template. Remove names, secrets and personal data from any excerpt.
2. **Report a problem in the kit:** a broken reference, a contradiction between two files, an error in the manual. Use the **Problem in the kit** template.
3. **Propose a change** with a pull request (below).

## Before a pull request

- For anything larger than a typo, **open an issue first** and describe the change, so we can agree on it before you spend time.
- Read [`maintainers/CONTEXT.md`](maintainers/CONTEXT.md) (what NodFirst is and the decisions already taken) and the rules in [`maintainers/README.md`](maintainers/README.md).

## Rules for changes to the kit

- **A rule comes with the defect that justified it.** Say what went wrong without the rule (a real run is best).
- **English only** in the kit, the manual and the repository. Users may work in any language; the kit itself stays in English.
- **Keep it short.** Playbooks stay one-command friendly; the constitution stays free of stack or project-kind specifics (those go in modules).
- **Plain language in the manual.** It must stay readable by people who do not write code.
- **Be honest about maturity.** Anything not used on a real project is marked "not yet proven".
- **Never weaken an approval gate, a test rule or a security rule** in a playbook or a working profile.
- If you add, rename or change the purpose of a playbook, update `COMMANDS` in `maintainers/tools/build_adapters.py`, run `python3 maintainers/tools/build_adapters.py`, and update the manual (Appendix C).
- The documentation site is generated from the repository files: edit the manual, playbooks or examples, never the site pages. `python3 maintainers/tools/build_site.py` checks that every internal link still works.
- Add a line under `[Unreleased]` in [`CHANGELOG.md`](CHANGELOG.md) naming the files you changed.

## How a pull request is handled

1. Fork the repository, create a branch, make the change, open a pull request against `main`.
2. The maintainer reviews it, may ask for changes, and decides whether to merge. Nothing reaches `main` without review.
3. Be patient: this is a small project maintained in spare time.

## Licence

By contributing, you agree that your contribution is released under the project's [MIT licence](LICENSE).

## Conduct

Be kind and specific. Criticise rules and documents, not people.
