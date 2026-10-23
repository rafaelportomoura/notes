# Lessons

Hierarchical, append-only memory for agents working in this repo.

- Layout: `SUMMARY.md` (root digest), `_inbox/` (new lessons) and `nodes/` (all topics, recursively).
- Every directory under `nodes/` is a **node**: a capped `SUMMARY.md` + loose lesson files + child nodes.
- Agents read `SUMMARY.md` at the root (auto-loaded via `CLAUDE.md`) and descend only when needed.
- New lessons go to `_inbox/`, then are routed and folded into topics.
- **Nothing is ever deleted.** Folding moves files deeper; old lessons are marked `superseded`, not removed.

Run `python3 .claude/skills/lessons/scripts/lessons.py check` to see caps and what needs consolidation.
