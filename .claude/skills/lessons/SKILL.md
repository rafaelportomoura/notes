---
name: lessons
description: Capture, read and consolidate this project's lessons learned in a capped, hierarchical tree under .claude/lessons. Use when the user corrects you, when you make a non-obvious discovery or confirm a non-obvious approach, when asked to record/consolidate/fold lessons, or when the check script reports TODOs.
---

# Lessons

A recursive, append-only memory. Cost to read stays constant; detail stays reachable.

## Tree model

```
.claude/lessons/
  SUMMARY.md            root digest (the ONLY file loaded every session)
  README.md
  _inbox/               new raw lessons, not yet routed
  nodes/                container for all topics (no SUMMARY of its own)
    <topic>/
      SUMMARY.md        capped digest of everything below
      <date>-<slug>.md  loose lessons (immutable bodies)
      <subtopic>/       same shape, recursively
```

The root node is `lessons/` itself (its `SUMMARY.md`); its children are the directories under `nodes/`. Only `SUMMARY.md`, `README.md`, `nodes/` and `_inbox/` may sit at the `lessons/` root.

A **node** is a directory with a `SUMMARY.md`. A **lesson** is any other `*.md` (except `README.md`). Topic = path relative to `nodes/`, e.g. `tooling/obsidian`. Links in the root summary look like `nodes/tooling/SUMMARY.md`; deeper summaries link to `child/SUMMARY.md`.

## Caps (enforced by `lessons.py check`)

| What | Cap |
|---|---|
| `SUMMARY.md` | 40 lines and 3000 bytes |
| Child directories per node | 12 |
| Loose lessons per node | 8 |
| Lessons in `_inbox/` | 5 |
| A lesson file | 25 lines |

At the root, the cap is what keeps the always-loaded context small. Do not raise caps; fold instead.

## Reading (default: cheap)

1. Rely on the root `SUMMARY.md` already in context.
2. If the task touches a topic, open that topic's `SUMMARY.md`. Repeat down the tree only while relevant.
3. Each rule in a summary ends with a reference (`→ <lesson-id>`). Open the lesson file only if you need the context, evidence or "why".
4. Never read the whole tree.

## Capturing

Capture when: the user corrects you or confirms a non-obvious choice; you hit a failure whose cause was not obvious; you find something that would save the next agent time and is **not** already in code, git history or `CLAUDE.md`.

Do not capture: task progress, one-off facts, anything derivable from the repo.

Steps:
1. `python3 .claude/skills/lessons/scripts/lessons.py new <slug> --hint "<topic/path>"` creates a file in `_inbox/`.
2. Fill it in. Imperative title; Context, Lesson, Why, How to apply, Evidence. Keep it short.
3. At most 3 new lessons per session.

## Routing and folding (consolidation)

Run `lessons.py check`. For each `TODO` it reports:

**Route** (inbox not empty): move each inbox lesson into the best-fitting topic directory under `nodes/` with `git mv` (or `mv`). Create the topic and its `SUMMARY.md` if it does not exist. Add the lesson's rule to that topic's summary.

**Fold** (node over cap, too many loose lessons):
1. Cluster the loose lessons by theme.
2. Create a subdirectory per cluster, move the files in, and write its `SUMMARY.md` (rules distilled, each with `→ <lesson-id>`).
3. In the parent summary replace those rules with one line per child: `- [child](child/SUMMARY.md): one-line digest`.
4. Re-check the parent. If it is still over cap, compress further: keep only the rules with the highest importance and push the rest down (they already live in the child summaries).
5. Repeat upwards until the root is within cap.

**Split** (too many child directories): group related children under a new intermediate node.

Importance when compressing = cost if violated x how often it applies x `hits` x recency. Rules for common, expensive mistakes stay near the root.

## Immutability

- A lesson's body is never edited. Only frontmatter `hits`, `status` and `superseded_by` may change.
- To change a rule: write a new lesson with `supersedes: [old-id]`, set the old one to `status: superseded` and `superseded_by: new-id`, and update the summaries. The old file stays.
- **Never delete** lessons or summaries' history. Folding only moves files deeper. Git history is the backup.

## Lesson file format

```markdown
---
id: 2026-10-23-short-slug      # must equal the file name without .md
date: 2026-10-23
status: active                 # active | superseded
supersedes: []
superseded_by:
confidence: medium             # low | medium | high
hits: 1                        # bump when the lesson is confirmed again
topic_hint: tooling/obsidian   # inbox only, optional
---
# Imperative rule as the title
**Context:** what was happening.
**Lesson:** what to do or avoid.
**Why:** the reason (incident, preference, constraint).
**How to apply:** when and where this kicks in.
**Evidence:** file, commit, error text.
```

## Summary file format

```markdown
---
node: tooling/obsidian
lessons: 7        # all descendant lessons
updated: 2026-10-23
---
# Obsidian
## Rules
- Rule in one line. (→ 2026-10-23-short-slug)
## Children
- [templates](templates/SUMMARY.md): one-line digest   # in the root summary: nodes/templates/SUMMARY.md
## Open questions
```

## Command reference

```
python3 .claude/skills/lessons/scripts/lessons.py check [--strict]
python3 .claude/skills/lessons/scripts/lessons.py new <slug> [--hint topic/path]
```
