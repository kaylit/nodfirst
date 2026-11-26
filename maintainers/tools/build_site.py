#!/usr/bin/env python3
"""Generate the NodFirst documentation site into .site-build/ (for GitHub Pages + Just the Docs).

Run from the repository root:  python3 maintainers/tools/build_site.py
Standard library only. The site is built from the repository's own files, so it is never out of sync:
  README.md            -> Home and "Compare with Spec Kit"
  kit/nodfirst/manual.md -> Manual (one page per Part and Appendix)
  kit/nodfirst/*       -> Reference (constitution, playbooks, modules, templates, command files)
  examples/            -> Examples
  CHANGELOG.md, ROADMAP.md, CONTRIBUTING.md -> project pages
Static files (configuration, colours, includes) live in site/.
Exit code 1 if a generated page links to a site page that does not exist.
"""
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / ".site-build"
REPO_URL = "https://github.com/kaylit/nodfirst"
BASE = "{{ site.baseurl }}"

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_adapters import COMMANDS  # noqa: E402

# Menu labels for the playbooks, in plain words (the exact command is shown on each page).
LABELS = {
    "init": "Init: start a new project",
    "adopt": "Adopt: start from existing code",
    "specify": "Specify: describe a feature",
    "clarify": "Clarify: remove doubts",
    "design-system": "Design system: look and feel",
    "design": "Design: screens of a feature",
    "plan": "Plan: how it will be built",
    "tasks": "Tasks: small steps",
    "analyze": "Analyze: check the documents",
    "implement": "Implement: build one task",
    "verify": "Verify: independent check",
    "fix": "Fix: small changes",
    "next": "Next: where are we?",
}

# Manual groups: (menu title, url slug, intro, first and last section number in the manual)
MANUAL_GROUPS = [
    ("Getting started", "getting-started", "What NodFirst is, how you can work with it, and how to set up your first project.", 0, 4),
    ("Working with NodFirst", "working-with-nodfirst", "Your role, the cycle of a feature, small fixes, changes, and what to do when something goes wrong.", 5, 13),
    ("Appendices", "appendices", "Glossary, checklists, the list of commands, where everything is, and the status of each part of the kit.", 14, 99),
]
# Menu titles that would clash with other pages of the site.
MANUAL_TITLES = {"Examples": "Worked examples", "Commands": "Commands at a glance"}

PAGES = {}      # site url -> True (for link checking)
SOURCE_TO_URL = {}  # repository path -> site url


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def front_matter(**kw):
    lines = ["---"]
    for k, v in kw.items():
        if v is None:
            continue
        if isinstance(v, bool):
            v = "true" if v else "false"
        elif isinstance(v, str):
            v = '"' + v.replace('"', '\\"') + '"'
        lines.append(f"{k}: {v}")
    lines.append("---\n")
    return "\n".join(lines)


TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
LABEL_LINE = re.compile(r"^\*\*[^*\n]+[.:]\*\*(\s|$)")


def space_blocks(text):
    """Add the blank lines kramdown (GitHub Pages) needs and GitHub does not.

    Only whitespace changes; the repository files stay as they are. Outside code fences:
    a blank line before a table that follows a heading or a paragraph line; between
    consecutive "**Label:** ..." or "**Label.** ..." lines and consecutive blockquote lines, so each stays its
    own line instead of being joined into one paragraph.
    """
    lines = text.split("\n")
    out, fence = [], None
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        marker = stripped[:3]
        if marker in ("```", "~~~"):
            ticks = len(stripped) - len(stripped.lstrip(marker[0]))
            if fence is None:
                fence = (marker[0], ticks)
            elif marker[0] == fence[0] and ticks >= fence[1] and not stripped.strip(marker[0]).strip():
                fence = None
            out.append(line)
            continue
        prev = out[-1] if out else ""
        if fence is None and prev.strip():
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if TABLE_ROW.match(line) and TABLE_SEP.match(nxt) and not TABLE_ROW.match(prev):
                out.append("")
            elif LABEL_LINE.match(line) and LABEL_LINE.match(prev):
                out.append("")
            elif line.startswith(">") and prev.startswith(">") and line.strip() != ">" and prev.strip() != ">":
                out.append(">")
        out.append(line)
    return "\n".join(out)


def write_page(url, body, **fm):
    """url like '/manual/part-1/'. Writes OUT/<url>/index.md."""
    PAGES[url] = True
    path = OUT / url.strip("/") / "index.md" if url != "/" else OUT / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(front_matter(permalink=url, **fm) + "\n" + space_blocks(body.strip()) + "\n", encoding="utf-8")


def rewrite_links(text, source):
    """Rewrite relative Markdown links and HTML src/srcset from a repository file."""
    base = (ROOT / source).parent

    def target(href):
        if re.match(r"^[a-z]+:|^#|^mailto:", href):
            return href
        path, _, anchor = href.partition("#")
        resolved = (base / path).resolve()
        rel = resolved.relative_to(ROOT).as_posix() if resolved.is_relative_to(ROOT) else path
        if rel.startswith("media/"):
            return f"{BASE}/assets/images/{pathlib.PurePosixPath(rel).name}"
        key = rel.rstrip("/")
        if key in SOURCE_TO_URL:
            return f"{BASE}{SOURCE_TO_URL[key]}" + (f"#{anchor}" if anchor else "")
        kind = "tree" if resolved.is_dir() else "blob"
        return f"{REPO_URL}/{kind}/main/{key}" + (f"#{anchor}" if anchor else "")

    def link(m):
        label, href = m.group(1), m.group(2)
        # A link shown as a kit file path (e.g. [`kit/nodfirst/manual.md`](...)) opens that file on GitHub.
        if label.startswith("`") and href.startswith("kit/") and not href.endswith("/"):
            return f"[{label}]({REPO_URL}/blob/main/{href})"
        return f"[{label}]({target(href)})"

    text = re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", link, text)
    text = re.sub(r'(src|srcset)="([^"]+)"', lambda m: f'{m.group(1)}="{target(m.group(2))}"', text)
    return text


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def split_sections(text, level):
    """Split Markdown text on headings of the given level (outside code fences)."""
    marker = "#" * level + " "
    parts, current, title, fence = [], [], None, False
    for line in text.splitlines():
        if line.startswith("```"):
            fence = not fence
        if not fence and line.startswith(marker):
            parts.append((title, "\n".join(current)))
            title, current = line[len(marker):].strip(), [line]
        else:
            current.append(line)
    parts.append((title, "\n".join(current)))
    return parts


def drop_rules(text):
    """Remove leading/trailing horizontal rules left by splitting."""
    return re.sub(r"(^\s*---\s*\n)|(\n\s*---\s*$)", "", text.strip()).strip()


def as_code(text, lang="markdown"):
    return f"````{lang}\n{text.rstrip()}\n````"


# ---------------------------------------------------------------- mapping first (links need it)
def plan_urls():
    SOURCE_TO_URL.update({
        "README.md": "/",
        "kit/nodfirst/manual.md": "/manual/",
        "kit/nodfirst/constitution.md": "/reference/constitution/",
        "kit/nodfirst/playbooks": "/reference/playbooks/",
        "kit/nodfirst/modules": "/reference/modules/",
        "kit/nodfirst/modules/README.md": "/reference/modules/",
        "kit/nodfirst/templates": "/reference/templates/",
        "kit/nodfirst/adapters/README.md": "/reference/command-files/",
        "kit/project/profile.md": "/reference/templates/profile/",
        "examples": "/examples/",
        "examples/README.md": "/examples/",
        "examples/shortz": "/examples/shortz/",
        "examples/shortz/README.md": "/examples/shortz/",
        "examples/shortz/project/profile.md": "/examples/shortz/profile/",
        "examples/shortz/project/roadmap.md": "/examples/shortz/roadmap/",
        "examples/shortz/specs/001-shorten-redirect-manage-by-token/spec.md": "/examples/shortz/spec/",
        "examples/shortz/specs/001-shorten-redirect-manage-by-token/design.md": "/examples/shortz/design/",
        "examples/shortz/specs/001-shorten-redirect-manage-by-token/plan.md": "/examples/shortz/plan/",
        "examples/shortz/specs/001-shorten-redirect-manage-by-token/tasks.md": "/examples/shortz/tasks/",
        "examples/shortz/specs/001-shorten-redirect-manage-by-token/analysis.md": "/examples/shortz/analysis/",
        "examples/shortz/specs/001-shorten-redirect-manage-by-token/verification.md": "/examples/shortz/verification/",
        "examples/shortz/specs/001-shorten-redirect-manage-by-token/verification-prep.md": "/examples/shortz/verification-prep/",
        "examples/shortz/specs/001-shorten-redirect-manage-by-token/keyboard-check.md": "/examples/shortz/keyboard-check/",
        "examples/book-club": "/examples/book-club/",
        "examples/book-club/README.md": "/examples/book-club/",
        "examples/book-club/review.md": "/examples/book-club/review/",
        "examples/book-club/specs/001-book-lending/spec.md": "/examples/book-club/spec/",
        "examples/book-club/project/profile.md": "/examples/book-club/profile/",
        "examples/book-club/project/roadmap.md": "/examples/book-club/roadmap/",
        "CHANGELOG.md": "/changelog/",
        "ROADMAP.md": "/roadmap/",
        "CONTRIBUTING.md": "/contributing/",
    })
    for p in sorted((ROOT / "kit/nodfirst/playbooks").glob("*.md")):
        SOURCE_TO_URL[f"kit/nodfirst/playbooks/{p.name}"] = f"/reference/playbooks/{p.stem}/"
    for p in sorted((ROOT / "kit/nodfirst/modules").glob("*.md")):
        if p.name != "README.md":
            SOURCE_TO_URL[f"kit/nodfirst/modules/{p.name}"] = f"/reference/modules/{p.stem}/"
    for p in sorted((ROOT / "kit/nodfirst/templates").glob("*.md")):
        SOURCE_TO_URL[f"kit/nodfirst/templates/{p.name}"] = f"/reference/templates/{p.stem}/"


# ---------------------------------------------------------------- pages
def home():
    text = read("README.md")
    sections = split_sections(text, 2)
    head, rest = sections[0][1], sections[1:]
    keep = [body for title, body in rest if title not in ("NodFirst and GitHub Spec Kit", "What makes it different", "Repository layout")]
    links = (
        "\n## Where to go next\n\n"
        f"- New here? Read [The idea in five minutes]({BASE}/manual/the-idea-in-five-minutes/), then [Starting]({BASE}/manual/starting/).\n"
        f"- See [what the documents look like]({BASE}/examples/), and how to review a first draft.\n"
        f"- Look up a [command]({BASE}/reference/playbooks/) or the [rules]({BASE}/reference/constitution/).\n"
        f"- Compare with [GitHub Spec Kit]({BASE}/compare/).\n"
    )
    head = re.sub(r"\s*<p><a href=\"https://kaylit\.github\.io/nodfirst/\">.*?</a></p>", "", head)  # the site links to itself
    head = re.sub(r"\s*<source media=\"\(prefers-color-scheme: dark\)\"[^>]*>", "", head)  # the site is always light
    body = rewrite_links(head + "\n\n" + "\n\n".join(keep), "README.md") + links
    write_page("/", body, title="Home", layout="home", nav_order=1, description="Nothing gets built until you say yes.")


def compare():
    sections = dict(split_sections(read("README.md"), 2))
    body = "# Compare\n\n" + "\n\n".join(
        sections[t].replace("## ", "## ", 1) for t in ("What makes it different", "NodFirst and GitHub Spec Kit") if t in sections
    )
    write_page("/compare/", rewrite_links(body, "README.md"), title="Compare with Spec Kit", nav_order=5)


def manual():
    text = read("kit/nodfirst/manual.md")
    pages = [(t_, b) for t_, b in split_sections(text, 1) if t_]
    intro_title, intro_body = pages[0]
    sections = pages[1:]
    toc = []
    for g_index, (g_title, g_slug, g_intro, first, last) in enumerate(MANUAL_GROUPS, 1):
        toc += ["", f"### {g_title}", ""]
        write_page(f"/manual/{g_slug}/", f"# {g_title}\n\n{g_intro}\n",
                   title=g_title, parent="Manual", nav_order=g_index, has_children=True)
        for order, (title, body) in enumerate(sections[first:last + 1], 1):
            short = re.sub(r"^(Part \d+|Appendix [A-Z]) — ", "", title)
            url = f"/manual/{slug(short)}/"
            toc.append(f"- [{title}]({BASE}{url})")
            write_page(url, rewrite_links(drop_rules(body), "kit/nodfirst/manual.md"),
                       title=MANUAL_TITLES.get(short, short), parent=g_title, grand_parent="Manual", nav_order=order)
    body = rewrite_links(drop_rules(intro_body), "kit/nodfirst/manual.md") + "\n\n## Contents\n" + "\n".join(toc)
    write_page("/manual/", body, title="Manual", nav_order=2, has_children=True, has_toc=False)


def reference():
    write_page("/reference/",
               "# Reference\n\nThe kit's own files, as they are in `kit/nodfirst/`. Agents read these; you can read them too.\n",
               title="Reference", nav_order=3, has_children=True)
    write_page("/reference/constitution/", rewrite_links(read("kit/nodfirst/constitution.md"), "kit/nodfirst/constitution.md"),
               title="Constitution", parent="Reference", nav_order=1)

    # Playbooks: an index table from the command list, then one page each.
    rows = ["| Step | Command | What it does |", "|---|---|---|"]
    for name, (desc, _hint) in COMMANDS.items():
        rows.append(f"| [{LABELS[name]}]({BASE}/reference/playbooks/{name}/) | `/nodfirst-{name}` | {desc} |")
    write_page("/reference/playbooks/",
               "# Playbooks and commands\n\nEach phase has one playbook in `nodfirst/playbooks/`. After `init`, your coding tool knows the commands below (in Codex, type `$` instead of `/`).\n\n" + "\n".join(rows),
               title="Playbooks", parent="Reference", nav_order=2, has_children=True, has_toc=False)
    for i, name in enumerate(COMMANDS, 1):
        src = f"kit/nodfirst/playbooks/{name}.md"
        body = read(src)
        first, _, rest = body.partition("\n")
        intro = (f"\n\n**Command:** `/nodfirst-{name}` (in Codex: `$nodfirst-{name}`). "
                 f"Without commands, tell your agent: follow `nodfirst/playbooks/{name}.md`.\n")
        write_page(f"/reference/playbooks/{name}/", rewrite_links(first + intro + rest, src),
                   title=LABELS[name], parent="Playbooks", grand_parent="Reference", nav_order=i)

    write_page("/reference/modules/", rewrite_links(read("kit/nodfirst/modules/README.md"), "kit/nodfirst/modules/README.md"),
               title="Modules", parent="Reference", nav_order=3, has_children=True)
    for i, p in enumerate(sorted((ROOT / "kit/nodfirst/modules").glob("*.md")), 1):
        if p.name == "README.md":
            continue
        src = f"kit/nodfirst/modules/{p.name}"
        title = read(src).splitlines()[0].replace("# Module: ", "")
        write_page(f"/reference/modules/{p.stem}/", rewrite_links(read(src), src),
                   title=title, parent="Modules", grand_parent="Reference", nav_order=i)

    write_page("/reference/templates/",
               "# Templates\n\nThe empty forms agents fill in. They are shown as plain text, so you can see the guidance comments the agent reads.\n",
               title="Templates", parent="Reference", nav_order=4, has_children=True)
    templates = [("kit/project/profile.md", "profile", "Project profile")] + [
        (f"kit/nodfirst/templates/{p.name}", p.stem, p.stem.replace("-template", "").capitalize() + " template")
        for p in sorted((ROOT / "kit/nodfirst/templates").glob("*.md"))
    ]
    for i, (src, stem, title) in enumerate(templates, 1):
        write_page(f"/reference/templates/{stem}/", f"# {title}\n\nSource: `{src.replace('kit/', '')}`\n\n" + as_code(read(src)),
                   title=title, parent="Templates", grand_parent="Reference", nav_order=i)

    write_page("/reference/command-files/", rewrite_links(read("kit/nodfirst/adapters/README.md"), "kit/nodfirst/adapters/README.md"),
               title="Command files", parent="Reference", nav_order=5)


def examples():
    write_page("/examples/", rewrite_links(read("examples/README.md"), "examples/README.md"),
               title="Examples", nav_order=4, has_children=True)
    write_page("/examples/shortz/", rewrite_links(read("examples/shortz/README.md"), "examples/shortz/README.md"),
               title="Shortz (real run)", parent="Examples", nav_order=1, has_children=True)
    shortz = [
        ("examples/shortz/project/profile.md", "/examples/shortz/profile/", "Profile"),
        ("examples/shortz/project/roadmap.md", "/examples/shortz/roadmap/", "Roadmap"),
        ("examples/shortz/specs/001-shorten-redirect-manage-by-token/spec.md", "/examples/shortz/spec/", "Spec 001"),
        ("examples/shortz/specs/001-shorten-redirect-manage-by-token/design.md", "/examples/shortz/design/", "Design 001"),
        ("examples/shortz/specs/001-shorten-redirect-manage-by-token/plan.md", "/examples/shortz/plan/", "Plan 001"),
        ("examples/shortz/specs/001-shorten-redirect-manage-by-token/tasks.md", "/examples/shortz/tasks/", "Tasks 001"),
        ("examples/shortz/specs/001-shorten-redirect-manage-by-token/analysis.md", "/examples/shortz/analysis/", "Analysis 001"),
        ("examples/shortz/specs/001-shorten-redirect-manage-by-token/verification.md", "/examples/shortz/verification/", "Verification 001"),
        ("examples/shortz/specs/001-shorten-redirect-manage-by-token/verification-prep.md", "/examples/shortz/verification-prep/", "Production smoke note"),
        ("examples/shortz/specs/001-shorten-redirect-manage-by-token/keyboard-check.md", "/examples/shortz/keyboard-check/", "Keyboard check note"),
    ]
    for i, (src, url, title) in enumerate(shortz, 1):
        write_page(url, rewrite_links(read(src), src), title=title, parent="Shortz (real run)", grand_parent="Examples", nav_order=i)
    write_page("/examples/book-club/", rewrite_links(read("examples/book-club/README.md"), "examples/book-club/README.md"),
               title="Book club", parent="Examples", nav_order=2, has_children=True)
    items = [
        ("examples/book-club/project/profile.md", "/examples/book-club/profile/", "Profile (draft)"),
        ("examples/book-club/project/roadmap.md", "/examples/book-club/roadmap/", "Roadmap (draft)"),
        ("examples/book-club/specs/001-book-lending/spec.md", "/examples/book-club/spec/", "Spec 001 (draft)"),
        ("examples/book-club/review.md", "/examples/book-club/review/", "Review of the draft"),
    ]
    for i, (src, url, title) in enumerate(items, 1):
        write_page(url, rewrite_links(read(src), src), title=title, parent="Book club", grand_parent="Examples", nav_order=i)


def project_pages():
    for i, (src, url, title) in enumerate([
        ("CHANGELOG.md", "/changelog/", "Changelog"),
        ("ROADMAP.md", "/roadmap/", "Roadmap"),
        ("CONTRIBUTING.md", "/contributing/", "Contributing"),
    ], 6):
        write_page(url, rewrite_links(read(src), src), title=title, nav_order=i)


def check_links():
    bad = []
    for md in OUT.rglob("*.md"):
        for m in re.finditer(r"\{\{ site\.baseurl \}\}(/[^)\s\"#]*)", md.read_text(encoding="utf-8")):
            url = m.group(1)
            if url.startswith("/assets/"):
                if not (OUT / url.lstrip("/")).exists():
                    bad.append((md, url))
            elif url not in PAGES:
                bad.append((md, url))
    for md, url in bad:
        print(f"BROKEN LINK in {md.relative_to(OUT)}: {url}")
    return not bad


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    shutil.copytree(ROOT / "site", OUT)
    images = OUT / "assets" / "images"
    images.mkdir(parents=True, exist_ok=True)
    for f in (ROOT / "media").iterdir():
        shutil.copy(f, images / f.name)
    plan_urls()
    home(); manual(); reference(); examples(); compare(); project_pages()
    ok = check_links()
    print(f"{len(PAGES)} pages written to {OUT.relative_to(ROOT)}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
