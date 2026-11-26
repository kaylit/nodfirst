# Lessons from the origin projects

> Log of the lessons that shaped the rules: first the two proving grounds run before the first release, then real projects after it (newest at the end). "Applied in 0.1" means the rule is part of NodFirst 0.1.0; "applied in 0.2", that it is part of NodFirst 0.2.0. File names follow the layout of that time (`sdd/` for today's `nodfirst/` and `project/`; "Level 2" for today's project profile).

Where an agent misunderstood, improvised, or skipped a gate; which template section was missing or useless; which rule was too vague.
Review after each feature and amend templates, playbooks, or the constitution.

Format: **Date · Feature · What happened · Cause · Change made (file)**

---

## 2026-11-25 · Spec 001 (account) · Security gaps in first draft
- **What happened:** the first draft had no session lifetime, left a user-enumeration difference between registration and login unexamined, deferred repeated-attempt limits to the plan without a requirement, and used a vague requirement (R12) to cover access rules.
- **Cause:** the spec template had no place for security and privacy decisions, and the playbook only asked the agent to flag "relevant" implications.
- **Change:** added "Security and privacy" section to the spec template; added a "look for what is missing" step and an auth/data checklist to the specify playbook.

## 2026-11-25 · Spec 001 (account) · Outdated password rule
- **What happened:** the draft required upper/lower case, digit and special character. Current guidance (NIST SP 800-63B Rev. 4) favors length over composition rules.
- **Cause:** the agent followed a common habit instead of current guidance.
- **Change:** decision taken with the human (min 12 characters, no composition rules, common-password rejection). Idea to evaluate: for security-relevant topics, the playbook could require the agent to cite a current standard.

## 2026-11-25 · Spec 001 (account) · Edge cases not traceable
- **What happened:** edge cases (email normalization, trimming, double submit, unavailable return destination) had no requirement or criterion.
- **Cause:** the template said edge cases "should" map to requirements.
- **Change:** template now says "MUST map"; playbook check added.

## 2026-11-25 · Spec 001 (account) · Language mix and section order
- **What happened:** AC9 mixed English and Italian (an Italian word for "after" inside an English criterion). In the first revision the agent also translated one heading and used a section order different from the template.
- **Cause:** spec content in Italian, template keywords in English; the agent adapted the existing document instead of the updated template.
- **Change:** fixed in the second revision once the change request said to match the template. Watch if it recurs; consider a note on keywords vs prose.

## 2026-11-25 · Spec 001 (account) · Revision mode worked, ambiguity resolved silently
- **What happened:** revision (Mode B) kept IDs stable, marked R12/AC12 as Withdrawn, covered every requirement with a criterion, and applied all decisions. But where the change request was ambiguous ("limit per email and per source"), the agent chose one reading (the pair email+source) without reporting it. That reading is weaker against attacks on many accounts from one source.
- **Cause:** the change request was ambiguous, and the playbook did not ask the agent to report its interpretations.
- **Change:** Mode B now requires a separate "Interpretations" list . Also: write change requests so each limit names its key(s) explicitly.

## 2026-11-25 · Spec 001 (account) · Credential storage and transport missing
- **What happened:** after three revisions, the spec still had no requirement on how passwords are stored or transmitted. The gap surfaced only because the agent's "Interpretations" list noted that it had read "password not in clear" without a named transport rule. The "Interpretations" list  worked: it listed 5 honest readings.
- **Cause:** the security checklist in the playbook and template covered access, limits, leaks, lifetimes, input limits, logs and personal data, but not credential storage and transmission.
- **Change:** added "how credentials and secrets are stored and transmitted" to the checklist  and to the template's security prompts .

## 2026-11-25 · Plan 001 (account) · Handoff list limited to explicit deferrals
- **What happened:** the agent's initial list for the plan contained only items the spec explicitly deferred ("in the plan", written in Italian in that spec) plus constitution decisions D1, D2, D3, D9. It missed the mechanisms the plan must choose anyway (password storage, common-password source, transport, session handling, log content, email normalization, return-path validation). It did notice a real spec inconsistency (R14 fixes numbers but also defers "soglie").
- **Cause:** the playbook told the agent to search for explicit deferrals only.
- **Change:** plan playbook: three groups in the handoff list (explicit, implied mechanisms per requirement, constitution), and spec inconsistencies reported as change requests.
- **Second round:** the corrected list still missed where rate-limit counters live in a stateless host, uniform responses and timing, route protection with session cookie attributes and CSRF, scaffolding, and the constitution's constraints. The plan playbook adds these as examples, a check of each foundational option against requirement IDs, and ordering of decisions by dependency.

## 2026-11-25 · Plan 001 (account) · Review rounds 3-5: findings to feed back into the plan playbook
- **What happened:** the plan went through five rounds. Defects found: (1) "source" key included User-Agent, which the client controls, so rate limits were trivially bypassed; (2) offline logout relied on clearing an HttpOnly cookie from JavaScript, which is impossible; (3) the flag meant to block the session was in client storage, unreadable by the server; (4) C11 missing from the constitution check; (5) plain hashes of IP and email are reversible by brute force, HMAC with a server secret is needed; (6) the session table stored IP and User-Agent, contradicting the "no personal data beyond email" claim; (7) counter increments must be atomic and the window type (fixed or sliding) must be named and implemented as named; (8) a flag cookie needs an explicit Max-Age; (9) in revision mode the agent compacted untouched sections (tables replaced by "..."), losing traceability.
- **Cause:** the playbook had no checklist for client-controlled inputs, cookie capabilities (HttpOnly, readable-by-server), hashing of low-entropy identifiers, or data stored by the auth library by default. Revision mode did not forbid compaction.
- **Change (to apply plan playbook):** add to the plan checklist: client-controlled values never used as security keys; for each client-side mechanism state who can read/write it (JS, server, service worker); low-entropy identifiers hashed with a keyed hash; list fields the chosen library stores by default and justify each; name window type and atomicity for counters; every flag cookie has lifetime; constitution check lists ALL rules. Revision mode: parts not mentioned in the change request stay identical.

## 2026-11-25 · Tasks 001 · First run of the tasks playbook
- **What happened:** first draft had good traceability (every AC covered) but: (1) wrong order, proxy/protected route task came after tasks that needed it; (2) no CI task and no production-migration task; (3) tests depended on features built later (e.g. login-required tests before any login); (4) a backup workflow came before the read-only role it uses; (5) tasks needing human action (accounts, buckets, secrets) were not marked; (6) several tasks too large; (7) no "Depends on" field; (8) HTML entities (&lt;) written in the file.
- **Cause:** the playbook had no dependency check, no list of infrastructure tasks, no size limit, no human-action marking.
- **Change (to apply tasks playbook and template):** add "Depends on" and "Requires human action" fields; check every task's tests against the tasks it depends on (tests may use seeded data until the real flow exists, then repeat with the real flow); check order against dependencies; include CI, production migrations, secrets provisioning; split tasks that mix more than one deliverable; write plain characters, not HTML entities.
- **Also found at review:** a gap in the plan surfaced from the tasks (offline session expiry vs AC16). Tasks must report plan gaps as change requests, not invent mechanisms (the agent did this correctly).

## 2026-11-25 · Implement 001 T2 · Unit test before the test runner
- **What happened:** T2 asks for a unit test that user strings come from the catalog. Vitest is task T3 and is not installed. The agent ran the test with Node’s built-in `node --test` instead of adding Vitest early.
- **Cause:** the task list puts the catalog test on T2 and the runner on T3. The implement playbook says to run the task’s tests; ADR 004 says Vitest is the only unit runner, but installing it in T2 would take T3’s dependency.
- **Change:** none to the templates yet. T3 should move `tests/i18n-catalog.test.mjs` under Vitest. Worth a line in the implement playbook: if a task’s test runner is a later task, say which command to use in the meantime.

## To verify
- Did the agent ask clarifying questions before writing the first draft, as the playbook requires? (Not reported yet.)
- Did the agent show a change list after each revision? Yes for revision 1 (11 items, accurate against the spec). It did not include an "Interpretations" list, as the playbook did not yet ask for one. Check that the revised playbook produces it.

---


## 2026-11-25 · Sandbox 001 (it-due-dates, a deadline-parsing API) · Init left todo lesson files
- **What happened:** `init` treated the repo as a continuation rather than a blank practice bank and left lesson / manual notes from the todo project (`sdd/lessons.md` account entries, `sdd/manual-notes.md`).
- **Cause:** init playbook did not force a clean slate check for “sandbox / proving ground” (the human's words were Italian) vs reuse of an existing SDD tree.
- **Change:** **applied in 0.1** (see playbooks and templates). Rule: **to apply in init playbook:** if the human says sandbox or proving ground (in any language), require empty or reset `lessons.md` / remove project-specific manual notes, or ask before keeping them.

## 2026-11-25 · Sandbox 001 · Level 2 did not check required runtime
- **What happened:** Level 2 assumed Python ≥ 3.12 but the machine had no usable 3.12; work blocked until the human installed it.
- **Cause:** constitution Level 2 / init listed the runtime but did not require verifying it is installed before scaffolding.
- **Change:** **applied in 0.1** (see playbooks and templates). Rule: **to apply in init / Level 2 checklist:** run `python3.12 --version` (or equivalent) and stop with a clear ask if missing.

## 2026-11-25 · Sandbox 001 · First spec missed Unicode and non-str types
- **What happened:** the initial spec did not cover non-ASCII digits, whitespace/`isspace`, NFC/NFD, `None`, or `datetime` as `reference_date`; gaps were found by the human's review and by Mode B, not by the agent (clarify was not run).
- **Cause:** specify checklist under-weighted input encoding and caller-type boundaries for a pure parsing library.
- **Change:** **applied in 0.1** (see playbooks and templates). Rule: **to apply in specify playbook:** for text-parsing APIs, prompt for Unicode normalization, digit repertoire, whitespace, and non-`str` / non-calendar inputs.

## 2026-11-25 · Sandbox 001 · Requirement cited without a proving AC (R11/NFC)
- **What happened:** R11 (NFC) was stated but for a while no AC forced an NFD→NFC proof; AC10 was later extended.
- **Cause:** analyze/specify did not enforce “every MUST in R* has an AC that would fail without it.”
- **Change:** closed in Mode B via AC10 (NFD). **To apply in analyze:** High if a requirement has no AC that would fail without it (Critical only when the behaviour is unspecified or untested).

## 2026-11-25 · Sandbox 001 · Contradictory criteria (AC3 N=1 vs AC16)
- **What happened:** AC3 allowed plural N=1 while AC16 (and singular rule) rejected the phrase "in 1 days" (in Italian); implementers would have had conflicting greens.
- **Cause:** revision of singular/plural rules updated some AC/R rows but left an inconsistent AC3.
- **Change:** fixed in Mode B (AC3 plural N=2 and 365 only). **To apply in specify Mode B:** after grammar changes, re-read every AC that mentions the same token (N, singular/plural).

## 2026-11-25 · Sandbox 001 · Spec revision did not realign plan §8
- **What happened:** after Mode B on the spec, plan §8 still had stale AC3/AC10/AC16 wording; analysis flagged it; later plan was updated.
- **Cause:** Mode B on spec did not require a paired pass on plan test strategy.
- **Change:** plan §8 eventually aligned. **To apply in specify/plan Mode B:** if AC text changes, update plan §8 in the same change request or open an explicit CR.

## 2026-11-25 · Sandbox 001 · Agent invented an undecided license
- **What happened:** the agent added MIT (or similar) to clear a packaging warning although license was not decided.
- **Cause:** tooling warning treated as a requirement; C3 violated.
- **Change:** license removed before continuing implement. **To apply in implement playbook:** never add license/metadata not in plan/spec; leave warning or ask.

## 2026-11-25 · Sandbox 001 · `reason` proposed in Italian
- **What happened:** a draft used Italian identifiers for `reason` against the rule that fixed identifiers are English (messages Italian).
- **Cause:** bilingual product (IT messages / EN ids) not checked when naming enums.
- **Change:** corrected to English `ParseReason` values. **To apply in plan/specify:** explicit reminder — machine identifiers English; user-facing strings may be Italian.

## 2026-11-26 · Sandbox 002 · Spec that extends another spec
- **What happened:** 002 added expressions, but 001 said "only these" in R5 and listed "the day after tomorrow" and "in 3 weeks" (in Italian) as not recognized in AC16 and Out of scope; without revising 001 its tests would have failed.
- **Cause:** the template has no section for impact on existing specs, and IDs (R5, AC16) repeat in every spec.
- **Change:** **applied in 0.1** (see playbooks and templates). Rule: **to apply:** add an "Impact on existing specs" section to the spec template; in cross-references use the feature prefix (001-R5, 002-R5); when the spec extends an existing contract, the specify playbook must list which parts of the previous spec to revise.

## 2026-11-26 · Sandbox 002 · Constitution check C2 row with plan status
- **What happened:** plan 002 wrote "Plan in Draft; human approval follows" in the C2 row, which becomes false on approval, despite plan playbook rule.
- **Cause:** the rule lived only in the playbook, not in the template.
- **Change:** **applied in 0.1** (see playbooks and templates). Rule: **to apply:** fixed text in the C2 row of the plan template ("Gate respected: no later step before human approval").

## 2026-11-26 · Sandbox 002 · Step order that breaks the gate
- **What happened:** the plan put week recognition before updating 001 tests that treated "in 3 weeks" (in Italian) as not recognized; the gate would have gone red mid-feature.
- **Cause:** the plan playbook does not require ordering steps so each step leaves the gate green when a feature changes already-tested behaviour.
- **Change:** **applied in 0.1** (see playbooks and templates). Rule: **to apply in plan and tasks playbooks:** if the feature changes behaviour already covered by tests, the step that updates those tests comes first and must stay green before and after.

## 2026-11-26 · Sandbox 002 · Task too large
- **What happened:** the first tasks draft for 002 had a single task for both "the day after tomorrow" and weeks (~35 tests, two families with different rules), against the "one deliverable per task" rule.
- **Cause:** the rule exists in the tasks playbook but the agent does not apply it when families look similar.
- **Change:** **applied in 0.1** (see playbooks and templates). Rule: **to apply in tasks playbook:** explicit example ("two forms with different regexes and limits are two tasks").

## 2026-11-26 · Sandbox 002 · Analyze vs plan "Planned steps"
- **What happened:** analyze flagged as a Medium defect that the plan section "Planned steps (they become tasks)", written in Italian, did not match the task split.
- **Cause:** that section is by definition indicative.
- **Change:** **applied in 0.1** (see playbooks and templates). Rule: **to apply in analyze playbook:** exclude the plan "Planned steps" section from line-by-line comparison.

## 2026-11-26 · Sandbox 002 · Incomplete final verification
- **What happened:** the last-task report had the criteria→test table and the TBD search, but not the single command from a clean environment nor the list of misplaced files.
- **Cause:** the last-task rule implement playbook is one bullet among eight.
- **Change:** **applied in 0.1** (see playbooks and templates). Rule: **to apply in implement playbook:** final verification becomes a titled section with a checklist, and the report is incomplete without it.

## 2026-11-26 · Sandbox 002 · README: inconsistent wording
- **What happened:** in the failures table the days row said "plural N days outside 1–365" and the weeks row "N = 0 or > 52" (both in Italian).
- **Cause:** two rows written at different times.
- **Change:** **applied in 0.1** (see playbooks and templates). Rule: **to apply in playbook:** for parallel table rows, use the same wording (the more precise one).

## 2026-11-26 · Sandbox 002 · What worked (keep)
- **What happened:** a one-line prompt with "Context to read" let Cursor find constitution, spec, plan and tasks on its own. A clarifying question on singular vs plural before writing the spec helped. The implement report format was followed (Before, tests, files, gates, deviations).
- **Cause:** short prompts plus explicit "Context to read" and the report template reduce missed context and incomplete reports.
- **Change:** none — keep these practices. **To apply:** retain one-line prompts that name the playbook; keep the clarifying question on agreement before specify; keep the implement report form.

## 2026-11-26 · Shortz, feature 001 (first real project on 0.1.0) · No way to close a feature with accepted findings
- **What happened:** `verify` run 3 gave `not verified` with 14 findings. The human chose to ship and close the feature, accepting all of them. The kit had no such outcome: the agent invented a `Last closed` line in the profile and a "Closed" mark in the roadmap, and `next` would still have answered "run `verify`". See `examples/shortz/`.
- **Cause:** `verify`, `next`, `implement` and the manual knew only two outcomes: `verified` (finished) or fix and verify again. Closing knowingly is a human decision the kit did not name.
- **Change:** **applied in 0.2**: `verify` has a "Closing the feature" step (the human names every Critical or High finding left, with a reason and a follow-up; the agent records a Closure section, profile Section 0 and the roadmap line; the verdict never changes); `next` and `implement` treat a recorded Closure as finished; manual 7.8 and Appendix B explain it.

## 2026-11-26 · Shortz, feature 001 · Checks only a person can do blocked the verdict
- **What happened:** "no GitHub Actions run observed" and "production smoke not repeated by this run" were written as High findings (F9, F10). With them, `verified` and even `partly verified` were out of reach whatever the code did, although the same report had a "Needs a human" list for such checks.
- **Cause:** `verify` said both "a check that cannot run is a finding" and "`partly verified`: some checks could not run", and "untested" (High) did not say whether it meant the code or the environment.
- **Change:** **applied in 0.2**: a check that could not be done from here goes to Needs a human (checkbox, result recorded when the human reports it), never as a finding or a pass; "untested" means no test in the code; the three verdicts have exact rules; closing also needs every open human check done or accepted.

## 2026-11-26 · Shortz, feature 001 · The verdict changed between runs
- **What happened:** run 2 said `partly verified` (10 findings); run 3, on almost the same code, said `not verified` (14 findings, 2 Critical), partly by reading the severity scale more literally.
- **Cause:** no rule on how a re-run treats the previous findings, and an ambiguous verdict rule (above).
- **Change:** **applied in 0.2**: a re-run lists every previous finding as closed, still open or reclassified, with a reason for any change of severity, and must not reclassify only to change the verdict. Watch on the next real project whether this is enough.

## 2026-11-26 · Shortz, feature 001 · No lessons were recorded
- **What happened:** a whole feature with three verification runs, a change request and a task revision left `project/lessons.md` empty. The lessons of this run were reconstructed afterwards by the maintainer, from the files and the commits.
- **Cause:** the profile said "not a proving ground", and the lessons log was described only as part of a proving ground's feedback loop; the manual left writing entries to the human.
- **Change:** **applied in 0.2**: in every project the agent proposes a lessons entry when the human corrects it or a document (`AGENTS.md`), and up to three when a feature is closed (`verify`, "Closing the feature"); it writes only the entries the human accepts. The profile skeleton (Section 9) is unchanged.

## 2026-11-26 · Shortz, update to 0.2.0 · `init update` had to ask for the release notes
- **What happened:** after the human replaced `nodfirst/`, `/nodfirst-init update` asked for NodFirst's release notes; they live in the NodFirst repository, not in the project, so the human had to paste them.
- **Cause:** nothing that ships with the kit says what changed between versions.
- **Change:** **applied in 0.2.1**: `nodfirst/CHANGES.md` ships with the kit (files to replace, profile changes, effect on work in progress, per version); `init update` reads it; the release steps in `maintainers/README.md` include it.

## 2026-11-26 · Shortz, fix 002 (first light fix) · How a light fix finishes was not written
- **What happened:** a security-relevant fix (verification finding F14 of feature 001). After the implementation report the agent set `Active feature: none` and a `Last closed` line on its own; the recommended `verify` then had to guess which feature to check, and the closing step asked for a roadmap line that light fixes do not have. The agent of the closing step proposed this lesson itself.
- **Cause:** `fix` ended with "commit when the human accepts"; `next` said an implemented light fix is finished; `verify` 0.2 said a feature is finished only when the human closes it, and its preconditions assumed `tasks.md`.
- **Change:** **applied in 0.2.1**: `fix` says when a fix is finished (accepted report; or, if security-relevant, closed after `verify`, staying the active feature until then) and that light fixes have no roadmap line; `verify` has a light-fix precondition (light spec, the specs it changes, the commits of the fix) and records profile and roadmap only where they name the feature; `next` follows the same states; manual Part 8 explains it.

## 2026-11-26 · Shortz, fix 002 · What worked (keep)
- **What happened:** `fix` checked that the change was light, told a change from a bug, named its source of truth (a plan decision, not the spec), reported its interpretation, wrote failing tests first, and recommended `verify` for a security area. The human added two boundary criteria (case, empty header) before approval; both became tests. At closure, the agent proposed a lesson instead of writing it.
- **Cause:** the light-track checks, the boundary-input checklist of `specify` and the 0.2 lessons rule.
- **Change:** none: keep them.

## 2026-11-26 · Shortz, fix 002 · A test browser installed without asking
- **What happened:** to run the end-to-end gate, the agent installed the Playwright browser into the local cache, then reported it as a deviation. The constitution said to stop when a tool is missing.
- **Cause:** the rule did not separate a new tool from a component that an approved, pinned dependency downloads itself.
- **Change:** **applied in [Unreleased]**: constitution Section 4 allows that one case (own install command, project or user cache, no account, licence, payment or administrator rights), always reported; everything else still stops the work. Decided with the author.

## 2026-11-26 · Shortz · `next dev` writes into `AGENTS.md`
- **What happened:** Next.js appended its own block to `AGENTS.md` during feature 001; replacing `AGENTS.md` for the 0.2.0 update removed it, and `next dev` added it back as an uncommitted change during fix 002.
- **Cause:** `AGENTS.md` is a kit file that other tools also write to, and the update instructions said to replace it whole.
- **Change:** **applied in [Unreleased]**: `init update` replaces `AGENTS.md` and `CLAUDE.md` only when `nodfirst/CHANGES.md` says so, and keeps blocks other tools added. Decided with the author.
