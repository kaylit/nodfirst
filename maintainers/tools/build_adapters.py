#!/usr/bin/env python3
"""Regenerate kit/nodfirst/adapters/ from the list of playbooks below.

Run from the repository root:  python3 maintainers/tools/build_adapters.py
Standard library only. Re-run after adding, renaming or describing a playbook.
"""
import pathlib, shutil

COMMANDS = {
    "init":          ("Set up NodFirst in a new project: profile, working profile, Git, commands.", "a few lines about the project, or 'update'"),
    "adopt":         ("Set up NodFirst in a project that already has code.", "a few lines about the project"),
    "specify":       ("Write or revise a feature spec (what and why, no technology).", "the idea, the change requests, or your material"),
    "clarify":       ("Remove ambiguity from the active spec, one question at a time.", "optional feature number"),
    "design-system": ("Create or revise the project's design system.", "visual direction and material"),
    "design":        ("Describe screens, flows, states and texts of the active feature.", "screens to cover and material"),
    "plan":          ("Turn the approved spec into a technical plan, one decision at a time.", "optional feature number"),
    "tasks":         ("Break the approved plan into small, ordered, verifiable tasks.", "optional feature number"),
    "analyze":       ("Read-only consistency check of spec, plan and tasks.", "optional feature number"),
    "implement":     ("Carry out the next task (or a named one): tests first, then code.", "optional task, e.g. T5"),
    "verify":        ("Independent check of the finished code against the spec. Run in a new chat.", "optional feature number"),
    "fix":           ("Light track: a bug fix or a small change to one behaviour.", "what is wrong or what should change"),
    "next":          ("Where are we and what is the next step? Changes nothing.", ""),
}

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "kit" / "nodfirst" / "adapters"

def body(name, args_line):
    return (f"Follow `nodfirst/playbooks/{name}.md` exactly, from its \"Context to read\" to its \"Stop\".\n"
            f"Do not start any other phase: NodFirst waits for the human's approval after every phase.\n"
            f"{args_line}\n")

def main():
    for sub in ("claude", "codex", "cursor", "copilot"):
        shutil.rmtree(OUT / sub, ignore_errors=True)
    for name, (desc, hint) in COMMANDS.items():
        cmd = f"nodfirst-{name}"
        # Claude Code: .claude/skills/<cmd>/SKILL.md
        d = OUT / "claude" / cmd; d.mkdir(parents=True)
        (d / "SKILL.md").write_text(
            f"---\nname: {cmd}\ndescription: NodFirst – {desc}\n"
            + (f"argument-hint: {hint}\n" if hint else "")
            + "disable-model-invocation: true\n---\n\n"
            + body(name, "The human's input, if any: $ARGUMENTS"))
        # Codex: .agents/skills/<cmd>/SKILL.md
        d = OUT / "codex" / cmd; d.mkdir(parents=True)
        (d / "SKILL.md").write_text(
            f"---\nname: {cmd}\ndescription: NodFirst – {desc} Use only when the user explicitly invokes {cmd}.\n---\n\n"
            + body(name, "The human's input is the rest of their message."))
        # Cursor: .cursor/commands/<cmd>.md (plain Markdown, no front matter)
        d = OUT / "cursor"; d.mkdir(parents=True, exist_ok=True)
        (d / f"{cmd}.md").write_text(f"# {cmd}\n\n{desc}\n\n" + body(name, "The human's input is the rest of their message."))
        # GitHub Copilot: .github/prompts/<cmd>.prompt.md
        d = OUT / "copilot"; d.mkdir(parents=True, exist_ok=True)
        (d / f"{cmd}.prompt.md").write_text(
            f"---\ndescription: NodFirst – {desc}\nagent: agent\n---\n\n"
            + body(name, "The human's input is the rest of their message."))
    print(f"{len(COMMANDS)} commands written to {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
