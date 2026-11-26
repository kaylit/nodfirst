# Playbook: Clarify

**Version:** 0.1 (not yet proven)
**Purpose:** remove ambiguity from a spec before planning: resolve open questions and find the gaps nobody wrote down. Works on specs written by the agent and on specs the human wrote by hand.
**Prompt:** `/nodfirst-clarify` (or mention `nodfirst/playbooks/clarify.md`) (add a feature number only if it is not the active one). Extra instructions below.
**Output:** the spec updated in place (revision rules of `specify`, Mode B), with no open questions left. When the human says the spec is clarified, the agent records the status `Clarified` (C2).

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `project/profile.md`, the modules it lists (`nodfirst/modules/`), `nodfirst/templates/spec-template.md`, the active feature's `spec.md`, the other specs (for terms and overlaps), and any reference material the human attached or listed in the spec (images, documents, links).

## Preconditions
- The spec exists and has status `Draft`. If it is already `Approved`, stop and ask whether to reopen it.
- If the spec does not follow the template (the human wrote it by hand), do **not** clarify it yet: tell the human to run `specify` in Mode C first, or offer to do it, and stop.

## Instructions for the agent

Follow `nodfirst/constitution.md`, especially C1, C2, C3, C4 and C6.

1. **Read** everything in "Context to read" completely.
2. **Collect the questions.**
   - Every entry in "Open questions" and every `[NEEDS CLARIFICATION]`.
   - Plus an **ambiguity scan** of the whole spec. Look for:
     - vague words ("fast", "secure", "easy", "etc.", "appropriate", "simple") with no measurable meaning;
     - requirements without a criterion, criteria without a requirement, requirements nobody can test;
     - values stated in two places that differ, or fixed in one place and deferred in another;
     - undefined terms or roles; behaviour that depends on an undefined state;
     - missing failure cases, limits, lifetimes, permissions, what is logged;
     - the **"Specify" checklist of every active module** (for a web app: states, access rules; for a mobile app: permissions and lifecycle; for a backend: contracts and repetition; and so on), applied one by one;
     - UI states that are not described (empty, loading, error, offline, permission denied);
     - **contradictions with reference material:** a screen, document or link that shows something the spec does not say or says otherwise. A visual shows behaviour only if it really shows it (see the design playbook, "Reference material").
3. **Show the list** with a priority (blocks planning / improves quality / cosmetic) and where each item comes from. Ask the human to confirm it.
4. **Ask one question at a time** (Solo and Team: up to three per message), at most 10 in total, most blocking first. For each: the question in plain words (assume the reader is not technical), 2-3 options with what each means for the user of the product, your recommended default and why. Never decide for the human (C3). Questions about technology belong to the plan: note them for the plan instead.
5. **Apply the answers** to the spec in place, following the revision rules of `specify` (stable IDs, withdrawn items kept, new IDs at the end, every requirement with a criterion). Remove the resolved markers and entries.
6. **Check** the spec again with the checks of `specify`, Mode A step 7.
7. **Stop.** Show three lists: **Changes**, **Interpretations** (every place where an answer left room for more than one reading), **Still open** (with the reason, and whether it blocks the plan). Ask the human to review and set the status.

## Do not
- Decide product behaviour on the human's behalf.
- Change the status to `Clarified` or `Approved` unless the human says so (C2); then record it and change nothing else.
- Touch any file other than the spec.
- Ask more questions at once than the working profile allows (Guided: one; Solo and Team: up to three).

## Example
Prompt: `/nodfirst-clarify`
Agent's first message (abridged): "I found 7 points. Blocks planning: (1) the spec says 'sign in quickly' with no limit: what is acceptable? (2) nothing says what happens after 5 wrong passwords. Improves quality: (3) the word 'member' and 'user' are both used. Do you confirm this list?"

## Extra instructions
<!-- Write below this line when you use the playbook. -->
