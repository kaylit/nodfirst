# Module: Library or package

**Version:** 0.1
**Scope:** a library, SDK or package with a public API used by other code (no UI, no hosting of its own). Language-neutral. Written from a text-parsing library; rules marked *text* apply when the API accepts text.
**State:** proven on one sandbox project built to test the kit (two features, fifteen tasks, 160 tests). Rules L7–L11 are written from standard practice and are *not yet proven*.

## Rules (in addition to the constitution)

- **L1 – The public API is the contract.** Every public name, type, error form and fixed message is in the spec and tested. No behaviour outside the spec. What is not public is marked as such (naming convention, module visibility) and may change without notice.
- **L2 – Failure forms are decided in the spec.** Failures caused by the input are typed results with fixed reason codes in English and fixed messages; failures caused by the caller's misuse (wrong types, missing arguments) are documented exceptions. They are different things and tested separately.
- **L3 – Messages do not echo the input** (C6). A check for this is vacuous for empty input: say what holds instead.
- **L4 – One command runs every quality gate** locally (no CI needed): lint, format check, strict type check including the tests, and tests. It is written in `project/profile.md`, Section 5.
- **L5 – Documentation for integrators is tested.** Every fixed message, reason code and documented example appears in the README and is checked by a test (examples run as doctest or equivalent). Documentation is not a later cleanup.
- **L6 – Accessibility (C7) and end-to-end flows (C5)** do not apply: record the exception in the profile, Section 10.
- **L7 – Versioning and compatibility.** The spec or plan states the versioning scheme (semantic versioning unless decided otherwise), which changes are breaking (any change to a public name, type, error form, message or default), the supported runtime versions, and the deprecation policy. A breaking change is a MAJOR version and an entry in the changelog.
- **L8 – Dependencies are liabilities (C8).** Every runtime dependency is justified in the plan (what it gives, why not the standard library), pinned or range-bounded on purpose, with its licence and maintenance state checked. Development tools are separate from runtime dependencies. Prefer none.
- **L9 – Behaviour under load and concurrency.** The spec says whether the API is safe to call from several threads or tasks, whether it keeps global state (it should not), and any size or time limits. Where input can be large or hostile, limits are enforced before the expensive work (for example length before parsing, a regular expression without catastrophic backtracking).
- **L10 – Packaging and publication (only if the spec asks).** What is published, where, under which name, with which licence **chosen by the human**, and how a release is made and verified (install in a clean environment and run the README example). Never add a licence, author or metadata that nobody named (C3).
- **L11 – Asynchronous or network APIs (if any).** Timeouts, cancellation, retries (which errors, how many, with what backoff) and how failures surface are decided in the spec; tests use a fake of the remote side, and a separate, clearly marked check uses the real one.

## Typical quality gates (copy into `project/profile.md`, Section 6)
1. Lint, 2. format check, 3. strict type check on source and tests, 4. unit tests (including the documentation tests), 5. all of them through the single command, run from a fresh environment at the end of a feature, 6. for published packages: build the package, install it in a clean environment, run the README example, 7. dependency audit if there are runtime dependencies.

## Checklists

**Specify.** The public surface as a list: names, inputs, outputs, errors. For every text input: normalization form, digit repertoire (ASCII or other scripts), what counts as whitespace, letter case, accents, how the length limit is measured, empty input, unusual characters. For every caller-supplied value: wrong types, `None`/null, and subclasses that pass a type check but break the meaning (a timestamp passed where a date is expected). List the accepted forms explicitly, and what each near-miss does (singular/plural, leading zeros, signs). Limits and out-of-range values: which failure, which message. Time, locale and randomness: what the API takes as an argument instead of reading from the environment (a reference date, never "now" inside). An extension of an existing contract lists its impact on the earlier spec and whether it is breaking (L7).

**Plan.** The public interface with a short example of use from the caller's side. Accepted forms in an explicit table; match whole strings; explicit ASCII digit ranges (many languages accept other scripts' digits in `\d` and in number parsers); plain lower-casing when the spec only says "ignore case"; a fixed order for trim, length check, normalization, whitespace collapse and comparison, with tests at the boundaries (including decomposed characters); type checks at the public boundary that state their intent, in one function. Verify standard-library facts you rely on (constants, limits). Pin exact tool versions from the registry, with release dates. Document how each fixed message reaches the README test. Dependencies, versioning and supported runtimes (L7, L8).

**Tasks.** Order: runtime check, scaffolding, environment and smoke test, single command recorded in the profile, then pure logic with tests first, one family of forms per task, documentation and its tests last, then packaging and release if in scope. If a feature changes behaviour already covered by tests, the task that updates those tests comes first.

## Typical open decisions
Package name, result and error forms, supported forms, date or number model, length limits, versioning and supported runtimes, dependencies, CI, publication target and licence.

## Proven and not yet proven
- **Proven:** the whole flow from `init` to the last task, a second feature that extends the first, revision rounds on every document, and an analysis before implementation.
- **Not yet proven:** a library with runtime dependencies, an asynchronous or network API, publication to a package index, a CI pipeline, versioning of the public API (L7–L11).
