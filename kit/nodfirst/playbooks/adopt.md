# Playbook: Adopt (existing project)

**Version:** 0.1 (not yet proven)
**Purpose:** bring NodFirst into a project that already has code: write the project profile from what exists, describe today's behaviour as a starting spec, and list the risks, so that new features follow the normal cycle.
**Prompt:** `/nodfirst-adopt` (or mention `nodfirst/playbooks/adopt.md`) and a few lines about the project and what you want to do next with it.
**Output:** `project/profile.md`, `specs/000-current-behaviour/spec.md` (status `Draft`), `project/roadmap.md`, `project/lessons.md`, command files for the human's tool. **No change to the existing code.**

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `nodfirst/VERSION`, `project/profile.md` (skeleton), `nodfirst/modules/README.md` and the modules it lists, `nodfirst/adapters/README.md`, `nodfirst/templates/spec-template.md`, and the existing repository: README and docs, build and package files, configuration, tests, CI files, and the source tree.

## Instructions for the agent

Follow `nodfirst/constitution.md`, especially C1, C2, C3 and C13. Until the working profile is chosen, speak as in the **Guided** profile.

1. **Do steps 1 to 4 of `init`** (preconditions, restate the project, working profile, Git), with one difference: the existing code is expected, and the residue audit lists only leftovers of the kit or of another project, never the project's own files.
2. **Map the existing project** (read, do not run anything that changes state):
   - kind of project and matching modules (with the proven-state warning of `init`, step 5.2);
   - languages, frameworks and runtimes with their versions, from the project files;
   - how to install, build, run and test it (from README, package files, scripts, CI); **run the test command once** if the human agrees, and record the result (number of tests, failures, time);
   - main areas of the code and what each does, in plain words;
   - where data is stored, which external services are called, how users sign in (if they do), where secrets come from (names only, never values).
3. **Interview the human** only for what the code cannot tell you (topics of `init`, step 5): who uses it, what must not break, what is planned next, quality expectations, legal regimes. At most 10 questions; one at a time in the Guided profile.
4. **Draft `project/profile.md`** as `init` step 7 does, with **Commands filled in** from what you found (marked "found, not yet verified" for any command you did not run) and quality gates that the project can pass **today** (list the gates the project should reach as open decisions, not as gates that fail on day one).
5. **Draft `specs/000-current-behaviour/spec.md`** from the spec template: the behaviour the product has **today**, as seen in the code, tests and documentation. Requirements describe what exists, not what should exist. For each requirement say where you saw it (file, test) and whether a test covers it. Behaviour you are not sure about becomes an open question, never a guess. Keep it to the main user-visible behaviour (C13); details are added when a feature touches them.
6. **Risk list** in the summary (not a file): areas with no tests, security concerns seen while reading (C6), outdated or unpinned dependencies, secrets in the repository (name the file, never the value), anything that contradicts the constitution — each with a suggested first feature or fix.
7. **Stop for approval** (C2): show the profile summary, the spec summary (number of requirements, how many are covered by tests), the risk list and the open questions.
8. **After approval:** create `project/roadmap.md` (the human's next features plus the risks they chose to address), `project/lessons.md`, `docs/decisions/` (with a first record for each important existing technical choice, marked "existing, recorded at adoption"), install the command files (`nodfirst/adapters/README.md`), record the approval in the profile header, and with git checkpoints commit the kit (`AGENTS.md`, `CLAUDE.md`, `nodfirst/`), the command files, `project/`, `specs/000-current-behaviour/` and `docs/` with the message `nodfirst: project adopted` (constitution, Section 4).
9. **Stop.** Suggest the next step: `/nodfirst-specify` for the first feature, or `/nodfirst-fix` for a first small fix. New specs that change existing behaviour list their impact on `000-R…` items.

## Do not
- Change, format, upgrade or "clean up" existing code, dependencies or configuration.
- Describe behaviour you did not see in the code, tests or documentation.
- Read or print the value of a secret.
