# NodFirst manual

**Version:** 0.1 · NodFirst, a Spec-Driven Development kit · works with any AI coding agent that can read and edit files in a folder.

This manual assumes **no technical knowledge**. Where a technical word is unavoidable it is explained the first time. Parts marked *(for developers)* can be skipped by everyone else.

**How to read it**
- In a hurry? Read Part 1, Part 4 and Appendix C (the commands).
- Want to see what the documents look like? Read Part 14 and the `examples/` folder of the NodFirst repository.
- First time? Read Parts 1 to 7 in order, then try a small project.
- Something went wrong? Go to Part 12.
- Lost? Type `/nodfirst-next` in your tool: it tells you where you are and what to do.

---

# Part 1 — The idea in five minutes

Building software with an AI agent without a plan is like asking a builder to build a house with no blueprint: the builder decides everything, and you find out at the end.

**Spec-Driven Development (SDD)** works the other way round:

1. You say **what** you want and **why**. This is the *specification* ("spec").
2. The agent proposes **how** to build it. This is the *plan*.
3. The plan is cut into small steps. These are the *tasks*.
4. The agent does **one task at a time** and proves it works with tests.
5. Another agent, in a fresh chat, **checks the result** against what you asked for.

**After every step the agent stops and waits for your nod.** Nothing moves on until you say "approved". That is the heart of the method, and the reason for the name.

**Why this helps**
- The agent cannot silently decide things for you. Every decision is written in a file you can read.
- If something is wrong, you find it in a short document, not in finished software.
- The work is repeatable: another person, or another agent, can pick it up from the files.

**What you do:** decide and approve.
**What the agent does:** write, check, report, and stop.
**What you never need to do:** write code or judge technical choices alone (the agent explains every choice in plain words and recommends one). You may occasionally need to install a program or create an account: the agent tells you exactly what and how.

---

# Part 2 — Three ways of working

At the start, NodFirst asks how you want to work. You can change it later.

| | **Guided** | **Solo** | **Team** |
|---|---|---|---|
| For whom | you do not write code | you are a developer working alone | several people review the work |
| How the agent talks | everyday words, one question at a time | technical, up to three questions at once | technical |
| Documents | short; sections that do not apply say only "N/A" and why | shorter still; reports start with a summary | as Solo |
| Approvals | you approve each step | you approve each step; small fixes in one go | each step approved by the right person (for example product approves the spec, engineering the plan) |
| Building | one task, then stop | several tasks in a row if you ask | one branch and one review per feature |
| Saved copies (Git) | the agent saves a copy at each approval | as you like | required |

The approvals never disappear: the profiles change how much you read and how often you are asked, not whether you are asked.

---

# Part 3 — What you need

1. **An AI coding agent.** A tool where an AI can read the files of a project folder, create and change them, and run checks. Examples: Claude Code, Cursor, GitHub Copilot in agent mode, OpenAI Codex, and similar. This manual says "the agent" and "your tool".
2. **A folder for the project** on your computer (it can be empty, or contain an existing project).
3. **The NodFirst kit:** the `kit` folder of the NodFirst repository.
4. **Nothing else to start.** If the agent needs a program installed, it tells you which, in plain words, and stops until you have done it.

**Good habits from day one**
- **Start a new chat for every phase and every task.** The agent does not remember earlier chats; it re-reads the files. That is intended.
- **Keep saved copies.** With Git (Part 5) the agent saves a copy at each approval. Without Git, copy the project folder before every phase.
- **Never paste passwords or keys in the chat.** The agent never needs to see them.

---

# Part 4 — Starting

## 4.1 Install the kit
1. On the NodFirst page on GitHub, click the green **Code** button, then **Download ZIP**. Open the downloaded file: you get a folder.
2. Create a folder for your project (for example `book-club` in your Documents), or use the folder of an existing project.
3. Open the `kit` folder you downloaded, select **everything inside it** (`AGENTS.md`, `CLAUDE.md`, `nodfirst`, `project`, `specs`, `docs`) and copy it into your project folder.
4. Open the project folder in your tool (Part 4.2).

What the folders are:
- `nodfirst/` belongs to the kit (rules, instructions, templates). You never edit it; updates replace it.
- `project/` belongs to your project (its profile, lessons, roadmap). Updates never touch it.
- `specs/` will hold one folder per feature; `docs/decisions/` the records of technical decisions.

## 4.2 Your tool, step by step
You need one AI coding tool. Two common choices, described for someone who has never used them (menus may change slightly over time):

**Claude (desktop app, Code tab)** — needs a paid Claude plan.
1. Download the Claude app from claude.ai for macOS or Windows, install it, open it and sign in.
2. Click the **Code** tab.
3. Under the box where you type, choose **Local** (so Claude works on files on your computer), then click the folder control next to it and pick your project folder.
4. For the permission mode choose **Manual**: Claude asks before every change and every command. It is the safest choice while you learn.
5. Type your first message (Part 4.3) and press Enter. For a new chat later: **+ New** in the sidebar.
(Developers can use Claude Code in the terminal instead: install it, open the project folder in a terminal, type `claude`.)

**Cursor** — has a free plan with limits.
1. Download Cursor from cursor.com, install it, open it and sign in (you can create an account there).
2. **File → Open Folder**, and pick your project folder.
3. Open the Agent panel: **Cmd + I** on Mac, **Ctrl + I** on Windows.
4. Type your first message (Part 4.3). For a new chat later: **Cmd + N** (Mac) or **Ctrl + N** (Windows) in the panel.

**Other tools** (GitHub Copilot in VS Code, OpenAI Codex, and others): open the project folder, open the agent chat in *agent* mode (the mode that can edit files), and write the same first message.

**Hidden folders.** The commands NodFirst installs go into folders whose name starts with a dot (for example `.claude`). Your computer hides them: that is normal. To see them on a Mac, press **Cmd + Shift + .** in Finder; on Windows, in File Explorer choose **View → Show → Hidden items**.

## 4.3 First message
New chat. Type one of these (with your own words after it):

```
follow nodfirst/playbooks/init.md
A mobile app where families share a weekly shopping list. iPhone and Android.
```
For a project that **already has code**, use `adopt` instead of `init` (Part 4.5).

At the end of `init` the agent installs the short commands for your tool, so from then on you can type `/nodfirst-specify` instead of the file path. (In Codex the commands start with `$`.)

## 4.4 What `init` does
The agent asks about 10-15 questions, **one at a time**, each with a suggested answer. You can always reply "your suggestion".
1. It restates your project to check it understood.
2. It asks how you want to work (Part 2) and about saved copies (Part 5).
3. It asks who the product is for, what is in the first version and what is not, which kind of project it is, which languages it speaks, how careful to be with personal data, how quality is checked.
4. It checks that your computer has the programs the project needs.
5. It shows you a summary and **waits for your approval**.
6. Then it writes the files and installs the commands.

**Which kind of project?** NodFirst has **modules**, extra rules for each kind of project:

| Module | Use it for |
|---|---|
| `web` | websites and web apps in a browser |
| `mobile` | apps for phones and tablets |
| `desktop` | programs installed on a computer |
| `backend` | the "behind the scenes" part: services, data, scheduled jobs |
| `library` | reusable code that other programmers use |

Most products need two: a web app with accounts needs `web` and `backend`; a phone app that talks to a server needs `mobile` and `backend`. The agent proposes them; you confirm.

**Untested modules.** Each module says whether it is *proven*, *partly proven* or *not yet proven* (table in `nodfirst/modules/README.md`). If you pick one that has never been used on a real project, the agent tells you so in plain words and asks: "Do you want to continue with it?" You can say yes: the kit still works, but its rules are an informed starting point, some checks need you (real phones or computers, store and cloud accounts), and you are asked to note in `project/lessons.md` whatever turns out wrong.

**Check before approving `init`:**
- Can you read the summary and recognise your project?
- Is the way of working right for you?
- Is there **one single check** (one command) that will test everything? It may still say "TBD" until the project is built; that is normal.
- Are the exceptions to the standard rules written, with a reason? (for example "this library has no screens, so accessibility does not apply")
- Do open decisions say *when* they will be decided?

## 4.5 A project that already has code: `adopt`
```
follow nodfirst/playbooks/adopt.md
Our booking website. Next we want to add online payments.
```
The agent reads the existing project **without changing it**, asks only what it cannot see in the code, and writes:
- the project profile, with the commands it found;
- a "current behaviour" spec (`specs/000-current-behaviour/`): what the product does today, and which parts are covered by tests;
- a list of risks (parts without tests, security concerns, outdated components), each with a suggested first step.
You approve, and from then on new features follow the normal cycle.

---

# Part 5 — Saved copies (Git) in plain words

**Git** is a tool that keeps a history of your project: every saved copy (a "commit") can be looked at or restored later. NodFirst uses it so that every approved step is saved.

- In the **Guided** profile the agent proposes it during `init`. If you agree, it saves a copy each time you approve something (for example "spec 002 approved"). It **never sends anything online** unless you ask.
- To go back, ask: "Show me the saved copies of the last week" and "Bring the project back to the copy called *spec 002 approved*". The agent explains what will be lost before doing it, and waits for your yes.
- If Git is not installed, the agent tells you how to install it, or you can work without it and copy the folder before every phase.
- In the **Team** profile Git is required, with one branch (a separate line of work) and one review request per feature.

---

# Part 6 — Your role, in practice

## 6.1 Decide and approve
At the end of each phase you read a file and a short report. If it is right, you write for example:

> Approved. Anna Rossi, 2026-12-01.

The agent then records it in the file (and, with Git, saves a copy). **Only you can approve.** If the agent ever marks something approved by itself, stop and tell it so.

## 6.2 How to read what the agent gives you
Every report starts with a **summary of at most five lines**. Then, in this order:
1. **Interpretations:** *the most important part.* Every place where the agent had to choose between two readings of what you wrote. If you disagree with a choice, say so now.
2. **Open questions and gaps:** what is still unclear. Answer them.
3. **What was not done or not checked.** A good report says this honestly.

## 6.3 Five questions you can always ask
- "Explain this decision in simple words and tell me what it means for the people who will use the product."
- "What happens if the user does something unexpected here?" (empty field, no internet, a wrong password…)
- "Which sentence in my spec does this come from?"
- "What did you assume that I did not tell you?"
- "How did you check that this works? Show me the result."

## 6.4 Red flags
- The agent used a word you do not understand and did not explain it.
- The report does not say what was **not** checked.
- The agent added something you never asked for (a feature, a licence, an extra tool).
- The agent says "done" but shows no check result.
- The agent moved to the next phase without waiting for you.

Reply: "Stop. Re-read `AGENTS.md`. Explain what you did in plain words and wait for my approval."

---

# Part 7 — The cycle of a feature

A **feature** is one thing the product does: "sign in", "add an item to the list", "export a report". Each feature gets its own folder `specs/001-name/`.

```
specify → (clarify) → (design) → plan → tasks → analyze → implement (task by task) → verify
```
Steps in brackets are optional. `specify` sets the new feature as the **active feature** in `project/profile.md`, so the other commands know which one you mean.

For every phase: **what it is**, **what you type**, **what you get**, **how to check it**.

## 7.1 Specify — say what you want
**What it is.** Turning your idea into a precise written description: who uses it, what must happen, what must not, and how we will know it works.

**What you type.** Three ways to start:
- **A short idea:** `/nodfirst-specify Users can save a recipe and mark it as a favourite. Not included: sharing, comments.` The agent asks up to 5 questions, then writes the spec.
- **Material you already have** (notes, a brief, screenshots, a Figma link): `/nodfirst-specify Mode C. Material: brief.docx, notes.txt, screens/home.png`. The agent keeps your words, shows where each sentence went, describes each image back to you for confirmation, and tells you what it could not place. See Part 9.
- **A change to an existing spec** (Mode B): `/nodfirst-specify Mode B on 001: 1. The password must be at least 12 characters, not 8. 2. Remove the "remember me" option.`

**What you get.** `specs/001-name/spec.md`, status *Draft*, with:
- **User stories** ("As a … I want … so that …").
- **Requirements** (R1, R2…): what must happen. Each says MUST (obligatory), SHOULD (recommended) or MAY (optional).
- **Acceptance criteria** (AC1…): concrete examples that prove a requirement ("If the password has 11 characters, the message says…").
- **Out of scope**, **Open questions**, **Security and privacy**, and **Impact on existing specs** if the feature changes an earlier one.

**How to check it**
- Read the user stories. Is that what you want?
- Read each requirement: does a normal person understand it? Could two people read it differently?
- For each MUST requirement ask: "Which acceptance criterion would fail if we removed this requirement?" If there is none, the requirement is not really checked.
- Look at the numbers (limits, times, lengths). Do all places that mention the same number agree?
- Check the edge cases: empty, too long, wrong kind of input, no internet, a stranger trying to see someone else's data.
- Is anything you did **not** ask for in the spec? Remove it.
- No open question may remain when you approve.

A spec for a small library needed four rounds of corrections in a real run. This is normal: gaps are found by reading carefully.

## 7.2 Clarify — remove doubts *(optional, not yet proven)*
**When.** The spec has open questions, you wrote it yourself, or you feel the agent guessed.
**What you type.** `/nodfirst-clarify`
**What happens.** The agent lists the doubts (vague words, contradictions, missing cases) with a priority, then asks **one question at a time** with options and a recommendation. You get the same spec, updated, and three lists: *Changes*, *Interpretations*, *Still open*. When no sentence can be read two ways, tell the agent "the spec is clarified" and it records the status. *Clarified* is not *approved*: approve the spec as usual before the plan.
If you wrote the spec in your own format, clarify first asks you to run `specify` in Mode C.

## 7.3 Design — what people see *(optional, only for features with screens, not yet proven)*
**What you type.** `/nodfirst-design Screens: sign in, create account, "something went wrong". Material: design/signin.png (follow it exactly), Figma link for the other screens (colours and mood only).`
**What you get.** `specs/001-name/design.md`: the **sources** you gave and what the agent *read* from each image; flows; screens; the table of **states** (empty, loading, error, offline…); every text the user will read; accessibility notes; **conflicts and gaps** (for example: the picture shows no error screen, so the agent *proposed* one, marked "proposed").
**Check.** Does each screen match your material? Is the agent's reading of your images correct? Is every text right? Does any screen show something the spec does not describe? The spec wins on behaviour.

**The design system** (colours, fonts, spacing, buttons) is created once, before the first feature with screens: `/nodfirst-design-system Direction: calm and clear, light and dark mode. Brand colour #2F5D8A (follow it). Material: brand/logo.png`. The agent **calculates** the contrast of every text colour (readable by people with low vision) and marks each value *given* (from your material) or *proposed*.

## 7.4 Plan — how it will be built
**What you type.** `/nodfirst-plan`
**What happens.** The agent first lists what it needs to decide and waits. Then it asks **one decision at a time**, with options, sources it checked and a recommendation, explained in plain words. **It never chooses for you.** If you do not know, say "recommend one and explain the consequences", then decide.
**What you get.** `specs/001-name/plan.md`, and for lasting decisions a short **decision record** in `docs/decisions/`.
**How to check it**
- For every decision, can you say in one sentence what you chose and why?
- Costs and commitments: is there anything you would pay for, or cannot undo? (hosting, accounts, licences)
- What happens to people's data? Where is it stored, for how long, who can read it?
- "How will this be tested?" must have a real answer.

## 7.5 Tasks — the work in small pieces
**What you type.** `/nodfirst-tasks`
**Check.** Each task fits in one sentence; every acceptance criterion has a task that tests it; tasks that need **you** (create an account, buy a domain) are marked "Requires human action" and placed before they are needed; the last task is a **final verification**.

## 7.6 Analyze — a second pair of eyes on the documents
**What you type.** `/nodfirst-analyze`
**What happens.** A read-only check that spec, plan and tasks agree with each other and with the rules. It writes `analysis.md` with findings by severity: **Critical** (something unspecified or untested), **High** (a requirement not properly proven, or documents that contradict each other), lower levels for wording.
**What you do.** Ask the agent to fix findings in the right file, then run analyze again. Start building only when no Critical or High finding is left, or you have accepted them knowingly.

## 7.7 Implement — the building
**What you type.** `/nodfirst-implement` (next task) or `/nodfirst-implement T5`. **New chat for each task.**
**What happens.** The agent writes the test first and shows it failing, writes the minimum code to make it pass, runs the single check, and reports: Task · Before (the test failed for the right reason) · Tests added · What changed · Checks and results · Deviations · Not done · Interpretations.
**How to check (no code reading)**
- Is there a "Before"? Does it say which command was run and how many tests passed?
- Is every deviation explained? Did the agent add anything you did not ask for?

**When the agent stops.** If a task cannot be done because the spec or plan is wrong, or a program is missing, the agent **stops and writes a change request**. That is good behaviour. You decide: revise the spec or plan, approve again, continue.

## 7.8 Verify — the independent check *(not yet proven)*
**What you type,** in a **new chat**, ideally with a different model or tool: `/nodfirst-verify`
**Why.** The agent that wrote the code should not be the only one to say it is right. Verify reads only the files and the code, runs the checks itself, and answers for each requirement: *met*, *partial*, *missing*, *contradicts* or *untested*. It also looks for things **nobody asked for**, does a security and privacy review, and lists the checks only a person can do (for example "open the app on your phone and try to sign in with a wrong password").
**What you get.** `verification.md` with a verdict:
- *not verified*: at least one serious problem in the code (Critical or High);
- *partly verified*: no serious problem found, but some checks only you can do are still open (they are in the list "Needs a human": tell the agent the result of each);
- *verified*: no serious problem, and nothing left for you to check.
**What you do.** You decide. Either the problems become new tasks or spec changes and verify runs again, or you **close** the feature knowingly: you name each problem you accept, why, and what will be done about it later (`/nodfirst-verify close accept F3: the time is shown in UTC, fix it in the next feature`). The agent writes your decision in the file and never changes the verdict to fit it. The feature is finished when you close it, even when it is *verified*.

---

# Part 8 — Small fixes (light track)

For a bug, or a small change to **one behaviour** that touches no stored data structure, public interface, sign-in or personal data:
```
/nodfirst-fix When a list is empty, the "Share" button still appears. It should be hidden.
```
The agent first checks that it is really small (otherwise it recommends the full cycle). It writes a short spec (goal, criteria, the test), waits for your approval, writes a failing test, fixes, runs the checks and reports. If in doubt, use the full cycle.

---

# Part 9 — Giving the agent your material

You may describe things in words, with pictures, with links to design tools, or all together.

| Material | Good for | Tips |
|---|---|---|
| **Words** (notes, brief, your own spec) | intent, rules, tone | Write like you speak. Say what must never happen. Give numbers (how many, how long). |
| **Images** (screenshots, photos of sketches, exported screens, PDFs) | what screens look like | One screen per image, clear names (`signin.png`), say what each is. |
| **Design-tool links or files** (Figma and similar) | appearance, styles, flows | Many agents cannot open them. If not, **export** the screens as images or PDF and copy the colour and font values. |
| **A running product** | patterns to keep | Say what to keep and what to fix. |

**Say what each item is worth:** *follow it* (the agent matches it) or *inspiration* (the agent borrows ideas). If you say nothing, the agent asks.

**What the agent does with it**
- It lists every item and tells you what it **read** from it ("a blue button labelled 'Sign in'"). You confirm or correct.
- It never pretends to have read a link it could not open.
- **Behaviour comes from the spec, appearance from the pictures.** A picture shows a screen, not a rule: "the button is there" does not say who may press it or how many times. Those become questions.
- **Conflicts are asked, never decided silently.** Order of authority if you have not said otherwise: your statement in the chat → the spec → pictures and design files → the design system → written taste → inspiration.

**A good first description (template)**
```
Product: <one sentence>
Who uses it: <people and what they want>
What it must do (v1): <list>
What it must NOT do / out of scope: <list>
Important numbers: <limits, times, sizes>
Languages: <…>
What is sensitive: <personal data, money, health…>
Material: <files and links, with role: follow it / inspiration>
```

---

# Part 10 — Changing your mind

Changes are normal. The rule: **change the document first, then everything after it.**
1. Revise the spec (`/nodfirst-specify Mode B on 001: …`), one numbered change per point, mentioning the IDs ("R5", "AC3").
2. The agent returns **Changes**, **Interpretations** and **Downstream impact** (which parts of plan and tasks now disagree).
3. Approve the spec again, then revise plan and tasks the same way, then run `analyze`.
4. Only then change the code.

IDs never change: a removed requirement stays listed as *Withdrawn*, new ones get new numbers at the end. **Extending a feature** (002 adds to 001): write a new spec; it lists its impact on 001.

---

# Part 11 — Modules and kinds of project

- The modules chosen at `init` are listed in `project/profile.md`, Section 1. The agent reads them in every phase.
- `library` is **proven**, `web` **partly proven**; `backend`, `mobile` and `desktop` are **not yet proven** (careful checklists from standard practice). You can use them: the agent warns you and asks for confirmation.
- **Real devices and machines:** for mobile and desktop, some checks can only be done on a real phone or computer. The agent asks you to run the app and report what you see.
- **Accounts and consoles** (app stores, cloud services, certificates) are always done by you. The task list marks them "Requires human action".
- If your kind of project has no module (for example features built on AI models), the agent uses the core rules and tells you what it could not check.

*(for developers)* A module has rules, typical quality gates, and checklists for specify, design, plan and tasks. Write a new one from `nodfirst/modules/README.md` after the first real project of that kind.

---

# Part 12 — When something goes wrong

| What you see | What it means | What to do |
|---|---|---|
| You do not know where you are | normal after a break | `/nodfirst-next` |
| The agent starts building before you approved | it broke the approval rule | "Stop. Nothing proceeds without my approval. Undo what you did after <file> and wait." With Git: "bring the project back to the last approved copy" |
| The agent adds something you did not ask for | it filled a gap on its own | "Remove it and explain why you added it." Note it in `project/lessons.md` |
| The agent uses technical words | the plain-language rule is not followed | "Explain this in everyday words and say what it changes for users." If it keeps happening, check that the profile says Guided |
| A task is blocked: a program is missing | the computer lacks something | install what it names (the agent explains how), then run the task again. Never accept "lower the version to continue" |
| `analyze` or `verify` finds a contradiction | the documents or the code disagree | fix the document that is wrong (Part 10), run the check again |
| The plan quotes old numbers after you changed the spec | the plan was not updated | ask for a revision of the plan, using the *Downstream impact* list |
| A task is huge | it bundles several things | "Split this into tasks of one deliverable each" |
| The agent cannot open your Figma link | many agents cannot | export the screens as images; copy colour and font values |
| The agent says "tests pass" but shows nothing | unverified claim | "Show the command and its result" |
| The `/nodfirst-…` commands do not appear | the command files are not installed for your tool | "Install the NodFirst commands for <your tool>" (the agent follows `nodfirst/adapters/README.md`), or mention the playbook file instead |
| The agent ignores a file | it did not read it | name the file in your message, or "read the Context to read list of the playbook" |
| The agent reads or prints a password | not allowed | stop, change that password, tell the agent never to read secrets |

**Golden rule:** when in doubt, stop the agent and ask it to explain. A pause costs nothing; a wrong step costs a lot.

---

# Part 13 — Keeping the kit healthy

- **Lessons:** whenever you correct the agent for a reason that could happen again, it proposes a line for `project/lessons.md` (date, what happened, cause, rule added); when you close a feature, it proposes up to three. You say which to keep. If a lesson is general, it can improve NodFirst itself: open an issue or a pull request in the NodFirst repository with the lesson.
- **Updating NodFirst:** replace the `nodfirst/` folder with the new one (and `AGENTS.md`, `CLAUDE.md` if the release notes say they changed). Do not touch `project/`, `specs/` or `docs/`. Then type `/nodfirst-init update`: the agent checks what changed, proposes additions to your profile (never removals) and refreshes the commands of your tool.
- **Exceptions:** if a rule of the constitution does not fit your project, the agent records an exception in `project/profile.md` with the reason, and you approve it. The constitution itself is never edited in a project.

---

# Part 14 — Examples

## 14.1 A real run (condensed)
A small project: a code library that understands date phrases written in Italian (such as "in 3 days"). This run used a pre-release version of the kit; the phases are the same.

1. **init.** About nine questions. Result: the project is a library; the library rules apply; one command checks everything; accessibility and screens do not apply (written as exceptions with reasons).
2. **specify.** Four rounds of review. Gaps found by a careful human read: what counts as a digit, what counts as a space, accents written in two ways, what happens if the wrong kind of value is passed, and two criteria that contradicted each other (one accepted the plural form with the number 1, as in "in 1 days", another rejected it).
3. **plan.** Decisions asked one by one (the shape of the result, the package name, how to check types, the order of cleaning the text, where documentation tests live). A table in the plan accepted a wrong phrase; found and fixed in review.
4. **tasks.** Ten tasks; analysis found problems; fixed; run again.
5. **implement.** Ten tasks, 112 tests, all checks passing from a clean start.
6. **Next feature.** A second spec added more phrases (weeks, "the day after tomorrow") and was built in five tasks, with 160 tests in total.

**What the method prevented:** a lookalike character being accepted as a weekday; a plural form accepting the number 1; a task too large to verify; a plan that quoted an outdated criterion.

## 14.2 What a first draft looks like, and how to review it
The `examples/book-club/` folder of the NodFirst repository shows the files an agent wrote for an imaginary book club (profile, roadmap, first spec) **exactly as drafted**, with a review that points out what a careful reader should catch before approving: a criterion with no action, an edge case decided by the agent instead of asked, an assumption hidden in a sentence, a rule that only exists in an edge case. It is illustrative, not a real project. Read the draft first, try to find the problems yourself, then read the review.

## 14.3 A whole feature, from start to finish
The `examples/shortz/` folder of the NodFirst repository has every document of one real feature: a small web app that shortens links, built in one day by an agent and deployed. You can follow it from the profile to the last verification: the check that added two missing criteria before any code, a security problem found by the independent check and fixed through the normal path, and how the owner closed the feature knowingly with fourteen problems accepted.

---

# Appendix A — Glossary (plain words)

- **Acceptance criterion (AC):** a concrete example that shows a requirement works.
- **Agent:** the AI that reads files, writes files and runs checks for you.
- **Approval:** your explicit "approved". Only you give it.
- **Backend:** the part of a product users do not see: stores data, applies rules, talks to other services.
- **Branch:** in Git, a separate line of work that is merged when it is ready.
- **Change request:** a note the agent writes when a spec or plan is wrong or incomplete. You decide.
- **Commit:** in Git, a saved copy of the project.
- **Constitution:** the core rules of NodFirst, the same in every project (`nodfirst/constitution.md`).
- **Contrast:** the difference in brightness between text and its background; low contrast is hard to read.
- **Decision record:** a short note saying what was decided, why, and what else was considered.
- **Design system:** the shared rules for how everything looks and behaves.
- **Feature:** one thing the product does; has its own folder under `specs/`.
- **Gate:** a condition that must be met: an approval, or a quality check.
- **Git:** a tool that keeps the history of a project, so any saved copy can be restored.
- **Interpretation:** a choice the agent made where your text could be read in two ways.
- **Light track:** a short route for small fixes (`fix`).
- **Mode A / B / C:** new spec / revise a spec / adopt material you wrote or collected.
- **Module:** extra rules for one kind of project (web, mobile…).
- **Plan:** how the feature will be built.
- **Playbook:** the instructions file the agent follows for one phase.
- **Profile (project):** `project/profile.md`, the description of your project and how you work.
- **Pull request:** in Git hosting services, a request to review and merge a branch.
- **Quality checks:** automatic checks (style, correctness, tests) that run with one command.
- **Requirement (R):** something the product must (MUST), should (SHOULD) or may (MAY) do.
- **Spec:** the written description of a feature.
- **Task:** one small step of the work.
- **Test:** a small program that checks one behaviour.
- **Traceability:** the chain requirement → criterion → plan → task → test.
- **Verification:** the independent check of the finished code against the spec.

---

# Appendix B — Checklists

**Before approving `init` or `adopt`:** you recognise your project · the way of working is right · one command for all checks (or TBD until the project is built) · exceptions written with reasons · open decisions have a time.
**Before approving a spec:** stories are what you want · each requirement understandable and testable · each MUST proven by a criterion · numbers consistent · edge cases covered · out of scope clear · no open questions · impact on earlier specs listed.
**Before approving a design:** matches your material · the agent's reading of images confirmed · texts right · states complete · conflicts and gaps decided · nothing the spec does not allow.
**Before approving a plan:** every decision explained and recorded · covers every requirement, nothing extra · data and privacy clear · costs and commitments known · testing described · versions fixed.
**Before approving tasks:** small · every criterion tested · your own actions marked · final verification last.
**Before accepting a task:** "Before" present · checks and results shown · deviations explained · nothing unrequested added · interpretations agreed.
**Before closing a feature:** `verify` run in a new chat · verdict *verified*, or every problem left accepted by you with a reason and a follow-up · the "needs a human" checks done by you, or accepted the same way.

---

# Appendix C — Commands

After `init` or `adopt` your tool knows these commands. Add your words after the command. In Codex, type `$` instead of `/`. In a tool without commands, write "follow `nodfirst/playbooks/<name>.md`".

```
/nodfirst-init <a few lines about the project>       set up a new project
/nodfirst-init update                                after updating the kit
/nodfirst-adopt <a few lines>                        set up a project that already has code
/nodfirst-next                                       where are we, what now?
/nodfirst-specify <idea>                             new spec (Mode A)
/nodfirst-specify Mode B on 001: 1. … 2. …           revise a spec
/nodfirst-specify Mode C. Material: <files, links>   adopt your material
/nodfirst-clarify                                    remove doubts from the spec
/nodfirst-design-system <direction, material>        colours, fonts, components (once)
/nodfirst-design <screens, material>                 screens of a feature
/nodfirst-plan                                       how it will be built
/nodfirst-tasks                                      the work in small steps
/nodfirst-analyze                                    check the documents agree
/nodfirst-implement                                  next task (or: /nodfirst-implement T5)
/nodfirst-verify                                     independent check (new chat)
/nodfirst-verify close accept F3: <reason>           close the feature, accepting what is left
/nodfirst-fix <what is wrong>                        small fix (light track)
```

Useful replies at any time:
```
Approved. <name>, <date>.
Stop. Explain what you did in everyday words and wait for my approval.
Show the command you ran and its result.
What did you assume that I did not tell you?
Explain this decision in simple words, give the options, and recommend one. I will decide.
```

---

# Appendix D — Where everything is

```
AGENTS.md                short rules every agent reads first
CLAUDE.md                points to AGENTS.md (for tools that read CLAUDE.md)
nodfirst/                THE KIT – replaced on update, never edited
  VERSION                kit version
  constitution.md        core rules C1–C14, working profiles, workflow
  manual.md              this manual
  playbooks/             one instruction file per phase
  templates/             empty forms: spec, plan, tasks, design
  modules/               extra rules by kind of project
  adapters/              command files for coding tools
project/                 YOUR PROJECT – never touched by updates
  profile.md             active feature, way of working, scope, commands, quality checks, exceptions
  lessons.md             what went wrong and which rule was added
  roadmap.md             next features (created by init)
  design-system.md       (created when needed)
specs/001-name/          spec.md · design.md · plan.md · tasks.md · analysis.md · verification.md · design/ (images)
docs/decisions/          decision records
```

**Who writes what:** the agent writes every file; you approve. You write only: your idea, your material, your answers, your approvals.

**If files disagree, this order wins:** constitution (with your profile's exceptions) → spec → design → plan → tasks → code. The agent stops and asks when they conflict.

---

# Appendix E — Status of this kit

| Part | State |
|---|---|
| `init` interview and profile, `specify` (Modes A and B), `plan`, `tasks`, `analyze`, `implement` | proven on two projects before the first release, used on a third after it |
| Working profile Solo, Git checkpoints, command files for Cursor, `design`, `verify` | used on one real project |
| Working profiles Guided and Team, command files for other tools, `init update` | new in 0.1, not yet used |
| `adopt`, `next`, `fix`; closing a feature after `verify` | new, not yet used |
| `specify` Mode C, `clarify`, `design-system` | written, not yet used |
| Module `library` | proven (on a sandbox project) |
| Module `web` | partly proven, on two projects |
| Module `backend` | used once, not yet reviewed line by line |
| Modules `mobile`, `desktop` | written from standard practice, not yet used |
| AI-feature module | not written |

Every "not yet used" part improves with its first real use: note what you find in `project/lessons.md`.
