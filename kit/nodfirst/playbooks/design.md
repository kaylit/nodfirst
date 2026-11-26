# Playbook: Design

**Version:** 0.1 (used on one project, one feature; not yet with images or a design-tool file)
**Purpose:** for a feature with a user interface, describe what users see and do: flows, screens, states, components, copy, and accessibility. The human may provide a written description, images, links to design tools (for example Figma), or any mix.
**Prompt:** `/nodfirst-design` (or mention `nodfirst/playbooks/design.md`) and, below it, the screens to cover and any files or links. Extra instructions below.
**Output:** `specs/NNN-feature-name/design.md`, status `Draft`. Reference images and exports go in `specs/NNN-feature-name/design/`.

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `project/profile.md` (including Section 7), the modules it lists (`nodfirst/modules/`), `nodfirst/templates/design-template.md`, `project/design-system.md` if it exists, the active feature's `spec.md`, and the reference material the human attached or linked.

## Preconditions
- The spec is `Approved` (`Clarified` is not enough).
- This phase is optional. Skip it when the screens are trivial and the spec already describes their states.

## Reference material (how to treat what the human provides)

| Kind | How to use it | Limits |
|---|---|---|
| **Written description** | Source of intent for screens, tone, priorities | Ask about anything vague; never fill gaps with taste |
| **Images and screenshots** (PNG, JPG, PDF pages) | Write down what you *read*: screens, elements, texts, states, hierarchy, apparent colours and spacing. The human confirms the reading | Colours and sizes read from a picture are approximate: mark them "approx."; texts inside images are transcribed and confirmed, not trusted |
| **Design-tool files or links** (Figma and similar) | If a connector or tool lets you open the file, read frames, components, text and styles; record the file name, frame names and version or date. If you cannot open it, say so and ask for exports (images or PDF) and, if available, the styles and measurements | Never guess content from a link you cannot open. A link may change after you read it: record when you read it |
| **Existing product** (running app or website, screenshots) | Source of current patterns to keep | Do not copy problems the spec wants to fix |

**Rules**
1. **List every item you received** in the design file's "Sources" table: what it is, where it is, version or date, what it covers, and its role: *authoritative* (follow it) or *inspiration* (borrow ideas). If the human did not say, ask.
2. **Authority when sources disagree** (unless the human says otherwise): the human's explicit statement in this conversation > the spec (behaviour) > authoritative design files and images (appearance) > the design system > written descriptions of taste > inspiration. For **behaviour** the spec always wins over a picture (C1): a screen that shows something the spec does not describe is reported as "not in the spec", not designed in.
3. **Report every conflict** (image against spec, image against design system, two images) in "Open questions" and ask; never resolve silently.
4. **Gaps are findings, not freedom:** a spec requirement shown nowhere in the sources, or a screen state no source shows (error, empty, loading, offline, permission denied), is listed as a gap. You may propose a state following the design system, marked "proposed".
5. Do not claim an image or file says something you could not read in it.

## Instructions for the agent

You are describing the interface, not building it. Follow `nodfirst/constitution.md`, especially C1, C3 and C7, and Section 7 of the profile.

1. **Read** the context. If the design system does not exist, say so and use only the rules of the constitution and the module; do not invent tokens.
2. **Inventory the sources** (rules 1 above) and show it with your **reading of each image** (what you see, in a short list). Ask the human to confirm or correct.
3. **List the screens and flows** the spec implies and the sources show, with the requirement and story IDs each serves, marking what is only in the spec, only in a source, or in both. Show the list and ask the human to confirm.
4. **Ask only what you need** about visual intent (references, tone, priorities on small screens), one question at a time (Solo and Team: up to three per message), in plain words, with a proposed default. Do not ask about technology.
5. **Write `design.md`** from the template: flows as numbered steps; for each screen its purpose, entry points, layout for the smallest supported screen first, larger layouts, main actions and the source it comes from; the states table; components (existing from the design system versus new: a new component or token is a **proposal**); copy (every user-facing string with a key, in the project language, no text hard-coded in components, messages that follow the spec); accessibility (order, focus, labels, announcements, contrast, target sizes). Apply the "Design" checklist of every active module (mobile and desktop: one set of screens per supported form factor and platform convention).
6. **Check:**
   - Every UI-related requirement and acceptance criterion is shown by at least one screen or state.
   - No screen shows behaviour the spec does not describe (C1).
   - Messages do not leak what the spec says must not leak.
   - Touch targets, contrast and states comply with the constitution and the active modules.
   - Every item in "Sources" is used or explicitly set aside.
7. **Stop.** Show a summary, the **conflicts**, the **gaps**, and the list of **interpretations**. Ask for review. Do not start the plan.

## Do not
- Choose libraries or frameworks, or write code.
- Add or change design-system tokens or components. Propose them.
- Mark the design as `Approved`.
- Redraw or "improve" an authoritative design on your own.

## Example
Prompt:
```
/nodfirst-design
Screens: sign-in, registration, "something went wrong".
Files: design/signin.png (authoritative), Figma link for the registration frames (inspiration, colours only).
```
Agent: "I cannot open the Figma link from here. Please export the frames as images, or paste the colour and font values. For signin.png I read: logo at the top, two fields (email, password), a primary button 'Sign in', a link 'Forgot password?' (not in the spec: recovery is out of scope). Do I read this correctly?"

## Extra instructions
<!-- Write below this line when you use the playbook. -->
