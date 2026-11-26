# Modules

A module adds rules, checklists and typical quality gates for one **kind of project**, on top of the constitution. A module never weakens a core rule. `init` (or `adopt`) asks which modules apply and records them in `project/profile.md`, Section 1.

Playbooks read the active modules listed in the profile (`Context to read`) and apply their checklists in `specify`, `plan` and `tasks`.

| Module | File | State |
|---|---|---|
| Library or package | `library.md` | **Proven** on a sandbox project (two features, fifteen tasks) |
| Web application | `web.md` | **Partly proven** on a real project; see "Not yet proven" in the file |
| Backend service (HTTP API, jobs, events) | `backend.md` | **Not yet proven**, written from standard practice |
| Mobile app (native or cross-platform) | `mobile.md` | **Not yet proven**, written from standard practice |
| Desktop app | `desktop.md` | **Not yet proven**, written from standard practice |
| LLM features (prompts, models, evaluation) | *not written* | Write the module when the first real project needs it. Start from the core and ask the human; do not copy another module |

**Several modules at once** are normal: a web app with its own server activates `web` and `backend`; a mobile app with a server activates `mobile` and `backend`. When two modules disagree, the stricter rule wins; record the conflict in the profile, Section 10.

**State values.** *Proven*: used on a real project end to end. *Partly proven*: some phases used; the unproven parts are listed in the module. *Not yet proven*: never used. `init` warns the human and asks for confirmation for the last two cases (for *partly proven*, it names the unproven parts).

**An unproven module** is a starting checklist, not a verdict: the first project that uses it reviews every rule, records in `project/lessons.md` what was wrong or missing, and the module is updated afterwards.
