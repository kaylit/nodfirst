# Playbook: Analyze

**Version:** 0.1 (tested on three feature runs)
**Purpose:** a read-only consistency check across constitution, spec, design (if any), plan and tasks, before implementation starts. It can be run again after any revision.
**Prompt:** `/nodfirst-analyze` (or mention `nodfirst/playbooks/analyze.md`) (add a feature number only if it is not the active one).
**Output:** `specs/NNN-feature-name/analysis.md` (the only file you may create or overwrite). Nothing else changes.

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `project/profile.md`, the modules it lists (`nodfirst/modules/`), and for the active feature: `spec.md`, `plan.md`, `tasks.md`, `design.md` if it exists, and the previous `analysis.md` if it exists.

## Preconditions
The spec, plan and tasks exist.

## Instructions for the agent

You are a reviewer, not an editor. Follow `nodfirst/constitution.md`.

1. **Read** every file completely.
2. **Report approval status separately, never as a finding:** for spec, plan and tasks give Status, who approved, date, and whether the file was **modified after its approval stamp** (compare content with the other files' change logs and dates). Open questions and open change requests go here too.
3. **Build the traceability matrix:** each active requirement → the acceptance criteria that **prove** it → plan section → tasks → named tests. Withdrawn items are listed apart. Add a second table: each criterion → task → test, with "does the test really verify it?".
4. **Run these checks** and record each problem as a finding:
   - **Proof:** every MUST requirement has at least one criterion that would **fail if the requirement were removed**. A criterion that lists the requirement in "Covers" but does not observe it is not proof.
   - **Contradictions:** for every token several criteria mention (a number, a form, singular/plural, a limit), read them side by side; do the same across spec, plan and tasks.
   - **Stale text:** after a revision, every plan or tasks sentence that quotes a changed criterion or requirement must match the spec. Do not compare the plan's "planned steps" section line by line with the tasks: it is indicative and the tasks may split it.
   - **Parallel wording:** tables or criteria that describe parallel cases use the same wording.
   - **Vacuous assertions:** a check such as "the message does not contain the input" is empty for empty input; a test that cannot fail is a finding.
   - **Dependencies and order:** each task's tests only use work done by earlier tasks; test infrastructure exists before the first task that needs it; environment and tool prerequisites are listed.
   - **Constitution:** C1-C14 and the exceptions recorded in the profile.
   - **Security items** of the spec each have a mechanism and a test.
5. **Severity:**
   - **Critical:** a behaviour that is **not specified or not tested**; a contradiction between spec, plan and tasks that would make two correct implementations differ; a constitution violation; a security item with no mechanism.
   - **High:** a requirement with no proving criterion (the behaviour is tested only by chance or only in tasks); a criterion with no test; a task with no source; an unverified decision stated as fact; an unjustified dependency.
   - **Medium:** stale or inconsistent text between documents while the behaviour is still specified and tested; ambiguity; tasks too large; stale approval stamp.
   - **Low:** wording, order, duplication, cosmetic.
6. **For every finding** give: ID, severity, where (file and item), what is wrong, the smallest fix and the file that must change (a spec fix is a change request).
7. **Verdict:** `ready to implement` only with no Critical and no High (a High the human has accepted is listed with that decision). Otherwise `not ready`, with the minimal path.
8. **Stop.** Show counts by severity and the verdict. Do not fix anything. Put the run number and date in the header; a re-run overwrites the file.

## Do not
- Edit any file other than `analysis.md`.
- Count approval state as a finding of Critical or High.
- Raise severity to force action. Severity follows what is specified and tested.
- Soften findings. If something cannot be verified, say so.

## Extra instructions
<!-- Write below this line when you use the playbook. -->
