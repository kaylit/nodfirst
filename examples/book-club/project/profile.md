# Project profile

> Owned by this project. Written by `init` (new project) or `adopt` (existing code). Kit updates never replace this file.
> Status: Approved · Approved by: Human (simulated) · Date: 2026-11-26
> Written with NodFirst kit version: 0.1.0

## 0. Current state
- **Active feature:** `specs/001-book-lending/`
- **Working profile:** Guided
- **Git:** used

## 1. Product summary
A small web app for a neighbourhood book club (about 10-40 members). Members record which books they are reading and lend physical books to each other. The interface and documentation for users are in English.
- **Modules:** web, backend (`nodfirst/modules/`)
- **Modules not fully proven, accepted by the human:** web (partly proven; W7-W11 unproven), backend (not yet proven); confirmed 2026-11-26
- **Proving ground for the kit:** no

## 2. Way of working
- **Who approves:** the human (club organiser)
- **Language of conversation:** English
- **Git checkpoints:** the agent commits after each approval
- **Branches and review (Team):** N/A – Guided profile

## 3. v1 scope
**In scope**
- Members sign in; each member keeps a list of books they are reading.
- Members mark books they own as available to lend; others request them; the owner accepts or declines.

**Out of scope for v1**
- Payments, public sign-up from outside the club, chat, ratings and reviews, mobile apps.

## 4. Technical profile
| Area | Decision |
|---|---|
| Language / runtime (with minimum version) | DECIDE (D1) |
| Framework / main libraries | DECIDE (D1) |
| Data storage | DECIDE (D2) |
| Hosting / distribution | DECIDE (D3) |
| Language of messages and documentation vs identifiers | User-facing text and identifiers in English (C12) |

## 5. Commands
- **Set-up:** TBD
- **Single quality command (runs every gate below):** TBD
- **Other:** TBD

## 6. Quality gates (a task is done only if all pass)
1. Lint passes with no errors.
2. Type check passes.
3. Unit and integration tests pass.
4. End-to-end tests of the current spec's critical flows pass.
5. Production build succeeds.
6. Automated accessibility check (WCAG 2.2 AA, C7) reports no violation on new screens; manual keyboard check for new UI.
7. Dependency audit reports no known high-severity issue.

## 7. Design system rules (only if there is a UI)
- Follow web module W2-W4. Tokens and components in `project/design-system.md` (not yet created).

## 8. Data, privacy and security specifics
- GDPR applies (members live in the EU). Personal data: name, email, book lists, loans. Data minimisation (C6, W5). No analytics in v1.
- Members see only club members' data; nothing is public.

## 9. Feedback loop (only if the project is a proving ground)
N/A – not a proving ground.

## 10. Exceptions to the constitution
- None.

## 11. Open decisions
| # | Decision | When | Candidates / criteria |
|---|---|---|---|
| D1 | Language and framework | Plan of the first feature | simple to host, well maintained, one language front and back |
| D2 | Data storage | Plan of the first feature | small data, backups easy, EU location |
| D3 | Hosting | Plan of the first feature | low or no cost, EU region |
| D4 | How members sign in | Spec of the first feature (sign-in) | email link vs password |
