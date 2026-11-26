<!--
PLAN TEMPLATE v0.1 — copy to specs/NNN-feature-name/plan.md
Rules:
- The plan answers HOW. It may only start from a spec with status Approved.
- Never contradict the spec. If the plan needs a different behavior, stop and change the spec first (C1).
- Every significant technical choice is a decision (C10): context, options, decision, consequences.
- Every new dependency needs a justification (C8).
- Remove all <!-- comments -->. A section that does not apply keeps its heading and one line: `N/A – reason` (C13).
-->

# Plan NNN: <Feature name>

- **Spec:** `specs/NNN-feature-name/spec.md`
- **Status:** Draft | Approved
- **Last updated:** YYYY-MM-DD

## 1. Summary
<!-- 3-5 sentences: the approach in plain words. -->

## 2. Constitution check
<!-- Every rule, C1-C14, with how the plan complies or why an exception is justified. Never write the approval status of the plan in this table: it goes stale. Keep the C2 row text as it is. -->
| Rule | Compliance / note |
|------|-------------------|
| C1 Spec is source of truth | |
| C2 Human approval gates | Gate respected: no later step before human approval |
| C3 Do not invent requirements | |
| C4 Traceability | |
| C5 Tests | see Section 8 |
| C6 Security & privacy | see Section 7 |
| C7 Accessibility | |
| C8 Simplicity / dependencies | see Section 10 |
| C9 Small verifiable increments | |
| C10 Architectural decisions | see Section 4 |
| C11 Specs stay alive | |
| C12 Language | |
| C13 Brevity | |
| C14 Independent verification | `verify` after the last task |

## 3. Technical context
<!-- Only what is specific to this feature. Stack comes from the profile; do not repeat it. -->
- **Touched areas:** 
- **Existing code/modules reused:** 
- **Constraints:** 

## 4. Decisions
<!-- One entry per decision. Link to open decisions in the profile (D1…). -->
### Decision: <title>
- **Context:** 
- **Options:** A) … B) …
- **Decision:** 
- **Consequences:** 

## 5. Data model
<!-- Entities, fields, relations, ownership (who owns each record), constraints, migrations. -->
- 

## 6. Interfaces and contracts
<!-- Endpoints/actions/events: inputs, outputs, errors, who may call them. Each cites requirement IDs. -->
| Interface | Purpose | Input → Output / errors | Auth | Covers |
|-----------|---------|--------------------------|------|--------|
| | | | | R1 |

## 7. Security and privacy
<!-- Threats and mitigations for this feature: authentication, authorization, input validation,
     data exposure, rate limiting, logging of personal data, data retention/deletion. Use the threat checklist named by each active module (for web: OWASP Top 10). -->
- 

## 8. Test strategy
<!-- Map every acceptance criterion to a test level (C4, C5). -->
| AC | Level (unit / integration / e2e / manual) | Test description |
|----|-------------------------------------------|------------------|
| AC1 | | |

## 9. UI and UX (if applicable)
<!-- Components, routes/screens, state handling (empty, loading, error, offline), i18n keys, accessibility.
     Reference design.md and project/design-system.md; do not duplicate them. -->
- 

## 10. Dependencies
<!-- New libraries or services. Justify each: what it replaces, maintenance status, size/risk, alternative considered. -->
| Dependency | Why | Alternatives considered |
|------------|-----|-------------------------|
| | | |

## 11. Risks and mitigations
| Risk | Likelihood / impact | Mitigation |
|------|---------------------|------------|
| | | |

## 12. Rollout and migration (if applicable)
<!-- Data migrations, feature flags, backward compatibility, rollback. -->
- 

## 13. Open questions
- [ ] 

## 14. Approval
- Approved by: 
- Date: 
