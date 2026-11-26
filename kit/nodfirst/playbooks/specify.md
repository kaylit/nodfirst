# Playbook: Specify

**Version:** 0.1 (Modes A and B tested on two projects; Mode C not yet proven)
**Purpose:** turn a feature idea into a draft `spec.md`, or revise an existing spec.
**Prompt:** `/nodfirst-specify` (or mention `nodfirst/playbooks/specify.md`) and, below it, the idea (Mode A), the change requests (Mode B), or the text and files you wrote or collected (Mode C), in any language.
**Output:** `specs/NNN-feature-name/spec.md`, status `Draft`.

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `project/profile.md`, the modules it lists (`nodfirst/modules/`), `nodfirst/templates/spec-template.md`; the goals of existing specs (skim); in Mode B also the active feature's spec, and plan and tasks if they exist (to report downstream impact).

## Instructions for the agent

You are writing a specification, not code. Follow `nodfirst/constitution.md`, especially C1, C2, C3, C4 and C6.

### Mode A: new spec

1. **Understand the idea.** Restate it in 2-3 sentences and list your assumptions. Do not write the spec yet.
2. **Ask before writing.** Ask only questions that would change the spec materially, one at a time (Solo and Team profiles: up to three per message), with your proposed default. At most 5. Prefer: who the user is, what is in/out of scope, what happens on failure, what is critical. Do not ask about technology.
3. **Create** `specs/NNN-feature-name/spec.md` (next free three-digit number, short kebab-case name). Fill the template (optional sections that do not apply: keep the heading with `N/A – reason`), number everything (`US`, `R`, `AC`). Keep the template's section numbers; a section that does not apply stays with `N/A – reason` and nothing else (C13). Set `Active feature` in `project/profile.md`, Section 0, to the new folder and say so in the report.
4. **Mark unknowns** as `[NEEDS CLARIFICATION: question]` and an entry in "Open questions". Do not guess product behaviour (C3).
5. **Look for what is missing.** Ask what a careful reviewer would find absent: failure cases, limits, lifetimes, who may do what, what happens offline, what is logged. Add each as a requirement, a decision in "Security and privacy", or an open question. Apply the "Specify" checklist of every active module.
   - **Boundary inputs.** For anything people type: empty, too long (and how length is counted), spaces at the ends, upper and lower case, accents. State what happens in each case. Deeper checklists (text encodings, digits of other scripts, wrong types from a calling program) are in the active modules, for example `library`.
   - **Prerequisites.** If the feature needs something no spec describes yet (for example signing in), do not specify it here: record it as an assumption and an open question, and suggest adding it to `project/roadmap.md`.
6. **Keep it technology-free.** No frameworks, libraries, database, endpoints or code. Technology in the idea becomes a constraint under "Open questions" for the plan.
7. **Check your work** before showing it:
   - Every requirement is testable and has an ID and a story.
   - **Every MUST requirement has at least one criterion that would fail if the requirement were removed.** Listing it in "Covers" is not proof.
   - Every criterion cites at least one requirement. Every edge case maps to a requirement or criterion.
   - **No two criteria contradict each other.** For every token that several criteria mention (a number, a form, singular/plural, a limit), read them side by side.
   - **Machine identifiers** (reason codes, enum values, field names) are in English; user-facing text follows the project language.
   - A "must not contain or repeat" check is vacuous for empty input: say what holds instead.
   - Critical flows are listed with a reason. If there is a UI: empty, loading, error and offline states.
   - "Security and privacy" is filled (or N/A with a reason). For accounts, sessions, user data or user input confirm: access rules, repeated-attempt limits, information leaks, lifetimes, input limits, what is logged and what never is, personal data and retention, how credentials and secrets are stored (never reversibly) and transmitted (only encrypted).
   - Nothing in "Out of scope" contradicts a requirement.
   - **Extension of another spec:** if this spec adds to or changes behaviour that another spec defines (a closed list, an out-of-scope item, an example in a criterion), fill "Impact on existing specs" with each affected item and each test that will need updating. Do not edit the other spec; refer to its items with the feature prefix (001-R5). Parallel table rows or criteria use the same wording.
   - **No `[NEEDS CLARIFICATION]` marker remains in a spec proposed for approval:** resolve it, or turn it into an explicit deferral to the plan with the reason.
8. **Stop.** Show: goal, number of requirements and criteria, open questions, assumptions, decisions you took on the human's behalf. Do not start any other phase (C2).

### Mode B: revise an existing spec

1. Read the spec and the change requests. Edit only the spec.
2. **IDs are stable:** never renumber or reuse. A removed requirement stays in the table as `Withdrawn` with the reason and where it moved. New items get the next free ID.
3. Resolved open questions: remove the marker, apply the decision, delete the entry from "Open questions".
4. **Parts the change request does not mention stay identical** (no compaction of tables).
5. After a change to a rule or form, **re-read every criterion and edge case that mentions the same token.**
6. Re-run the checks of Mode A step 7. Update "Last updated". Set the status to `Draft`.
7. **Stop.** Show three lists:
   - **Changes:** what changed, with IDs added, changed or withdrawn.
   - **Interpretations:** every ambiguity in the change request, the reading you chose and the alternative. Never resolve an ambiguity silently.
   - **Downstream impact:** the other specs, the sections of the plan (test strategy, security table, change log) and the tasks (mapping, traceability) that quote a changed ID. Do not edit them: the human decides whether to align them in the same round.

### Mode C: adopt material the human wrote or collected

Use when the human already has a spec in their own words, a document, notes, a product brief, screenshots, mockups or links (for example Figma), and wants them turned into a spec in the template.

1. **List what you received** (each file or link, with what it appears to contain). Links you cannot open: say so and ask for an export (image, PDF or text); never guess their content.
2. **Keep the human's words.** Do not rewrite meaning. Map each statement to the template (story, requirement, criterion, out of scope, open question) and show the **mapping list**: source sentence → place in the spec. Anything that does not fit the template goes to "Open questions", not to the bin.
3. **Images and mockups are evidence of behaviour only when they show it.** Write down what you *read* from each (screens, actions, texts, states) and ask the human to confirm that reading. A screen shows what users see; it does not by itself prove a rule (a limit, a permission, a lifetime): such rules become open questions. Visual style goes to the design phase, not to the spec.
4. **Conflicts are reported, never resolved silently:** between two documents, between text and image, or between the material and the constitution. Order of authority when the human has not said otherwise: the human's explicit statement in this conversation > written spec text > images and mockups > inferred intent.
5. Then continue as in Mode A from step 4 (mark unknowns, look for what is missing, keep it technology-free, check, stop). Add to "Stop": the mapping list, the reading of each image, and the conflicts found.

## Do not
- Invent features "that would be nice", copy technical choices from the profile, or mark the spec `Clarified` or `Approved` by yourself.

## Feature idea or change requests
<!-- Write below this line when you use the playbook. -->
