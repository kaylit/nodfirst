# Playbook: Plan

**Version:** 0.1 (tested on three projects, including a change request after verification)
**Purpose:** turn an approved spec into `plan.md`: how the feature will be built, with every technical decision recorded.
**Prompt:** `/nodfirst-plan` (or mention `nodfirst/playbooks/plan.md`) (and a feature number only if it is not the active one). Extra instructions go below.
**Output:** `specs/NNN-feature-name/plan.md`, status `Draft`.

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `project/profile.md`, the modules it lists (`nodfirst/modules/`), `nodfirst/templates/plan-template.md`, the active feature's `spec.md` (and `design.md` if any), existing plans, `docs/decisions/`, and the code base if any.

## Preconditions
- The spec status is `Approved` and its "Open questions" are empty. `Clarified` is not enough: the human must approve the spec. If not, stop and say so (C2).
- If the feature has a UI and the human wants a design phase, `design.md` should exist first; otherwise ask whether to skip it.

## Instructions for the agent

You are designing, not coding. Follow `nodfirst/constitution.md`, especially C1, C2, C3, C4, C6, C8, C10.

1. **Build the handoff list.** Before designing anything, show the human three groups:
   - **A. Explicit deferrals:** everything the spec defers to the plan (search for "in the plan" and its equivalent in the spec's language, and read Security and privacy).
   - **B. Implied mechanisms:** go through every requirement and criterion and ask "which mechanism satisfies this, and is it already fixed by the spec or the constitution?". Use the "Plan" checklist of every active module and the question "where can state live in the hosting environment?". Include scaffolding, tools and runtimes the feature needs on the machine, and how each mechanism is tested **locally and in CI with the same component as in production** (a database, a driver or a service that differs between test and production is a decision to take, not a detail).
   - **C. Profile and constitution:** the open decisions of the profile (Section 11) this feature needs, and the constraints of the profile and the constitution, listed explicitly.
   Report spec inconsistencies as **spec change requests**, not plan decisions. Ask the human to confirm or correct the list.
2. **Resolve technical decisions one at a time.** For each undecided choice:
   - Research current information (versions, maintenance, limits, pricing). Never rely on memory; cite sources and write "verified on <date>". Standard-library facts you rely on are verified too (for example a constant or a limit).
   - **Release age:** when a choice is not urgent and the version was published in the last 7 days, read its release notes and say what you found; prefer the previous stable release unless the new one is needed.
   - Present 2-3 options with pros and cons against the criteria in the profile's open decisions (Section 11), and your recommendation. For foundational decisions check each option against the requirement IDs it touches; a requirement an option cannot satisfy is a **spec change request**.
   - Order decisions by dependency. Wait for the human's decision. Never choose on their behalf (C3).
   - Record each decision as context, options, decision, consequences (C10). Give an example of use from the caller's side when the decision shapes a public interface.
   - Pin container image tags and tool versions; never `latest`.
   **Security checks for every mechanism:** apply the active modules' checklists (for web: client-controlled values, who can read and write each client-side mechanism, cookie lifetime and attributes, keyed hashes for low-entropy identifiers, library defaults, counters and windows).
   - The constitution check lists **every** rule and states compliance. Keep the template's text for the C2 row; never write the approval status of the plan.
3. **Write `plan.md`** from the template:
   - Map every handoff item to a mechanism or an open question.
   - Security and privacy: for each point of the spec, the mechanism and how it is tested.
   - **Test strategy:** every criterion gets a level and a description naming the inputs that would make the test fail. Name the test infrastructure (runner, fixtures, services) and where it comes from.
   - Interfaces cite the requirement IDs. Dependencies are justified (C8).
   - User-facing texts the plan fixes (messages, labels) are proposed in a table and approved before the plan is approved.
   - **Technical context lists the tools and runtimes** needed on the machine, each with its verification command.
   - Include scaffolding as a described step (it becomes tasks). Do not run commands or create code.
   - **Order the steps so each leaves the quality gate green.** When the feature changes behaviour that existing tests cover, the step that updates those tests comes first and stays green before and after the change. The "planned steps" section is indicative: the tasks may split it.
   - **Impact on other specs and plans:** if the spec lists impact on existing specs, state which tests change and add a note "no change to plan NNN" or the change request needed.
4. **Do not change the spec.** Gaps, contradictions or untestable items become a **spec change request** (what, why, suggested wording).
5. **Check your work:**
   - Every R and AC appears in interfaces, security or test strategy.
   - Every deferral is resolved or an open question; **no open question remains in a plan proposed for approval.**
   - No decision without the human's confirmation; no unverified fact stated as certain.
   - Machine identifiers are English; user-facing text follows the project language.
   - Nothing adds behaviour the spec does not describe (C1).
6. **Stop.** Show decisions taken, decisions pending, assumptions, spec change requests, open questions and **interpretations**. Do not create tasks or code (C2).

## Checklist for every project (core)
State where state lives; how failures surface to callers; what is logged; what the tests run against; tools and versions. Project-kind checklists (security mechanisms for web, text parsing and public APIs for libraries, and so on) are in the modules listed in the profile.

## Revising an existing plan
Edit in place, keep a change log at the end, re-run the checks of step 5, and show two lists (changes and interpretations). **Parts the change request does not mention stay identical** (no "..." in tables). Compare with the previous version before showing it. **When the spec changed, update every plan sentence that quotes a changed requirement or criterion** (test strategy, security table, interfaces) in the same round, or list it as an open change request.

## Do not
- Choose technology without the human's decision, invent versions, limits or prices, edit the spec, create tasks or code, or mark the plan `Approved`.

## Extra instructions
<!-- Write below this line when you use the playbook. -->
