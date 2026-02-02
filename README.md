# mark's Agent Skills

an attempt to write skills with high-signal activation because i didn't want to ask the agent to not use `head` on my windows machine, among other things

## skills

### core standards (always start here)

- `majo-standards` — universal principles: British English, error handling, exit codes, AGENTS.md maintenance
- `agents-md-authoring-majo` — writing effective AGENTS.md files (see the 6-core-areas framework)
- `skill-authoring-majo` — creating new skills from patterns

### language-specific

- `python-majo` — Python development with UV, basedpyright, ruff, Python 3.10+ syntax, and Meadow Docstring Format (MDF)
- `js-bun-majo` — JavaScript/TypeScript using Bun (not npm, i've hopped on the Bun train)
- `shell-majo` — POSIX shell scripting (pure sh, not bash), error handling, exit codes
- `csharp-unity-majo` — C# development for Unity: naming conventions, British spellings, callback patterns

### workflow and tooling

- `git-majo` — my git workflow: auto-commit after every prompt, conventional commits, never auto-push
- `task-planning-majo` — planning workflow for complex tasks: gather context, draft plan, 3 questions max
- `docs-majo` — writing documentation in my voice: first person lowercase "i", casual but technical, British English
- `mdf-majo` — Meadow Docstring Format for Python docstrings

### platform and setup

- `windows-majo` — working on Windows: maps Unix commands to PowerShell equivalents (`tail` → `Get-Content`, etc.)
- `public-domain-setup-majo` — setting up repos with dual licensing (Unlicense OR 0BSD)

### sizes

trying not to overbloat the skills as per [best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

| skill | lines | words | status |
|-------|-------|-------|--------|
| `agents-md-authoring-majo` | 401 | 1748 | 🟢 |
| `csharp-unity-majo` | 210 | 914 | 🟢 |
| `docs-majo` | 518 | 1612 | 🟡 |
| `git-majo` | 201 | 798 | 🟢 |
| `js-bun-majo` | 71 | 398 | 🟢 |
| `majo-standards` | 307 | 1354 | 🟢 |
| `mdf-majo` | 443 | 1671 | 🟢 |
| `public-domain-setup-majo` | 346 | 1573 | 🟢 |
| `python-majo` | 334 | 1267 | 🟢 |
| `shell-majo` | 450 | 1583 | 🟢 |
| `skill-authoring-majo` | 436 | 1852 | 🟢 |
| `task-planning-majo` | 265 | 1250 | 🟢 |
| `windows-majo` | 440 | 1492 | 🟢 |

run `count.py` to update this table.

for whats in a skill: <https://agentskills.io>

### how skills activate

skills load in three levels:

1. **discovery** — only `name` + `description` loaded at startup
2. **activation** — full SKILL.md loaded when the agent thinks it's relevant
3. **deep dive** — `references/` and `examples/` loaded when explicitly referenced

common triggers:

- "writing Python code" → `python-majo`
- "this is complex" → `task-planning-majo`  
- "commit" → `git-majo`
- "README" → `docs-majo`
- "Windows" → `windows-majo`

### using multiple skills together

skills stack. i usually do:

1. base: `majo-standards` (always)
2. language: `python-majo`, `js-bun-majo`, etc.
3. workflow: `git-majo`, `task-planning-majo` (as needed)

### design principles

- **clear activation triggers** — the `description` is the main signal. be specific: "Python with UV" not "a skill about code"
- **actionable instructions** — tell the agent HOW ("use `uv add`") not what ("uv is a package manager")
- **explicit boundaries** — always have "when to use" AND "do NOT use" sections
- **test before shipping** — check that the skill triggers when it should and doesn't when it shouldn't

### skills vs AGENTS.md

these work alongside AGENTS.md (project-specific knowledge):

- use **AGENTS.md** for: project-specific stuff, exact flags, version-matched docs
- use **skills** for: cross-project patterns, large content, workflows

AGENTS.md wins because it's always loaded. skills win for stuff that doesn't fit.

### validating skills

for my own use lol:

```powershell
for /d %i in (majo-skills\*) do @echo Validating %i... && uvx --refresh --from ./agentskills/skills-ref skills-ref validate "%i"
```

## licence

all skills are dual-licensed under [The Unlicense](https://unlicense.org/) OR [BSD Zero Clause License](https://opensource.org/licenses/0BSD) (SPDX: `Unlicense OR 0BSD`).

go ham.
