# What changed in each version

Read by `/nodfirst-init update` after the human replaces `nodfirst/`. Newest first. For each version: the files to replace, profile changes, and what affects a feature in progress. The full history is `CHANGELOG.md` in the NodFirst repository.

## 0.2.1
- **Replace:** `nodfirst/`.
- **Profile:** no change.
- **Light track:** a fix stays the active feature until it is finished. It is finished when the human accepts the implementation report, or, for a security-relevant fix, when the human closes it after `verify` (`/nodfirst-verify close`). Light fixes have no roadmap line.
- **`verify` on a light fix:** checks the light spec, the specs it changes and the commits of the fix; there is no `tasks.md`.
- **`init update`:** reads this file instead of asking for release notes.
- **In progress:** a light fix already implemented and accepted under 0.2.0 is finished; nothing to redo.

## 0.2.0
- **Replace:** `nodfirst/` and `AGENTS.md`.
- **Profile:** no change.
- **`verify`:** after a verification the human fixes or closes the feature (`/nodfirst-verify close`), naming every Critical or High finding left and every open Needs-a-human check, with a reason and a follow-up; the verdict never changes. Checks the agent cannot do from its environment go to "Needs a human", never findings or passes. Exact rules for `verified`, `partly verified` and `not verified`; a re-run accounts for every previous finding.
- **Lessons:** the agent proposes entries for `project/lessons.md` when corrected, and up to three when a feature is closed.
- **In progress:** a feature already verified under 0.1.0 is not finished until the human closes it; `next` will say so.
