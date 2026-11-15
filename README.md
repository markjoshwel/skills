# skills

Agent skills I use. They work in Claude Code and Codex. `hillclimb` uses
[T3 Code](https://github.com/pingdotgg/t3code) delegates when they are
available and falls back to the harness's own subagents when they are not.

| Skill | Say | What it does |
|---|---|---|
| `prompt-writing` | "prompt skill" | Writes prompts, subagent briefs, and skills that say the outcome, the proof, and the edges. |
| `hillclimb` | "hill climb" | Improves something against a score in a loop: a program or a panel of judges, a bar, a budget, a stop. |

Both load only when you say the phrase.

## Install

```bash
git clone https://github.com/markjoshwel/skills
ln -s "$PWD/skills/skills/"* ~/.claude/skills/   # Claude Code
ln -s "$PWD/skills/skills/"* ~/.codex/skills/    # Codex
```

## Judges

`hillclimb` uses the judges you name in the request: "hill climb this with
one Sol and one Opus". To set a default panel, put it in your `CLAUDE.md` or
`AGENTS.md`. With neither, it picks two strong models from different
providers.

## Credit

Based on Theo's videos on prompting, skills, and hill climbing, and on his
[tstack](https://github.com/t3dotgg/tstack) skills.
