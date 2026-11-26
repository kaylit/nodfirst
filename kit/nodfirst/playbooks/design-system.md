# Playbook: Design system

**Version:** 0.1 (not yet proven)
**Purpose:** create or revise `project/design-system.md`: the visual and interaction rules every feature must follow (tokens, components, states, responsive behaviour), for a web, mobile or desktop UI. The human may describe the direction in words, provide brand material, images, a design-tool file (for example Figma), or any mix.
**Prompt:** `/nodfirst-design-system` (or mention `nodfirst/playbooks/design-system.md`) and, below it, the direction and any files or links. Extra instructions below.
**Output:** `project/design-system.md`, status `Draft`.

## Context to read (do not ask the human to attach it)
`AGENTS.md`, `nodfirst/constitution.md`, `project/profile.md` (Sections 4 and 7), the modules it lists (`nodfirst/modules/`), the decision record of the UI library or toolkit if the project uses one, the existing `project/design-system.md` if any, and the material the human attached or linked.

## Preconditions
- If the project uses a UI library or toolkit, its decision is made and recorded (the profile or a decision record). If not, stop and say so (C2, C10).
- Section 7 of `project/profile.md` exists.

## Modes
- **Create:** no design system yet. Start from the human's direction and material.
- **Import:** the human has styles, variables or a brand guide (including in a design tool). Extract them; do not redesign them.
- **Revise:** a design system exists. Change only what the human asks for; list every feature that the change affects.

## Reference material
Apply the same rules as the design playbook ("Reference material"): list each item with its role (authoritative or inspiration); write down what you read from images and confirm it; if a design-tool link cannot be opened, ask for exports or the style values; conflicts are asked, not resolved. In the design system, mark every token and component as **given** (taken from the material, with the source) or **proposed** (you chose it).

## Instructions for the agent

Follow `nodfirst/constitution.md`, especially C3, C7, C8 and Section 7 of the profile.

1. **Read** the context and show the inventory of material and your reading of it. Ask the human to confirm.
2. **Interview the human**, one question at a time (Solo and Team: up to three per message), in plain words, each with a proposed default: tone and personality, density (compact or airy), colours or brand constraints, light and dark themes, typography, iconography, motion, supported platforms. Skip what the human already gave.
3. **Propose the foundations:**
   - Colour tokens with semantic names (background, surface, text, accent, danger, success, and so on), for each theme in use.
   - **Contrast:** compute the contrast ratio of every text and interactive pair with a script and show the numbers. Do not estimate. Every pair must meet WCAG 2.2 AA (C7). If a given colour fails, report it and propose an adjusted value as an alternative; never change a given colour silently.
   - Typography scale, spacing scale, radii, elevation, breakpoints or window and screen classes of the supported platforms, motion durations and the reduced-motion rule.
   - Minimum touch or click targets from the active module (web: 44×44 CSS px; iOS: 44×44 pt; Android: 48×48 dp; desktop: per platform guideline).
   - Names that are platform-neutral, plus a short note for how each token maps on each supported platform.
4. **Components:** list the components taken from the chosen library or toolkit and the ones to build, with their states (default, hover or pressed, focus, active, disabled, loading, error). Describe behaviour and accessibility rules, not code.
5. **Patterns:** forms and validation messages, empty, loading, error, offline and permission-denied states, feedback (toasts, inline messages), navigation, how texts come from the message catalogue and layouts tolerate longer translations.
6. **Check** against Section 7 of the profile and the active modules, and report every rule you could not satisfy.
7. **Stop.** Show a summary, the contrast results, the list of given versus proposed items, assumptions and **interpretations**. Ask for review. Do not create components or code.

## Do not
- Choose the UI library or toolkit.
- Invent brand identity without the human's input.
- Mark the design system as `Approved`.
- Change a given value without telling the human.

## Example
Prompt:
```
/nodfirst-design-system
Direction: calm and clear, airy, light and dark. Brand colour #2F5D8A from our logo (authoritative).
Material: brand/logo.png, Figma link (inspiration for shapes only).
```
Agent: "I cannot open the Figma link: please export the main screen as an image. The brand colour on white has contrast 6.7:1 (passes AA for text). On the dark background it would need a lighter variant: I propose #7FA9D6 (7.9:1), marked 'proposed'. Do you accept?"

## Extra instructions / visual direction
<!-- Write below this line when you use the playbook. -->
