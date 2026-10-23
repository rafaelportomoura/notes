#!/usr/bin/env python3
"""Validate and scaffold the hierarchical lessons tree in .claude/lessons.

Commands:
  check [--strict]   Validate structure and report consolidation TODOs.
  new SLUG [--hint]  Create a lesson skeleton in _inbox/.

Exit codes: 0 ok, 1 structural errors (or TODOs with --strict).
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

# <repo>/.claude/skills/lessons/scripts/lessons.py -> <repo>/.claude
CLAUDE_DIR = Path(__file__).resolve().parents[3]
LESSONS = CLAUDE_DIR / "lessons"
NODES = LESSONS / "nodes"  # container for topic directories; has no SUMMARY of its own

MAX_SUMMARY_LINES = 40
MAX_SUMMARY_BYTES = 3000
MAX_CHILD_DIRS = 12
MAX_LOOSE_LESSONS = 8
MAX_INBOX = 5
MAX_LESSON_LINES = 25

INBOX = "_inbox"
NODES_DIR = "nodes"
SUMMARY = "SUMMARY.md"
IGNORED_FILES = {SUMMARY, "README.md"}
REQUIRED_KEYS = ("id", "date", "status", "confidence", "hits")
STATUSES = {"active", "superseded"}
CONFIDENCE = {"low", "medium", "high"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")

TEMPLATE = """---
id: {id}
date: {date}
status: active
supersedes: []
superseded_by:
confidence: medium
hits: 1
topic_hint: {hint}
---
# {title}
**Context:**
**Lesson:**
**Why:**
**How to apply:**
**Evidence:**
"""


def parse_frontmatter(text):
    """Return a dict of top-level `key: value` pairs from a leading --- block."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    data = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return data
        match = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*(?:#.*)?$", line)
        if match:
            data[match.group(1)] = match.group(2)
    return None  # unterminated block


def parse_list(value):
    inner = value.strip().strip("[]")
    return [item.strip() for item in inner.split(",") if item.strip()]


def lesson_files(directory):
    return sorted(
        p for p in directory.glob("*.md") if p.name not in IGNORED_FILES
    )


def child_dirs(directory):
    """Child nodes of a node. The root's children live under nodes/."""
    base = NODES if directory == LESSONS else directory
    if not base.is_dir():
        return []
    return sorted(
        p for p in base.iterdir()
        if p.is_dir() and not p.name.startswith(".")
    )


def check(strict):
    errors, todos = [], []
    ids = {}
    supersedes = []
    total = 0
    max_depth = 0

    if not LESSONS.is_dir():
        print(f"ERROR: {LESSONS} not found")
        return 1

    if not NODES.is_dir():
        errors.append(f"missing {NODES_DIR}/ directory")

    # Top level may only hold SUMMARY.md, README.md, nodes/ and _inbox/.
    allowed = IGNORED_FILES | {NODES_DIR, INBOX}
    for entry in sorted(LESSONS.iterdir()):
        if entry.name.startswith(".") or entry.name in allowed:
            continue
        errors.append(f"{entry.name}: not allowed at lessons/ root (use {NODES_DIR}/ or {INBOX}/)")

    nodes = [LESSONS] + (
        [
            p for p in NODES.rglob("*")
            if p.is_dir() and not any(
                part.startswith(".") for part in p.relative_to(NODES).parts
            )
        ]
        if NODES.is_dir()
        else []
    )

    for node in nodes:
        rel = "." if node == LESSONS else node.relative_to(NODES).as_posix()
        label = rel
        max_depth = max(max_depth, 0 if rel == "." else len(Path(rel).parts))
        summary = node / SUMMARY
        if not summary.is_file():
            errors.append(f"{label}: missing {SUMMARY}")
            continue

        text = summary.read_text(encoding="utf-8")
        n_lines, n_bytes = len(text.splitlines()), len(text.encode("utf-8"))
        if n_lines > MAX_SUMMARY_LINES or n_bytes > MAX_SUMMARY_BYTES:
            todos.append(
                f"FOLD {label}: summary {n_lines} lines/{n_bytes} bytes "
                f"(cap {MAX_SUMMARY_LINES}/{MAX_SUMMARY_BYTES}); compress and push detail down"
            )

        for target in LINK_RE.findall(text):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            path = (node / target.split("#")[0]).resolve()
            if not path.exists():
                errors.append(f"{label}/{SUMMARY}: broken link -> {target}")

        children = child_dirs(node)
        if len(children) > MAX_CHILD_DIRS:
            todos.append(
                f"SPLIT {label}: {len(children)} child dirs (cap {MAX_CHILD_DIRS}); "
                "group related children under a new node"
            )
        prefix = f"{NODES_DIR}/" if node == LESSONS else ""
        for child in children:
            if f"{prefix}{child.name}/{SUMMARY}" not in text:
                todos.append(f"LINK {label}: summary does not link to child '{child.name}'")

        loose = [] if node == LESSONS else lesson_files(node)
        if len(loose) > MAX_LOOSE_LESSONS:
            todos.append(
                f"FOLD {label}: {len(loose)} loose lessons (cap {MAX_LOOSE_LESSONS}); "
                "cluster them into subtopics"
            )

    all_lessons = [
        p for p in LESSONS.rglob("*.md")
        if p.name not in IGNORED_FILES and p.parent != LESSONS
    ]
    for path in all_lessons:
        total += 1
        rel = path.relative_to(LESSONS).as_posix()
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        if meta is None:
            errors.append(f"{rel}: missing or unterminated frontmatter")
            continue
        for key in REQUIRED_KEYS:
            if not meta.get(key):
                errors.append(f"{rel}: missing frontmatter key '{key}'")
        if meta.get("id") and meta["id"] != path.stem:
            errors.append(f"{rel}: id '{meta['id']}' != file name '{path.stem}'")
        if meta.get("status") and meta["status"] not in STATUSES:
            errors.append(f"{rel}: invalid status '{meta['status']}'")
        if meta.get("confidence") and meta["confidence"] not in CONFIDENCE:
            errors.append(f"{rel}: invalid confidence '{meta['confidence']}'")
        if len(text.splitlines()) > MAX_LESSON_LINES:
            errors.append(f"{rel}: longer than {MAX_LESSON_LINES} lines")
        if meta.get("id"):
            if meta["id"] in ids:
                errors.append(f"{rel}: duplicate id (also {ids[meta['id']]})")
            ids[meta["id"]] = rel
        for old in parse_list(meta.get("supersedes", "")):
            supersedes.append((rel, old))

    for rel, old in supersedes:
        if old not in ids:
            errors.append(f"{rel}: supersedes unknown id '{old}'")

    inbox = LESSONS / INBOX
    pending = lesson_files(inbox) if inbox.is_dir() else []
    if pending:
        level = "ROUTE" if len(pending) > MAX_INBOX else "route"
        todos.append(
            f"{level} _inbox: {len(pending)} lesson(s) waiting "
            f"(cap {MAX_INBOX}); move into topics and update summaries"
        )

    root_text = (LESSONS / SUMMARY).read_text(encoding="utf-8") if (LESSONS / SUMMARY).is_file() else ""
    print(
        f"lessons={total} nodes={len(nodes)} depth={max_depth} "
        f"root={len(root_text.encode('utf-8'))}B/{MAX_SUMMARY_BYTES}B"
    )
    for item in errors:
        print(f"ERROR: {item}")
    for item in todos:
        print(f"TODO: {item}")
    if not errors and not todos:
        print("OK")
    if errors or (strict and todos):
        return 1
    return 0


def new(slug, hint):
    if not SLUG_RE.match(slug):
        print("ERROR: slug must be kebab-case (a-z, 0-9, hyphens)")
        return 1
    today = datetime.date.today().isoformat()
    lesson_id = f"{today}-{slug}"
    inbox = LESSONS / INBOX
    inbox.mkdir(parents=True, exist_ok=True)
    path = inbox / f"{lesson_id}.md"
    if path.exists():
        print(f"ERROR: {path} already exists")
        return 1
    title = slug.replace("-", " ").capitalize()
    path.write_text(
        TEMPLATE.format(id=lesson_id, date=today, hint=hint or "", title=title),
        encoding="utf-8",
    )
    print(path.relative_to(CLAUDE_DIR.parent).as_posix())
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_check = sub.add_parser("check")
    p_check.add_argument("--strict", action="store_true", help="exit 1 on TODOs too")
    p_new = sub.add_parser("new")
    p_new.add_argument("slug")
    p_new.add_argument("--hint", default="")
    args = parser.parse_args()
    sys.exit(check(args.strict) if args.cmd == "check" else new(args.slug, args.hint))


if __name__ == "__main__":
    main()
