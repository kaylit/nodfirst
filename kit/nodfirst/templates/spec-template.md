<!--
SPEC TEMPLATE v0.1 — copy to specs/NNN-feature-name/spec.md
Rules for whoever fills this in (human or agent):
- Describe WHAT users need and WHY. No technology, no code, no database or framework names.
- Content may be written in the project language (profile). Keep headings and IDs as they are.
- Do not invent requirements (constitution C3). Unknown → write [NEEDS CLARIFICATION: question].
- Every requirement has an ID (R1, R2…). Every acceptance criterion cites at least one requirement, and every MUST requirement has at least one criterion that would fail if the requirement were removed.
- IDs restart in every spec. When one spec refers to another, prefix the ID with the feature number (001-R5, 002-R5).
- IDs are stable: never renumber or reuse an ID. A removed requirement stays in the table marked "Withdrawn" with a reason.
- Keep the section numbers. A section that does not apply stays with "N/A" and the reason.
- A spec proposed for approval has no [NEEDS CLARIFICATION] marker left.
- Remove all <!-- comments --> when done.
-->

# Spec NNN: <Feature name>

- **Status:** Draft | Clarified | Approved
- **Track:** Full | Light (constitution, Section 1; light track: `fix` playbook)
- **Last updated:** YYYY-MM-DD

## 1. Goal
<!-- 2-3 sentences: what problem this solves, for whom, and why now. -->

## 2. User stories
<!-- One line each. Format: US1. As a <user>, I want <capability> so that <benefit>. -->
- **US1.**

## 3. Requirements
<!-- Testable statements. Use MUST / SHOULD / MAY. One idea per requirement. -->
| ID | Requirement | Story |
|----|-------------|-------|
| R1 | The system MUST … | US1 |

## 4. Acceptance criteria
<!-- Format: Given <context>, when <action>, then <observable result>.
     "Test" column: the automated test that will verify it (or a named manual check and why). Fill during the Plan/Tasks phase. -->
| ID | Criterion | Covers | Test |
|----|-----------|--------|------|
| AC1 | Given …, when …, then … | R1 | |

## 5. Critical flows
<!-- Which user flows are critical and therefore need end-to-end tests (constitution C5)? -->
- 

## 6. UI behavior (only if the feature has an interface)
<!-- Screens or views involved and what the user sees and does. Detail in design.md if needed.
     For each screen state the empty, loading, error and offline behavior (and the active modules' rules, for example web W3). -->
- 

## 7. Security and privacy
<!-- Required for every feature that touches accounts, user data, user input, or sessions. Write "N/A" with a reason otherwise.
     Cover what applies, as requirements (R) where behavior is visible or testable, and as notes here for decisions:
     - Who can see or change what (access rules)
     - Abuse and brute force (limits on repeated attempts)
     - Information leaks (do messages or behavior reveal whether an account or record exists?)
     - Session or token lifetime
     - Input limits (maximum lengths, allowed characters)
     - What is logged, and what must never be logged (constitution C6)
     - How credentials and secrets are stored (never in reversible form) and transmitted (only over encrypted channels)
     - Personal data collected, retention, deletion
     Record explicit decisions and accepted risks here, with the reason. -->
- 

## 8. Out of scope
<!-- Things people might expect but are NOT part of this feature. -->
- 

## 9. Open questions
<!-- Every [NEEDS CLARIFICATION] used above must be listed here. All must be resolved before status = Clarified. -->
- [ ] 

## 10. Edge cases (optional)
<!-- Unusual inputs, limits, concurrency, failure modes.
     Each one MUST map to a requirement or acceptance criterion (C4): write the ID next to it, or add one. -->
- 

## 11. Success measures (optional)
<!-- Only if measurable and relevant: how will we know the feature works for users? -->
- 

## 12. Impact on existing specs (only if this spec extends or changes another)
<!-- List every requirement, criterion, edge case or out-of-scope item of other specs that this spec contradicts or extends (001-R5, 001-AC16…), and the tests that will need updating. Do not edit the other spec here: it is revised separately (Mode B). Write "N/A" if the spec is self-contained. -->
- 

## 13. Approval
- Approved by: 
- Date: 
