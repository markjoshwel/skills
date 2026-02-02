---
name: git-majo
description: Git workflow standards for Mark's projects. Use when making commits, creating branches, or managing git history. Covers commit message format, auto-commit policy, and push behavior.
license: Unlicense OR 0BSD
metadata:
  author: Mark Joshwel <mark@joshwel.co>
  version: "2026.2.2"
---

# Git Workflow Standards (Mark)

Git standards for commit messages, auto-commits, and repository management.

## Auto-Commit Policy

**ALWAYS commit after every prompt unless explicitly told NOT to**

This allows tracking how many LLM prompts a feature or bug fix required.

### Commit Workflow

After completing work on a prompt:

```bash
# 1. Check what changed
git status
git diff

# 2. Stage changes
git add <files>

# 3. Commit with descriptive message (see format below)
git commit -m "type(component): description"

# 4. DO NOT push (unless explicitly told to)
```

## Commit Message Format

Use conventional commits format:

```
<type>[(<component>)]: <description>
```

### Types

- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation changes
- `style` - Code style/formatting (no logic change)
- `refactor` - Code refactoring
- `perf` - Performance improvements
- `test` - Adding or fixing tests
- `chore` - Maintenance tasks, dependencies
- `ci` - CI/CD changes
- `meta` - Repository/meta changes (init, config, etc.)

### Examples

```bash
# Simple changes
git commit -m "meta: init files"
git commit -m "feat(cli): add verbose flag"
git commit -m "fix(parser): handle empty input"

# With component
git commit -m "ci(lint): add basedpyright check"
git commit -m "docs(readme): update installation steps"
git commit -m "refactor(utils): extract helper functions"
```

## Including Original Prompt

**Commit description should include the original prompt** (shortened/redacted if lengthy):

```bash
# For short prompts
git commit -m "feat(api): add user authentication endpoint" -m "Prompt: add login with jwt tokens"

# For longer prompts (redact verbose parts)
git commit -m "fix(parser): handle edge case in csv parsing" -m "Prompt: fix the issue where empty lines cause crash [diagnostic output redacted]"
```

**Redaction guidelines**:
- Keep the core request/intent
- Remove large pasted diagnostic output
- Remove excessive context dumps
- Keep it readable in one line

## Push Policy

**NEVER auto-push unless explicitly told TO do so**

Default behavior: commit locally only.

When told to push:
```bash
# Push current branch
git push

# Push specific branch
git push origin <branch-name>
```

## Commit Frequency

**One commit per prompt** (unless the prompt specifically asks for multiple commits):

```
User: "Add user authentication"
→ Do work
→ git commit -m "feat(auth): add user authentication" -m "Prompt: Add user authentication"

User: "Now add password reset"
→ Do work
→ git commit -m "feat(auth): add password reset" -m "Prompt: add password reset"
```

## Branch Naming

If creating branches:
- `feature/<name>` - New features
- `fix/<name>` - Bug fixes
- `docs/<name>` - Documentation
- `refactor/<name>` - Refactoring

## Checking Past Commits

To understand commit style from history:
```bash
# View recent commits
git log --oneline -20

# View commit with message
git log -1
```

Match the style of existing commits in the repository.

## Integration

This skill extends `majo-standards`. Always ensure `majo-standards` is loaded for:
- AGENTS.md maintenance
- Universal code principles
- Documentation policies

Works alongside:
- `python-majo` — For Python-specific development and commits
- `js-bun-majo` — For JavaScript/Bun development and commits
- `shell-majo` — For shell scripting and commits
- `docs-majo` — For documentation commits
- `task-planning-majo` — For complex multi-step work
- `windows-majo` — For git operations on Windows
