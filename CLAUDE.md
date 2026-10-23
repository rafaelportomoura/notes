# notes

Project to learn how to read, take notes and remember, so the notes can be found and used later. Goal: a study practice that is easy to keep and never becomes a burden.

## Language rules

1. **Folder and file names are always in English** (kebab-case for docs, e.g. `one-vault-or-many.md`; Obsidian template files may use `Capitalized-Words.md`).
2. **Written content (docs, notes, templates text) may be in Portuguese.**
3. **Code is always in English**: identifiers, comments, commit messages, docstrings and error messages.
4. Frontmatter/property keys and values are English (`type`, `area`, `status`; e.g. `type: source`).

## Layout

This repository **is** the Obsidian vault (vault root = repo root).

- `README.md`: entry point
- `00-Inbox/`, `10-Journal/`, `20-Projects/`, `30-Areas/`, `40-Sources/`, `50-Permanent-Notes/`, `90-Templates/`: the vault
- `99-SYSTEM/`: `decisions/`, `method/` (reading, note-taking, remembering, routine, sustainability) and `plan-30-days.md`
- `.obsidian/`: tracked settings (see `.gitignore`)
- `.claude/`: agent config and lessons

## Working principle

Keep it small. Complexity cap: 8 root folders, 3 properties, 3 templates in use (see `99-SYSTEM/method/sustainability.md`). When adding something, remove something else.

## Lessons (agent memory)

Consolidated lessons are auto-loaded below (capped at 40 lines / 3000 bytes). Go deeper only when the task touches a topic: open that topic's `SUMMARY.md`, then individual lesson files via the `→ <id>` references.

@.claude/lessons/SUMMARY.md

- Capture, route and fold lessons with the `lessons` skill (`.claude/skills/lessons/SKILL.md`).
- **Never delete lessons.** Folding moves files deeper; changed rules are superseded, not erased.
- Before finishing a task where you were corrected or learned something non-obvious, capture at most 3 lessons.
