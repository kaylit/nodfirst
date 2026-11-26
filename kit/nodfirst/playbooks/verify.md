# Playbook: Verify

**Version:** 0.1 (not yet proven)
**Purpose:** an independent check that the finished code does what the approved spec says, nothing more and nothing less, and respects the plan and the constitution (C14). It complements `analyze`, which checks the documents before the code exists.
**Prompt:** `/nodfirst-verify` (or mention `nodfirst/playbooks/verify.md`), **in a new chat**, ideally with another model or another agent than the one that implemented the feature.
**Output:** `specs/NNN-feature-name/verification.md` (the only file you may create or overwrite). Nothing else changes.

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `project/profile.md`, the modules it lists (`nodfirst/modules/`), and for the active feature `spec.md`, `design.md` if any, `plan.md`, `tasks.md`, `analysis.md`; then the code and tests the tasks name, and the rest of the code base as needed.

## Preconditions
- All tasks of the feature are `[x]`. If not, say which are open and ask whether to verify what exists (a partial verification says so in its header).
- **Independence:** if this chat also wrote code for the feature, say so and recommend a new chat; continue only if the human insists, and write it in the header.

## Instructions for the agent

You are an inspector, not a builder. Follow `nodfirst/constitution.md`, especially C1, C3, C4, C5, C6 and C14. Do not trust the implement reports: check the code and run the commands yourself.

1. **Run the single quality command** (profile, Section 5) from a fresh environment if the profile allows it, otherwise as is. Record the command, the result and the number of tests. If it cannot run (a missing tool, a secret, a device), say so: that is a finding, not a pass.
2. **Requirement by requirement.** For every active requirement and acceptance criterion of the spec, find the code that implements it and the test that proves it. Classify each:
   - **met:** implemented, and a test fails if the behaviour is removed (read the test; a test that cannot fail does not count);
   - **partial:** some cases or criteria missing;
   - **missing:** not implemented;
   - **contradicts:** implemented differently from the spec;
   - **untested:** implemented but no test proves it.
3. **Look for what nobody asked for (C1, C3):** behaviour, screens, endpoints, settings, dependencies, licences or metadata that no spec, plan or task names. Each is a finding of kind **unrequested**.
4. **Plan and constitution:** decisions of the plan respected (data model, interfaces, dependencies with their pinned versions); constitution rules C1-C14 and the exceptions in the profile.
5. **Security and privacy review** (C6) of the feature's code, using the spec's "Security and privacy" section, the plan's security table and the active modules' checklists (for web: OWASP Top 10; for a backend: OWASP API Security Top 10). At least: input validation at the boundary, access checks on the trusted side for every protected operation, secrets in code or config, personal data in logs or messages, messages that echo input, dependencies with known high-severity vulnerabilities if an audit tool exists. Write what you checked and what you could not check.
6. **Accessibility** (C7, if there is a UI): what automated checks report, and what needs a person (keyboard and screen reader pass) — the latter goes to "Needs a human".
7. **Severity** of each finding, as in `analyze`: **Critical** (missing or contradicting behaviour, a security hole, a constitution violation), **High** (partial, untested, unrequested behaviour), **Medium** (stale text, weak test), **Low** (cosmetic).
8. **Write `verification.md`:**
   - Header: feature, date, run number, who verified (model or agent, and "independent: yes/no"), quality command and result.
   - **Summary** (at most five lines) and the verdict: `verified` (no Critical or High), `partly verified` (some checks could not run), or `not verified`.
   - Table: requirement / criterion → status → code → test.
   - Findings: ID, severity, kind, where, what is wrong, the smallest fix and where it belongs (a new task, a spec change request, a plan revision).
   - **Needs a human:** checks only a person can do (real device, store console, manual screen-reader pass), each as one line the human can follow.
9. **Stop.** Show the summary and the verdict. In the Guided profile, explain the verdict in everyday words. Do not fix anything: fixes become tasks appended to `tasks.md` by the `tasks` playbook (revision), or change requests, and then `verify` runs again.

## Do not
- Edit any file other than `verification.md`, fix code, mark tasks, or approve anything.
- Count a check that did not run as passed.
