# Playbook: Verify

**Version:** 0.2 (used on one project, three runs; closing step, Needs-a-human checks and re-run rule new in 0.2, not yet proven)
**Purpose:** an independent check that the finished code does what the approved spec says, nothing more and nothing less, and respects the plan and the constitution (C14). It complements `analyze`, which checks the documents before the code exists.
**Prompt:** `/nodfirst-verify` (or mention `nodfirst/playbooks/verify.md`), **in a new chat**, ideally with another model or another agent than the one that implemented the feature. To close the feature afterwards: `/nodfirst-verify close` followed by the findings you accept, each with a reason (any chat).
**Output:** `specs/NNN-feature-name/verification.md` (the only file you may create or overwrite). Nothing else changes, except the lines named in "Closing the feature" when the human closes it.

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `project/profile.md`, the modules it lists (`nodfirst/modules/`), and for the active feature `spec.md`, `design.md` if any, `plan.md`, `tasks.md`, `analysis.md`; then the code and tests the tasks name, and the rest of the code base as needed.

## Preconditions
- All tasks of the feature are `[x]`. If not, say which are open and ask whether to verify what exists (a partial verification says so in its header).
- **Independence:** if this chat also wrote code for the feature, say so and recommend a new chat; continue only if the human insists, and write it in the header.

## Instructions for the agent

You are an inspector, not a builder. Follow `nodfirst/constitution.md`, especially C1, C3, C4, C5, C6 and C14. Do not trust the implement reports: check the code and run the commands yourself.

0. **Closing.** If the human asks to close the feature (`close` …), skip the checks and go to "Closing the feature" below.
1. **Run the single quality command** (profile, Section 5) from a fresh environment if the profile allows it, otherwise as is. Record the command, the result and the number of tests. If it cannot run (a missing tool, a secret, a device), say so and why: it goes to **Needs a human** (step 8), and it is never a pass.
2. **Requirement by requirement.** For every active requirement and acceptance criterion of the spec, find the code that implements it and the test that proves it. Classify each:
   - **met:** implemented, and a test fails if the behaviour is removed (read the test; a test that cannot fail does not count);
   - **partial:** some cases or criteria missing;
   - **missing:** not implemented;
   - **contradicts:** implemented differently from the spec;
   - **untested:** implemented but no test in the code proves it.
   A check that **could not be done from here** (a real device, a store or CI console, the production site, a person with a keyboard or a screen reader) is not a finding about the code: write it under **Needs a human**, never as passed and never as a finding.
3. **Look for what nobody asked for (C1, C3):** behaviour, screens, endpoints, settings, dependencies, licences or metadata that no spec, plan or task names. Each is a finding of kind **unrequested**.
4. **Plan and constitution:** decisions of the plan respected (data model, interfaces, dependencies with their pinned versions); constitution rules C1-C14 and the exceptions in the profile.
5. **Security and privacy review** (C6) of the feature's code, using the spec's "Security and privacy" section, the plan's security table and the active modules' checklists (for web: OWASP Top 10; for a backend: OWASP API Security Top 10). At least: input validation at the boundary, access checks on the trusted side for every protected operation, secrets in code or config, personal data in logs or messages, messages that echo input, dependencies with known high-severity vulnerabilities if an audit tool exists. Write what you checked and what you could not check.
6. **Accessibility** (C7, if there is a UI): what automated checks report, and what needs a person (keyboard and screen reader pass) — the latter goes to "Needs a human".
7. **Severity** of each finding, as in `analyze`: **Critical** (missing or contradicting behaviour, a security hole, a constitution violation), **High** (partial, untested, unrequested behaviour), **Medium** (stale text, weak test), **Low** (cosmetic).
   **On a re-run,** list every finding of the previous run as *closed*, *still open* or *reclassified*; a change of severity or kind needs a reason (new evidence, or the previous run misapplied this scale). Do not reclassify only to change the verdict.
8. **Write `verification.md`:**
   - Header: feature, date, run number, who verified (model or agent, and "independent: yes/no"), quality command and result.
   - **Summary** (at most five lines) and the verdict, by these rules only:
     - `not verified`: at least one Critical or High finding;
     - `partly verified`: no Critical or High finding, and some items under Needs a human are still open;
     - `verified`: no Critical or High finding, and nothing under Needs a human is open.
   - Table: requirement / criterion → status → code → test.
   - Findings: ID, severity, kind, where, what is wrong, the smallest fix and where it belongs (a new task, a spec change request, a plan revision).
   - **Needs a human:** checks that could not be done from here, each as a checkbox line the human can follow (what to do, where, what counts as a pass). When the human reports a result, record it on the line (result, who, date, as given); a failed check becomes a finding of the next run.
   - On a re-run: the previous findings with their new state (step 7).
9. **Stop.** Show the summary and the verdict. In the Guided profile, explain the verdict in everyday words. Do not fix anything: fixes become tasks appended to `tasks.md` by the `tasks` playbook (revision), or change requests, and then `verify` runs again; or the human closes the feature with the findings accepted (below).

## Closing the feature (only when the human decides)
After the verification, the human decides; you never do (C2). Either **fix** (the findings become tasks or change requests, then `verify` runs again) or **close**. Even a `verified` feature is finished only when the human closes it. The human closes with `/nodfirst-verify close …` or in words (for example "close feature 001, accept F3 and F7"). Closing does not need a new chat: it records a decision and checks nothing. Then:
1. **Every Critical or High finding left, and every open item under Needs a human, is named by the human as accepted** (or, for a Needs-a-human item, reported as done), each with a reason and a follow-up (a roadmap item, a later feature, or "none"). Ask for whatever is missing. Anything the human does not name stays open, and the feature is not closed. Before recording an accepted Critical or security finding, say in one sentence what it means for the people who use the product (Guided profile: in everyday words).
2. **Record the decision,** changing nothing else:
   - `verification.md`: a final section **Closure** with closed by, date (as the human gives them), the verdict at closure (unchanged), and a table finding or check → reason → follow-up (for a feature with nothing left: "Nothing left open");
   - `project/profile.md`, Section 0: `Active feature: none`;
   - `project/roadmap.md`: at the end of the feature's line, `– closed <date> (verified)` or `– closed <date> (findings accepted: F…)`; each follow-up the human wants on the roadmap, as a new feature line.
3. **Git checkpoints:** commit those files with the message `feature NNN closed`.

The verdict is never changed to make a closure possible: a feature closed with accepted findings stays `partly verified` or `not verified`, and says so.

## Do not
- Edit any file other than `verification.md` (and, at closure, the lines named above), fix code, mark tasks, or approve or close anything on your own.
- Count a check that did not run as passed.
