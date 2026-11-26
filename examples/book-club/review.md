# Review of spec 001 (book lending), draft 1

What a careful reader finds before approving. Severity as in `analyze`: **High** = something would be built wrong or not tested; **Medium** = unclear or inconsistent; **Low** = wording.

## Findings

1. **High – a rule exists only as an edge case, and the agent decided it alone.**
   Section 10 says that when the owner accepts one request, the other requests for the same book "are declined automatically", marked "[NEEDS CLARIFICATION → resolved as assumption]".
   - A spec proposed for approval may not contain a `[NEEDS CLARIFICATION]` marker (template rules).
   - It is a product decision taken by the agent (C3): the club might prefer that other requests stay waiting for when the book comes back.
   - It is a rule with no requirement and no criterion, so nothing would test it (C4).
   **Ask:** decide what happens to the other requests, then make it a requirement (R7) with a criterion.

2. **High – who can see a request is not said.**
   Section 7 says only signed-in members see books and requests. It does not say whether every member sees every request, or only the owner and the person who asked. For a small club this is a privacy choice (who is borrowing what).
   **Ask:** "A request MUST be visible only to the owner of the book and to the member who made it" (or the opposite, if the club wants it public), with a criterion.

3. **Medium – what happens when the owner makes a book unavailable while a request is waiting?**
   R1 lets the owner switch availability at any time; R5 covers accept and decline. Nothing covers switching off with a pending request.
   **Ask:** pending requests are declined, or stay waiting; with a criterion.

4. **Medium – what the member sees is missing in three criteria.**
   AC4 gives the exact message ("This book is not available"); AC2, AC5 and AC8 only say "refused" or "no second request". A Guided user cannot check a screen against "refused".
   **Ask:** an exact message for each, like AC4.

5. **Medium – AC5 has no action.**
   "Given Anna requests her own book, then the request is refused" mixes context and action. Every criterion is *Given … when … then …*.
   **Fix:** "Given Anna owns a book that is available, when she tries to request it, then … (message) and no request is created."

6. **Medium – an assumption hidden in the UI section.**
   Section 6 says "Offline: N/A – offline not required in v1 (assumption)". An assumption the human never confirmed is a decision taken on their behalf (C3). It may well be right for a club that meets at home, but it belongs in the agent's report, where the human sees it, not inside a sentence.
   **Ask:** confirm it explicitly ("offline is out of scope for v1") and move it to Out of scope.

7. **Low – how a lent book becomes available again is implicit.**
   Returns are out of scope, so the only way back is the owner switching availability on again (R1). That is a reasonable reading, but it should be written, so nobody builds a "return" button.
   **Ask:** one sentence in Out of scope: "When the book is back, the owner marks it available again (R1)."

8. **Low – "nothing logged beyond member ID" is vague.**
   Which events are logged (requests, accept, decline)? Is the book title logged?
   **Ask:** name the events and say that names and book titles are not logged, or decide it in the plan and say so here.

## The change request to send

```
/nodfirst-specify Mode B on 001:
1. Section 6: offline is out of scope for v1. Move it to Out of scope and remove "(assumption)".
2. Section 10: when the owner accepts a request, the other pending requests for the same book stay waiting [or: are declined, with the message "…"]. Make it R7 with a criterion; remove the marker.
3. Add a requirement: a request is visible only to the owner of the book and to the member who asked. Add a criterion.
4. Add a requirement for an owner who marks a book not available while requests are waiting: they are declined with the message "This book is no longer available". Add a criterion.
5. AC2, AC5, AC8: give the exact message the member sees, as in AC4.
6. AC5: rewrite as Given / when / then.
7. Out of scope: add "When the book is back, the owner marks it available again (R1)."
8. Section 7: logged events are request, accept and decline, with member IDs and book ID only; never names or titles.
```

After the agent answers, read its three lists (**Changes**, **Interpretations**, **Downstream impact**), check the spec again, and only then approve.
