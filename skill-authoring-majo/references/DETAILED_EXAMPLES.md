# Detailed Examples and Patterns

This file contains detailed examples and patterns for skill authoring.
See [SKILL.md](../SKILL.md) for the main skill authoring guide.

---

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

---

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

**Characteristics**:
- Single sentence description
- No metadata
- One-line instruction
- 10 lines total

### Medium Skill (task-planning-majo)

**Characteristics**:
- Clear activation criteria
- Step-by-step workflow
- Decision tree
- Plan templates

### Complex Skill (python-majo)

**Characteristics**:
- Multiple sections
- References/ directory for MDF format
- Tool-specific guidance
- Workflow integration

---

## Anti-Patterns to Avoid

### 1. Too Broad / Vague Description

The description is your PRIMARY TRIGGER. Vague descriptions cause the skill to either:
- Never trigger (lost in noise)
- Trigger for everything (unpredictable behavior)

**Bad**: "A skill about programming"  
**Bad**: "Helps with code"  
**Good**: "Python development with UV, basedpyright, and MDF docstrings. Use when writing Python code or setting up Python projects."

### 2. Too Narrow / One-Off

**Bad**: "How to fix bug #123 in project X"  
**Good**: "Debugging workflow for Python asyncio issues"

### 3. Documentation Instead of Instructions

Skills should be actionable procedures, not educational content.

**Bad**: Explaining what a tool is  
**Good**: Explaining how to use the tool with step-by-step commands

### 4. Missing "Do NOT Use" Criteria

Without anti-conditions, the skill may activate inappropriately.

**Bad**: Only "When to use" with no boundaries  
**Good**: Explicit "Do NOT use when" for edge cases and overlaps

### 5. Overlapping Skills

If multiple skills sound similar, the model picks unpredictably.

**Bad**: Three skills that all "help with coding"  
**Good**: Clear separation:
  - `create-plan` — planning and risk assessment
  - `run-tests` — test orchestration
  - `debug-failures` — investigating errors

### 6. No Examples

**Bad**: Pure text descriptions without code  
**Good**: Concrete code examples, command snippets, decision trees

### 7. Missing Activation Triggers

**Bad**: "This skill helps with code"  
**Good**: "Use when writing Python code, working with type annotations, or setting up Python projects"

### 8. Untested Skills

**Bad**: Writing a skill without testing implicit invocation  
**Good**: Systematic testing with both explicit and implicit triggers before shipping

---

## References

See [SKILL.md](../SKILL.md) for the main skill authoring guide.
