# NodFirst constitution

> Version: 0.1.0 · Part of the NodFirst kit (`nodfirst/`). Replaced as a whole when the kit is updated: never edit it in a project.
> Language: framework files in English. Product and spec content may be in any language.

The constitution holds the **core rules**: they are the same in every project and for every agent.
What is specific to one project lives in **`project/profile.md`** (the project profile), written by `init` or `adopt` and owned by the project. The profile may add rules and record exceptions with a reason; it never removes a core rule silently.

**Modules** (`nodfirst/modules/*.md`) add rules, checklists and typical quality gates for a kind of project (web application, library, backend, mobile, desktop). The profile lists the modules that apply. A module never weakens a core rule. Each module states whether it is **proven** (used on a real project), **partly proven** or **not yet proven**; using one that is not fully proven requires the human's explicit confirmation, recorded in the profile.

Keywords **MUST**, **MUST NOT**, **SHOULD**, **MAY** are used as in RFC 2119.
Rule IDs (C1, C2, …) exist so specs, plans, tasks and reviews can reference them.

---

## 1. Workflow

Phases, in order. Each phase produces a file and ends with **human approval**.

1. **Set-up** → `project/profile.md`: `init` for a new project, `adopt` for an existing code base (once per project)
2. **Specify** → `specs/NNN-name/spec.md` (what and why, no technology)
3. **Clarify** *(optional)* → no ambiguity or open question left in the spec
4. **Design** *(optional, features with a UI)* → `specs/NNN-name/design.md`
5. **Plan** → `specs/NNN-name/plan.md` (how: architecture, data, contracts, risks)
6. **Tasks** → `specs/NNN-name/tasks.md` (small, ordered, verifiable)
7. **Analyze** → `specs/NNN-name/analysis.md`: read-only consistency check of spec, plan, tasks and constitution
8. **Implement** → one task at a time
9. **Verify** → `specs/NNN-name/verification.md`: an independent check of the finished code against spec, plan and constitution

`next` can be run at any time: it reads the files and says where the project stands and what comes next. It changes nothing.

**Two tracks.**
- *Full track*: all phases. Use for any new feature, data-model change, public-contract change or security-relevant change.
- *Light track* (`fix` playbook): bug fixes and changes to a single behaviour that touch no data model, public contract, authentication or personal data. A short spec (goal, acceptance criteria, test), approved by the human, then implementation and a short verification. When in doubt, use the full track.

## 2. Working profiles

The profile chooses one way of working. Profiles change **tone, length and batching**. They never remove an approval gate (C2), a test (C5) or a security rule (C6).

| | **Guided** | **Solo** | **Team** |
|---|---|---|---|
| For | people who do not write code | a developer working alone | several people, with review |
| Language | everyday words; every technical term explained once; one question at a time | technical words allowed; questions may be grouped (at most 3 per message) | technical; questions may be grouped |
| Documents | template sections that do not apply keep their heading with `N/A – reason` and nothing else | same, plus short reports (summary first, details only on request) | same as Solo |
| Approvals | the human approves each phase | the human approves each phase; for a **light-track** change, may approve the spec and let the agent implement in the same session (the implementation report is still accepted separately) | each phase approved by the role named in the profile (for example product for the spec, engineering for the plan); approver and date recorded in the file |
| Implement | one task, then stop | may run "until T<n>" when the human says so | one task or "until T<n>"; one branch and one pull request per feature |
| Git | strongly recommended: the agent creates a checkpoint commit after each approval, with the human's agreement given once in the profile | as the profile says | required: branch per feature, pull request, the quality command in CI |

The default profile is **Guided**.

## 3. Principles

**C1 – Spec is the source of truth.**
No behaviour is implemented that is not described in an approved spec.
If reality and spec diverge, fix the spec first, then the code.

**C2 – Human approval gates.**
An agent MUST NOT move to the next phase until the human has approved the current one.
Approval is explicit, never assumed from silence. Only the human approves; when told to, the agent records the approval (status, name, date as given) and changes nothing else. Statuses such as `Clarified` and `Approved` are set the same way: the human says so, the agent records it.

**C3 – Do not invent requirements or decisions.**
If something is ambiguous, an agent MUST ask or mark `[NEEDS CLARIFICATION: question]`, and MUST report every reading it chose in an "Interpretations" list.
It MUST NOT silently choose product behaviour, add features, widen scope, or add anything (licence, metadata, configuration, dependency) that the spec, plan or tasks do not name.

**C4 – Traceability.**
Every requirement has an ID (`R1`, `R2`, …). Every task cites the requirement IDs it serves.
Every MUST requirement has at least one acceptance criterion that would **fail if the requirement were removed**; listing it as "covered" is not proof.
Every acceptance criterion maps to at least one automated test (or a named manual check, with a reason).
IDs are stable. In references across specs, prefix the feature number (`001-R5`).

**C5 – Tests are mandatory.**
- Business rules and pure logic: unit tests.
- Boundaries (public API, persistence, authentication): integration tests.
- Critical user flows, where the project has a user interface: end-to-end tests. Which flows are critical is decided per spec, with the human.
- Bug fixes: first a failing test that reproduces the bug.
- A task is not done until its tests exist and pass. A test must be able to fail.

**C6 – Security and privacy by default.**
- Validate all input at the system boundary and never trust the caller or the client.
- Where there are users or accounts, authentication and authorization are enforced on the trusted side for every protected operation; users reach only their own data unless a spec says otherwise.
- Secrets live in environment variables or secret stores, never in the repository, logs or client bundles.
- No personal data in logs or error messages; messages do not echo untrusted input.
- Collect the minimum personal data needed.
- Treat user-supplied content as untrusted. Each module names the threat checklist to use as a baseline (for web: the OWASP Top 10).

**C7 – Accessibility by default (projects with a UI).**
A UI MUST meet the accessibility target in the active module and the profile (web: WCAG 2.2 level AA). Projects without a UI record the exception in the profile.

**C8 – Simplicity.**
Prefer the simplest design that satisfies the spec. No speculative features or abstractions.
A new dependency requires a written justification in the plan (what it replaces, maintenance status, size and risk). Pin exact versions of tools and images (never `latest`).

**C9 – Small verifiable increments.**
Work in vertical slices. One deliverable per task; each task leaves the project building, linted, typed and tested, and can be proven inside the task.

**C10 – Architectural decisions are recorded.**
Any significant technical choice is written as a short decision record in the plan or in `docs/decisions/NNN-title.md`: context, options, decision, consequences.

**C11 – Specs stay alive.**
When behaviour changes, the spec changes in the same change set, together with the plan sentences and tests that quote it. A spec that extends another lists its impact on that spec. Outdated specs are defects.

**C12 – Language.**
Framework files, identifiers in code and machine-readable values (error codes, enum values, field names) are in English. User-facing text and product documentation follow the project language set in the profile. The agent talks to the human in the language the human uses.

**C13 – Brevity.**
Write what a reader needs and nothing more. A template section that does not apply keeps its heading and one line: `N/A – reason`; do not repeat in one document what another already says, refer to it. Every report starts with a summary of at most five lines; details follow. A longer document is not a better one.

**C14 – Independent verification.**
The agent that wrote the code does not certify it alone. Before a feature is called finished, `verify` runs in a **new session** (a new chat, ideally another model or another agent), reads only the files, and checks the code against spec, plan and constitution.

## 4. Agent conduct

- Read this constitution, `project/profile.md`, `AGENTS.md`, and the relevant `spec.md`, `plan.md` and `tasks.md` before changing anything.
- Work on one task at a time. State which task and which requirement IDs you address.
- Report deviations, blockers and discovered gaps instead of working around them. When something the task needs is missing (a runtime, a tool, a permission), stop and say so; never lower a constraint to continue.
- Do not edit approved specs or plans to fit the code. Write a change request.
- Never read, print or commit secrets. Never run destructive commands without explicit human approval.
- Do not modify files outside the scope of the current task.
- Before declaring a task done, run the quality gates (profile) and report the result honestly: what was done, what was not run, and the interpretations you chose.
- **Git** follows the profile. When git is used: never push, force-push, rewrite history or delete branches unless the human asks; a checkpoint commit contains the files of the phase or task just approved, plus any change to Section 0 of the profile, with a message that names it (for example `spec 002 approved`). The **first** checkpoint (after `init` or `adopt`) also contains the kit itself (`AGENTS.md`, `CLAUDE.md`, `nodfirst/`), so every saved copy holds the rules it was made with; so does the first checkpoint after a kit update. When git is not used, never mention commits.
- **The human may not be technical.** Unless the profile says Solo or Team, explain in everyday words, say what each option means for the people who will use the product, and explain a technical term in one short sentence the first time you use it.

## 5. Governance

- The constitution changes only with a new version of the kit. A project that needs a different rule records an **exception** in its profile: rule ID, reason, approved by, date.
- Version with semver: MAJOR = principle removed or redefined, MINOR = principle added or expanded, PATCH = wording.
- The constitution outranks the profile's added rules, specs, plans and tasks; recorded exceptions are the only way around a rule. On conflict, stop and ask.
- When two files disagree, this order wins: constitution (with the profile's recorded exceptions) → spec → design → plan → tasks → code.
