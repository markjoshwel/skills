---
name: task-planning-majo
description: Task planning workflow for complex work. Use when a task seems complex enough to require planning. Gather context, draft a plan in markdown, ask up to 3 follow-up questions, and track progress in AGENTS.md or AGENTS.PLAN.md.
license: Unlicense
metadata:
  author: mark@joshwel.co
  version: "2026.2.2"
---

# Task Planning Workflow (Mark)

Planning protocol for complex tasks requiring structured execution.

## When to Plan

**Plan when**:
- The task seems complex enough to require multiple steps
- You're unsure about the approach or requirements
- The task involves significant changes across multiple files
- User explicitly asks for a plan

**Don't plan when**:
- The task is straightforward (single file, obvious fix)
- User gives explicit step-by-step instructions
- It's a continuation of already-planned work

## Planning Workflow

### Step 1: Gather Context

Gather just enough context to reason about the prompt:

1. Read relevant files (AGENTS.md, existing code, configs)
2. Understand the codebase structure
3. Identify related components

**Don't over-research** - get enough to reason about the task, then plan.

### Step 2: Draft Plan

Think about and draft a plan in markdown regarding next steps:

```markdown
## Plan: [Brief Task Description]

### Phase 1: [First Major Step]
- [ ] Sub-task 1
- [ ] Sub-task 2

### Phase 2: [Second Major Step]
- [ ] Sub-task 1
- [ ] Sub-task 2

### Follow-up Questions
1. [Question about requirements]
2. [Question about approach]
3. [Question about constraints]
```

### Step 3: Ask Follow-up Questions (Max 3 Times)

Include any follow-up considerations you may want to ask the user before continuing.

**Rules**:
- Ask maximally up to three times for follow-up questions
- When asking, present them as up to five numbered questions
- Be specific and concise

**Example Questions**:
```
Before proceeding, I have a few clarifications:

1. Should the new feature be opt-in or enabled by default?
2. Are there any specific performance requirements I should consider?
3. Should this integrate with the existing auth system or be standalone?
```

### Step 4: Finalize and Execute

Once questions are answered:

1. Update the plan with clarified requirements
2. Proceed with execution
3. Track progress in AGENTS.md or AGENTS.PLAN.md

## Plan Tracking

### Where to Store Plans

**Primary**: `AGENTS.md` (if it exists in the project)

**Fallback**: `AGENTS.PLAN.md` (create if AGENTS.md doesn't exist)

### Plan Format

```markdown
## Current Plan: [Task Name]

**Status**: In Progress / Completed / Blocked
**Started**: [Date]

### Phases

#### Phase 1: Setup
- [x] Task 1 (completed)
- [ ] Task 2 (in progress)
- [ ] Task 3 (pending)

#### Phase 2: Implementation
- [ ] Task 4
- [ ] Task 5

### Blockers
- [Description of any blockers]

### Notes
- [Any relevant notes or decisions made]
```

### Updating Plans

As you work:

1. **Check off completed items**: Mark tasks as `[x]` when done
2. **Add new discoveries**: If new tasks emerge, add them
3. **Update status**: Change status if blocked or completed
4. **Record decisions**: Note any important decisions made

## Example Workflow

### Scenario: Adding a New Feature

**User**: "Add user authentication to the API"

**Agent Response**:
```
I'll analyze this task and draft a plan. Let me first gather some context...

[Reads AGENTS.md, examines existing API structure]

## Plan: Add User Authentication to API

### Phase 1: Research & Design
- [ ] Review existing user model
- [ ] Choose auth strategy (JWT vs sessions)
- [ ] Design auth endpoints

### Phase 2: Implementation
- [ ] Add password hashing
- [ ] Create login endpoint
- [ ] Create register endpoint
- [ ] Add auth middleware

### Phase 3: Integration
- [ ] Protect existing routes
- [ ] Add tests
- [ ] Update documentation

### Follow-up Questions

1. Should I use JWT tokens or session-based auth?
2. Are there existing user models I should extend, or create new ones?
3. Should registration be open or invite-only?
```

**User**: "Use JWT, extend existing User model, open registration"

**Agent**:
```
Perfect! I'll proceed with JWT-based auth extending the existing User model with open registration.

[Creates/updates AGENTS.md with the plan and starts execution]
```

## Decision Tree

```
User request received
    ↓
Is it complex? (multiple files, unclear approach, significant changes)
    ↓
Yes → Gather context → Draft plan → Ask questions (max 3 rounds) → Execute
    ↓
No → Execute directly
```

## Best Practices

### Do
- ✅ Keep plans concise but complete
- ✅ Ask specific, actionable questions
- ✅ Update AGENTS.md as you progress
- ✅ Mark completed items promptly
- ✅ Record decisions and their rationale

### Don't
- ❌ Over-plan simple tasks
- ❌ Ask more than 3 rounds of questions
- ❌ Let plans go stale (update as you work)
- ❌ Skip tracking in AGENTS.md
- ❌ Ask vague questions like "What should I do?"

## Integration

This skill extends `majo-standards`. Always ensure `majo-standards` is loaded for:
- AGENTS.md maintenance policies
- Universal code principles

Works alongside:
- `python-majo` — For Python-specific planning considerations
- `js-bun-majo` — For JavaScript/Bun-specific planning considerations
- `shell-majo` — For shell script planning considerations
- `git-majo` — For planning git workflows and commits
- `docs-majo` — For planning documentation structure
