---
name: agents-md-authoring-majo
description: Write effective AGENTS.md files for AI coding agents. Use when creating or updating AGENTS.md to ensure high signal-to-noise ratio, proper structure, and maximum agent effectiveness. Based on Vercel research showing AGENTS.md achieves 100% pass rate vs 79% with skills.
license: Unlicense OR 0BSD
metadata:
  author: Mark Joshwel <mark@joshwel.co>
  version: "2026.2.2"
---

# AGENTS.md Authoring Guide (Mark)

Write effective AGENTS.md files that outperform skills-based approaches.

## Core Principle

**Minimize root file; maximize signal-to-noise ratio through strategic structure, not exhaustive documentation.**

AGENTS.md is loaded on every agent request. Keep it concise but information-dense.

## AGENTS.md vs Skills: When to Use Each

| Approach | Use When | Performance |
|----------|----------|-------------|
| **AGENTS.md** | Project-specific knowledge, always-needed context, version-matched docs | 100% pass rate |
| **Skills** | Cross-project patterns, progressive disclosure, large reference material | 79% pass rate |

**Key Finding (Vercel Research)**: AGENTS.md achieved 100% pass rate vs 79% with skills, even with explicit skill invocation instructions.

**Why AGENTS.md Wins**:
1. No decision point - always loaded
2. Consistent availability - in system prompt every turn
3. No ordering issues - no "read docs first vs explore project first" dilemma

**Use AGENTS.md for**:
- Domain concepts specific to your project
- Non-obvious conventions agents can't infer
- Executable commands with exact flags
- Version-matched framework documentation
- Project boundaries and gotchas

**Use Skills for** (see `skill-authoring-majo`):
- Cross-project patterns
- Large content requiring progressive disclosure
- Workflows that don't fit in AGENTS.md
- When context bloat is a concern

## Six-Core-Areas Framework

Structure your AGENTS.md around six key areas (300-800 tokens total):

### 1. Commands (~80 tokens)

Exact, copy-paste-ready commands with flags.

```markdown
## Build Commands

```bash
# Build the package
pnpm build

# Development mode
pnpm dev

# Run tests
pnpm test
```
```

**Why**: Agents reference repeatedly; vague instructions create clarification loops.

### 2. Testing (~50 tokens)

Framework, location, coverage minimum, run command.

```markdown
## Testing

Framework: Jest
Location: tests/
Coverage: 80% minimum
Run: pnpm test
```

Don't include philosophy or lengthy examples.

### 3. Project Structure (~50 tokens)

Strategic hints, not exhaustive paths.

```markdown
## Project Structure

src/ — Application code (READ)
tests/ — Unit/integration tests
docs/ — Markdown (WRITE)
```

Agents discover files well; structure drifts. Skip detailed file listings.

### 4. Code Style (~75 tokens)

One real repo example showing BOTH positive and negative patterns.

```markdown
## Code Style

```python
# GOOD: Use retry() for polling/waiting
from next_test_utils import retry
await retry(async () => {
    const text = await browser.elementByCss('p').text()
    expect(text).toBe('expected value')
})

# AVOID: Don't use setTimeout for waiting
await new Promise((resolve) => setTimeout(resolve, 1000))
```
```

One example > three paragraphs of description. Show the anti-pattern too.

### 5. Git Workflow (~40 tokens)

Commit format, branch naming, PR requirements.

```markdown
## Git Workflow

Commits: feat(scope): description (Conventional Commits)
Branches: feature/*, bugfix/*, docs/*
PRs: lint ✓, tests ✓, focused diff
```

### 6. Boundaries (~50 tokens)

Three-tier system: Always/Ask/Never (more effective than flat "don't" lists).

```markdown
## Boundaries

ALWAYS: Run tests before commits; follow naming conventions
ASK FIRST: Before schema changes; before new dependencies; before CI/CD changes
NEVER: Commit secrets; edit node_modules; remove failing tests without approval
```

**Why three tiers**: Eliminates agent ambiguity better than flat lists.

## Token Efficiency Techniques

### Progressive Disclosure

Link to detailed docs instead of inlining:

```markdown
Detailed patterns: [see docs/api.md §3.2]
Quick reference: Endpoints return { "data": {...}, "error": null }
```

### Compression

Use pipe-delimited format for complex concepts. Vercel achieved 80% reduction (40KB → 8KB):

```markdown
[Docs Index]|root: ./.docs
|01-getting-started:{installation.md,project-structure.md}
|02-api:{routing.md,caching.md}
```

### Hierarchical Summarization

Extended TOC at top; full sections below. Keeps frequent tasks in focus.

## What to Include vs Exclude

### INCLUDE:

- Domain concepts specific to your project ("Organization" vs "Workspace")
- Non-obvious conventions agents can't infer ("Use composition over inheritance")
- Executable commands with exact flags
- Boundaries and gotchas from real experience ("This library has a memory leak in v3.2.1")
- Real code examples from your repo (not templates)

### EXCLUDE:

- File structure documentation (agents infer this; it drifts)
- Duplicates of README/docs (link instead)
- Abstract best practices ("Write clean code")
- Lengthy prose (every section = 10-second scan)
- Vague guidance ("Be careful with X" → "Never do X without...")
- Generic advice that overlaps across projects

## Example AGENTS.md Structure

Based on Vercel's Next.js AGENTS.md:

```markdown
# Project Development Guide

## Quick Start

```bash
# Install dependencies
pnpm install

# Start development
pnpm dev

# Run tests
pnpm test
```

## Project Structure

src/ — Application code
tests/ — Test files
docs/ — Documentation

## Build Commands

```bash
pnpm build      # Production build
pnpm dev        # Development server
pnpm test       # Run all tests
pnpm test:watch # Watch mode
```

## Testing

Framework: Vitest
Location: tests/
Coverage: 80% minimum

### Writing Tests

```typescript
// GOOD: Use retry() for polling
await retry(async () => {
    expect(await page.text()).toBe('done')
})

// AVOID: Don't use setTimeout
await new Promise(r => setTimeout(r, 1000))
```

## Code Style

- TypeScript strict mode
- Prettier for formatting
- ESLint for linting

## Git Workflow

Commits: feat(scope): description
Branches: feature/*, bugfix/*
PRs: tests pass, lint clean

## Boundaries

ALWAYS: Run tests before push; update AGENTS.md after agent mistakes
ASK FIRST: Before adding dependencies; before architectural changes
NEVER: Commit .env files; modify generated code directly

## Common Issues

- **Build fails after branch switch** → Run `pnpm build`
- **Tests timeout** → Check if dev server is running
- **Type errors** → Run `pnpm types` to check
```

## Nested AGENTS.md (Monorepos)

For monorepos, use nested AGENTS.md files:

```
project/
├── AGENTS.md                    # Global rules
├── packages/
│   ├── backend/
│   │   └── AGENTS.md           # Backend-specific
│   └── frontend/
│       └── AGENTS.md           # Frontend-specific
```

Agents use the nearest AGENTS.md (like .gitignore). Keeps context tight and relevant.

## Iterative Refinement Process

1. **Start minimal**: Six-core-areas, ~400 tokens
2. **Run agents on real tasks**: Observe mistakes
3. **When agent misunderstands/fails**: Note it
4. **Add clarifying rule/example/boundary to AGENTS.md**
5. **Tell agent**: "I updated AGENTS.md. Given these new rules, refactor accordingly."
6. **Repeat**: Each iteration tightens spec, reduces future mistakes

**Example iterations**:
- Iteration 1: Agent uses old API → Add: "Use v2/users endpoint, not v1/users"
- Iteration 2: Agent skips validation → Add: "Always validate ID format"
- Iteration 3: Agent modifies tests when not asked → Add boundary: "Never modify tests unless explicitly asked"

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Vague rules | Agent asks clarifying questions (wasted tokens) | Be specific: "Never commit secrets" not "Be careful with secrets" |
| Outdated AGENTS.md | Agent ignores stale guidance or hallucinates | Update immediately after mistakes; track in git |
| Monolithic structure | Agent loads irrelevant context every task | Use nested AGENTS.md; progressive disclosure |
| Duplicate docs | Token waste; maintenance burden | Link instead of inlining |
| Abstract examples | Agents don't know how to apply guidance | Use real files: "copy DashForm.tsx" |
| Conflicting rules | Agent uncertain which rule applies | Use Always/Ask/Never tiers, not flat lists |

## Quick Checklist

- [ ] Root ≤ 800 tokens
- [ ] Six-core-areas framework present
- [ ] Three-tier boundaries (Always/Ask/Never)
- [ ] Real code examples (positive & negative)
- [ ] Links to external docs, not duplicates
- [ ] No file structure documentation
- [ ] No vague guidance
- [ ] Updated after every agent mistake
- [ ] Nested AGENTS.md for monorepos (if applicable)
- [ ] Progressive disclosure for large docs

## Integration with Other Skills

This skill extends `majo-standards`. Always ensure `majo-standards` is loaded for:
- AGENTS.md maintenance
- Universal code principles
- Documentation policies

Works alongside:
- `skill-authoring-majo` — For deciding when to use AGENTS.md vs create skills
- `task-planning-majo` — For planning AGENTS.md updates
- `git-majo` — For committing AGENTS.md changes
- `docs-majo` — For writing documentation about AGENTS.md

## References

- Vercel Research: ["AGENTS.md outperforms skills in our agent evals"](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals) (100% vs 79% pass rate)
- Next.js AGENTS.md: https://github.com/vercel/next.js/blob/canary/AGENTS.md
- agents.md specification: https://agents.md/
