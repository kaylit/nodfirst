# Spec 001: Book lending

- **Status:** Draft
- **Track:** Full
- **Last updated:** 2026-11-26

## 1. Goal
Club members can show which of their books are available to lend, and ask another member to lend them a book.

## 2. User stories
- **US1.** As a member, I want to mark one of my books as available to lend, so that others know they can ask for it.
- **US2.** As a member, I want to request an available book from another member.
- **US3.** As an owner, I want to accept or decline a request.

## 3. Requirements
| ID | Requirement | Story |
|----|-------------|-------|
| R1 | A member MUST be able to mark one of their own books as available or not available. | US1 |
| R2 | A member MUST NOT be able to change the availability of another member's book. | US1 |
| R3 | A member MUST be able to request an available book owned by another member. | US2 |
| R4 | A member MUST NOT be able to request their own book or a book that is not available. | US2 |
| R5 | The owner MUST be able to accept or decline a pending request; accepting makes the book not available. | US3 |
| R6 | A member MUST NOT have more than one pending request for the same book. | US2 |

## 4. Acceptance criteria
| ID | Criterion | Covers | Test |
|----|-----------|--------|------|
| AC1 | Given Anna owns "The Name of the Rose" (not available), when she marks it available, then other members see it as available. | R1 | |
| AC2 | Given Bruno is signed in, when he tries to change the availability of Anna's book, then the change is refused and nothing changes. | R2 | |
| AC3 | Given Anna's book is available, when Bruno requests it, then Anna sees a pending request from Bruno. | R3 | |
| AC4 | Given Anna's book is not available, when Bruno requests it, then the request is refused with the message "This book is not available". | R4 | |
| AC5 | Given Anna requests her own book, then the request is refused. | R4 | |
| AC6 | Given a pending request, when Anna accepts, then the book becomes not available and Bruno sees "Request accepted". | R5 | |
| AC7 | Given a pending request, when Anna declines, then the book stays available and Bruno sees "Request declined". | R5 | |
| AC8 | Given Bruno has a pending request for a book, when he requests it again, then no second request is created. | R6 | |

## 5. Critical flows
- Request and accept a book (AC3, AC6): the core of the feature.

## 6. UI behavior (only if the feature has an interface)
- "My books" with an availability switch; "Available books" list with a "Request to borrow" button; "Requests" for the owner. Empty state: "No books available". Error: message, no data lost. Offline: N/A – offline not required in v1 (assumption).

## 7. Security and privacy
- Only signed-in members (sign-in: roadmap item 1, not yet specified) see books and requests. Access rules R2, R4. Personal data: member name shown next to a book. Nothing logged beyond member ID.

## 8. Out of scope
- Return of the book, due dates, reminders, notifications by email, waiting lists.

## 9. Open questions
- (none)

## 10. Edge cases (optional)
- Two members request the same book at the same time and the owner accepts one: the other request is declined automatically [NEEDS CLARIFICATION → resolved as assumption: R5 only allows accepting while available].

## 11. Success measures (optional)
N/A – small club app.

## 12. Impact on existing specs (only if this spec extends or changes another)
N/A – first spec. Depends on sign-in (roadmap item 1), not yet specified.

## 13. Approval
- Approved by: 
- Date: 
