---
name: majo-standards
description: Mark's core development standards and conventions. Use for any code generation to ensure consistency with maintainable, readable code that follows established patterns. Covers universal principles like code style, documentation policies, and AGENTS.md maintenance.
license: Unlicense
metadata:
  author: mark@joshwel.co
  version: "2026.2.2"
---

# Mark's Development Standards

Core development standards that apply across all languages and projects.

## Universal Code Principles

### Code Quality

**Maintainability First**
- Generated code should be maintainable through readability and/or modularity
- No undue pre-optimization beyond existing complexity in the codebase
- Follow conventions of previous or attached files

**Self-Documenting Code**
- Code should not require extensive comments
- Variable names and expressions should visibly describe the logic
- Naming should be apt yet visible in describing implemented logic

**Diagnostic Cleanliness**
- Generated code should not have diagnostic errors or warnings
- Suppress diagnostics only when reasonable (e.g., external package missing type stubs)

### Code Organization

**Section Comments**
Use clear section comments to group related code:
```python
# constants
VERSION: Final[str] = "1.0.0"
DEBUG: Final[bool] = False

# configuration
config = load_config()

# main logic
result = process(config)
```

**Defensive Programming**
- Check preconditions before operations
- Validate inputs early
- Provide descriptive error messages
- Use specific exit codes for different error types

**Logical Grouping**
- Group related constants together
- Keep functions/methods focused on single responsibility
- Separate I/O from business logic where possible

### File Operations

**Respect File Moves**
- If a file has been renamed/moved without duplicate, consider the newest structure correct
- Do not revert seemingly deliberate file moves if you did not cause them

## Documentation Policy

**NO Documentation Unless Asked**
- Do not write README files, API docs, or user-facing documentation unless explicitly requested
- Do not write code comments explaining obvious logic

**License Headers**
All source files must include the full license text at the top. See language-specific skills for exact formatting:
- `python-majo` - Python file headers
- `shell-majo` - Shell script headers
- `rust-majo` - Rust file headers (if created)
- `zig-majo` - Zig file headers (if created)

**AGENTS.md Maintenance (CRITICAL)**

Maintain an `AGENTS.md` file with:
- Knowledge of the codebase
- Understood code style and structure
- Practices and methodologies recognized
- Linguistic style of comments
- Current task at hand and/or to-do list

**Location**: Place wherever documentation is stored in the project.

**Purpose**: Enable resumption from a context-less state without requiring codebase inquiry every time a new agent-or-LLM conversation thread starts.

**Updates**: Update old knowledge in the file as you work.

## Environment Awareness

### Read-Write Environment

**Gemini CLI, Claude Code, ChatGPT Codex CLI**: Your environment is NOT read-only. You can read and write files in this workspace.

### Search Constraints

**Grok-code-fast-1**: Do NOT use regex-based or purely wildcard workspace/file content searches. Use globs or regexes that have a non-wildcard component.

## When to Use This Skill

Activate this skill when:
- Starting work on any codebase
- Generating new code
- Refactoring existing code
- Unsure about documentation requirements
- Need to maintain AGENTS.md

## SPDX License Identifiers

When creating new source files in public domain projects, add the appropriate SPDX identifier at the top:

**For most files** (dual-licensed):
```python
# SPDX-License-Identifier: Unlicense OR 0BSD
```

**For files by contributors who cannot waive copyright**:
```python
# SPDX-License-Identifier: 0BSD
```

## Integration

This skill works alongside language-specific skills:
- `python-majo` - Python-specific standards (UV, basedpyright, MDF)
- `js-bun-majo` - JavaScript/Bun standards
- `shell-majo` - POSIX shell scripting standards
- `git-majo` - Git workflow and commit standards
- `docs-majo` - Documentation writing standards
- `task-planning-majo` - Planning workflows
- `public-domain-setup-majo` - Public domain repository setup
- `windows-majo` - Windows-specific command alternatives
- `skill-authoring-majo` - Creating new Agent Skills
- `agents-md-authoring-majo` - Writing effective AGENTS.md files

Always load this skill first, then the appropriate language-specific skill.
