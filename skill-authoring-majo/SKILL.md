---
name: skill-authoring-majo
description: Create new Agent Skills based on learned patterns and workflows. Use when you have developed a repeatable workflow, coding pattern, or expertise that doesn't fit in AGENTS.md but should be reusable across projects. Covers SKILL.md format, progressive disclosure, and skill structure best practices.
license: Unlicense OR 0BSD
metadata:
  author: Mark Joshwel <mark@joshwel.co>
  version: "2026.2.2"
---

# Skill Authoring Guide (Mark)

Create reusable Agent Skills from learned patterns and workflows.

## When to Create a Skill

**Create a skill when:**
- You've developed a repeatable workflow (e.g., "how I set up X")
- You have domain expertise that applies across projects
- You find yourself repeating the same instructions
- A pattern doesn't fit well in AGENTS.md (too large, too specific)
- You want progressive disclosure (load only when needed)

**Don't create a skill when:**
- It's project-specific knowledge (use AGENTS.md)
- It's a one-time task
- It's already covered by existing skills

## Skill vs AGENTS.md

| Use Case | AGENTS.md | Skill |
|----------|-----------|-------|
| Project-specific knowledge | ✅ | ❌ |
| Cross-project patterns | ❌ | ✅ |
| Large reference material | ❌ | ✅ |
| Progressive disclosure | ❌ | ✅ |
| Current task tracking | ✅ | ❌ |
| Reusable workflows | ❌ | ✅ |

## SKILL.md Format

### Required Structure

```yaml
---
name: skill-name                    # 1-64 chars, lowercase alphanumeric + hyphens
description: When to use this...    # 1-1024 chars, explains what and when
license: Unlicense OR 0BSD          # Your license
metadata:                           # Optional but recommended
  author: Mark Joshwel <mark@joshwel.co>
  version: "2026.2.2"
  requires: python>=3.10            # Optional requirements
---

# Skill Title

## When to Use This Skill

Clear activation triggers:
- User mentions "keyword"
- Working with specific technology
- Specific task type

## Overview

Brief explanation of what this skill provides.

## Instructions

Step-by-step guidance, examples, code snippets.

## Integration

How this skill relates to others.
```

### Naming Conventions

**Format**: `{topic}-majo` for personal skills

**Examples**:
- `python-majo` - Python development
- `task-planning-majo` - Planning workflows
- `windows-majo` - Windows-specific commands

**Good names**:
- Short and descriptive
- Lowercase with hyphens
- Indicates purpose clearly

## Directory Structure

### Simple Skill (text only)

```
skill-name/
└── SKILL.md
```

### Complex Skill (with references)

```
skill-name/
├── SKILL.md
├── references/
│   ├── detailed-guide.md
│   └── api-reference.md
└── examples/
    └── example.py
```

### Advanced Skill (with scripts)

```
skill-name/
├── SKILL.md
├── scripts/
│   └── setup.sh
├── references/
│   └── patterns.md
└── assets/
    └── template.json
```

## Progressive Disclosure

The key principle: load information only when needed.

### Level 1: Discovery (Always Loaded)

Just the YAML frontmatter:
- `name` - skill identifier
- `description` - when to activate

**~100 tokens** - loaded at startup

### Level 2: Activation (Loaded When Matched)

Full SKILL.md body:
- Instructions
- Examples
- Workflows

**< 5000 tokens** - loaded when task matches

### Level 3: Deep Dive (Loaded on Demand)

References and assets:
- Detailed guides
- Code templates
- Large examples

**Loaded only when explicitly needed**

## Writing Effective Skills

### 1. Clear Activation Triggers

**Good**:
```yaml
description: Use when working with Windows paths (B:\path\to\file) or when Unix commands like tail, head, mkdir -p fail
```

**Bad**:
```yaml
description: A skill about Windows
```

### 2. Action-Oriented Instructions

**Good**:
```markdown
### Step 1: Check Repository State

Determine if this is a new repository:

```bash
if [ -d .git ]; then
    echo "Existing repository"
else
    echo "New repository"
fi
```
```

**Bad**:
```markdown
Git is a version control system. It was created by Linus Torvalds...
```

### 3. Include Decision Trees

```markdown
User task → What kind of request?
   ├─ Start focused work → Check status first, then start session
   ├─ Check current timer → Use status command
   └─ Review productivity → Use stats command
```

### 4. Show Examples

```markdown
**Example**:
```python
# SPDX-License-Identifier: Unlicense OR 0BSD

def example():
    pass
```
```

### 5. Cross-Reference Other Skills

```markdown
This skill works alongside:
- `majo-standards` - For SPDX identifiers
- `python-majo` - For Python-specific setup
```

## Common Skill Patterns

### Pattern 1: Tool Wrapper

Wraps a CLI tool with usage guidance:

```yaml
name: sheets-cli-majo
description: Read, write, and update Google Sheets via CLI. Use when the user asks to read spreadsheet data, update cells, append rows, or work with Google Sheets.
```

**Structure**:
- Quick reference table
- Workflow pattern
- Command examples
- Best practices

### Pattern 2: Language Standards

Coding standards for a specific language:

```yaml
name: python-majo
description: Python development standards for Mark's workflow. Use when writing Python code.
```

**Structure**:
- Tool choices (UV, basedpyright, ruff)
- Syntax preferences (Python 3.10+)
- Documentation format (MDF)
- Workflow steps

### Pattern 3: Platform-Specific

Platform-specific workarounds:

```yaml
name: windows-majo
description: Windows-specific development standards. Use when working on Windows systems to avoid Unix-isms.
```

**Structure**:
- Recognition guide (how to identify platform)
- Unix → Windows command mapping
- Common pitfalls
- Cross-platform alternatives

### Pattern 4: Workflow/Process

Repeatable workflows:

```yaml
name: task-planning-majo
description: Task planning workflow for complex work. Use when a task seems complex enough to require planning.
```

**Structure**:
- When to use (decision criteria)
- Step-by-step workflow
- Templates
- Best practices

### Pattern 5: Setup/Configuration

Project initialization:

```yaml
name: public-domain-setup-majo
description: Set up public domain repositories with dual licensing. Use when initializing a new repository.
```

**Structure**:
- Prerequisites
- Setup workflow
- Verification steps
- Post-setup actions

## Skill Checklist

Before finalizing a skill:

- [ ] Clear name following convention
- [ ] Description explains when to activate
- [ ] Proper YAML frontmatter
- [ ] License specified
- [ ] Instructions are actionable
- [ ] Examples included
- [ ] Decision trees where appropriate
- [ ] Cross-references to other skills
- [ ] Progressive disclosure considered
- [ ] Under 5000 tokens (or split into references)

## Workflow: Creating a New Skill

### Step 1: Identify the Pattern

Ask:
- Is this repeatable across projects?
- Does it not fit in AGENTS.md?
- Will I use this again?

### Step 2: Choose a Name

Follow `{topic}-majo` convention.

### Step 3: Draft the SKILL.md

Start with:
1. YAML frontmatter
2. When to use section
3. Core instructions
4. Examples

### Step 4: Review for Progressive Disclosure

- Can any sections be moved to references/?
- Is the description clear enough for discovery?
- Will the full content load only when needed?

### Step 5: Test the Skill

- Does the description trigger appropriately?
- Are instructions clear?
- Do examples work?

### Step 6: Place in Skills Directory

```
majo-skills/
└── your-new-skill/
    ├── SKILL.md
    └── [references/]
        └── [if needed]
```

### Step 7: Update AGENTS.md

Note the new skill in the project's AGENTS.md:

```markdown
## Available Skills

- `majo-standards` - Core standards
- `your-new-skill` - [brief description]
```

## Examples from Mark's Skills

### Minimal Skill (js-bun-majo)

```markdown
---
name: js-bun-majo
description: Use Bun instead of Node.js and npm for JavaScript/TypeScript development.
---

# JavaScript/Bun Standards

**Use Bun as the runtime, tooling, and package manager in lieu of Node and npm.**

If uncertain on how to invoke Bun commands, use the command line for help.
```

### Medium Skill (task-planning-majo)

- Clear activation criteria
- Step-by-step workflow
- Decision tree
- Plan templates

### Complex Skill (python-majo)

- Multiple sections
- References/ directory for MDF format
- Tool-specific guidance
- Workflow integration

## Anti-Patterns to Avoid

### 1. Too Broad

❌ **Bad**: "A skill about programming"
✅ **Good**: "Python development with UV, basedpyright, and MDF docstrings"

### 2. Too Narrow

❌ **Bad**: "How to fix bug #123 in project X"
✅ **Good**: "Debugging workflow for Python asyncio issues"

### 3. Documentation Instead of Instructions

❌ **Bad**: Explaining what a tool is
✅ **Good**: Explaining how to use the tool

### 4. Missing Activation Triggers

❌ **Bad**: "This skill helps with code"
✅ **Good**: "Use when writing Python code, working with type annotations, or setting up Python projects"

### 5. No Examples

❌ **Bad**: Pure text descriptions
✅ **Good**: Code examples, command snippets, decision trees

## Integration with Existing Skills

### Skill Dependencies

If skill B extends skill A, mention it:

```markdown
## Integration

This skill extends `majo-standards`. Always ensure `majo-standards` is loaded.
```

### Skill Conflicts

If two skills shouldn't be used together, document it:

```markdown
## Note

Do not use alongside `other-skill` - they provide conflicting guidance.
```

## Resources

- Agent Skills specification: https://agentskills.io/specification.md
- Example skills: https://github.com/anthropics/skills
- Skill validation: Use `skills-ref validate ./skill-name`

## Quick Reference

| Element | Required | Notes |
|---------|----------|-------|
| YAML frontmatter | Yes | name, description required |
| name | Yes | 1-64 chars, lowercase, hyphens |
| description | Yes | 1-1024 chars, explains when to use |
| license | Recommended | Unlicense OR 0BSD |
| metadata | Optional | author, version, etc. |
| Body content | Yes | Instructions, examples |
| references/ | Optional | For large content |
| scripts/ | Optional | Executable code |
| assets/ | Optional | Templates, data |

## Integration

This skill extends `majo-standards`. Always ensure `majo-standards` is loaded for:
- AGENTS.md maintenance
- Universal code principles
- Documentation policies

Works alongside:
- `docs-majo` — For writing skill documentation
- `git-majo` — For committing new skills
- `task-planning-majo` — For planning complex skill creation
