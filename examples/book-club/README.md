# Example: a book club web app

> **Illustrative, not a real project.** These files were produced in a dry run of NodFirst 0.1.0 before release: an agent followed `init` and `specify` literally, with a simulated non-technical human who answered "your suggestion" to almost every question. Nothing was built.

## The project
A small web app where a neighbourhood book club tracks what members are reading and lends books to each other. Working profile: **Guided**.

## Files (as the agent drafted them)
- [`project/profile.md`](project/profile.md): the project profile written by `init` and approved.
- [`project/roadmap.md`](project/roadmap.md): the feature backlog.
- [`specs/001-book-lending/spec.md`](specs/001-book-lending/spec.md): the first spec, status *Draft*, as proposed for approval.
- [`review.md`](review.md): what a careful reader should catch in that draft, and the change request to send.

## How to use this example
1. Read the spec as if you had to approve it. Use the checklist in the manual (Part 7.1, "How to check it").
2. Write down every problem you find.
3. Then read `review.md` and compare.

The draft is a good first draft: it has clear stories, requirements with IDs, criteria with real names and messages, and it noticed that sign-in must come first. It still has eight problems that would cost time later. Finding them before approval is the whole point of the method.

## Notes on the files
- The original dry run used a club with an Italian interface; the files are shown here in English, otherwise unchanged. That run also mixed two languages inside the spec, which is why the released `init` now asks for the **language of specs and documents** (profile, Section 2). You can use NodFirst in any language: the kit is in English, your conversation and your documents need not be.
- The roadmap predates the released format, which adds **depends on** for each feature.
- `Approved by: Human (simulated)` in the profile marks the simulated approval.
