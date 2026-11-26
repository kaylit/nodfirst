# Playbook: Fix (light track)

**Version:** 0.1 (not yet proven)
**Purpose:** a bug fix, or a small change to one behaviour, without the full cycle (constitution, Section 1, light track).
**Prompt:** `/nodfirst-fix` (or mention `nodfirst/playbooks/fix.md`) and, below it, what is wrong or what should change, in your own words.
**Output:** `specs/NNN-short-name/spec.md` with `Track: Light`, a test, the change, and the records updated.

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `project/profile.md`, the modules it lists, the specs that describe the behaviour involved, and the code concerned.

## Instructions for the agent

Follow `nodfirst/constitution.md`, especially C1, C2, C5 and C11.

0. **Resume.** If the human names an existing light spec that is already `Approved` (for example in a new chat), go straight to step 5.
1. **Check that it is light.** It is light only if it changes **one behaviour** and touches **no** data model, public contract (API, file format, message others rely on), authentication, permissions or personal data. If any of these is touched, or you are unsure, say so and recommend the full track (`/nodfirst-specify`). Stop unless the human confirms.
2. **Find the source of truth.** Name the spec and the requirement or criterion that describe the behaviour today (`001-R5`), or say that no spec describes it.
   - A **bug** is code that does not do what the spec says: the spec stays as it is.
   - A **change** is a new or different behaviour: the spec that describes it must change too (C11).
3. **Write the light spec** `specs/NNN-short-name/spec.md` (next free number; set it as `Active feature` in the profile, Section 0) with only: goal (two sentences), the requirement(s) and criteria changed or added, "Impact on existing specs" with the IDs involved, the test that will prove it, and `Track: Light`. For a change, list the edits to the existing spec (as Mode B of `specify` would: IDs stable, withdrawn items kept).
4. **Stop for approval** (C2). In the Solo profile the human may approve this spec and ask you to implement in the same session ("approved, go ahead"); the implementation report is still accepted separately.
5. **After approval:**
   - Apply the edits to the existing spec, if any, and record the approval.
   - **Test first:** write the test that reproduces the bug or describes the change; run it and show it fails for the right reason (C5).
   - Make the smallest change that passes; run the single quality command (profile, Section 5).
   - Report as `implement` does (Task, Before, Tests added, Implementation, Gates, Deviations and interpretations).
6. **Short verification:** re-read the criteria of the light spec against the code and the test, and list any other behaviour the change could affect, with the tests that cover it. For a security-relevant area, recommend `/nodfirst-verify` in a new chat.
7. **Stop.** With git checkpoints, commit when the human accepts (`fix NNN done`).

## Do not
- Use the light track to avoid an approval, a test, or a spec update.
- Change anything outside the behaviour named in the light spec.
