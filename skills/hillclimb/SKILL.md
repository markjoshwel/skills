---
name: hillclimb
description: Trigger this if the user says "hill climb" or "hillclimb".
---

# Hillclimb

The user wants something made better by measurement, not by one pass of your
own judgment: a UI, a flaky prompt, tool descriptions, a slow path. Find a
score you can measure yourself, then loop until it clears the bar.

If the user did not clearly ask for a hill climb, do not start one. These
loops can run for hours.

Take the bar and the budget from the request. With no bar, use 9 out of 10
from every judge. Running out of budget is not a pass.

## The score

A program is best: tests, an eval, a timer, a byte count. For a prompt or
tool descriptions, build the eval from the times a model did the wrong thing
in the user's session history. Run it before you change anything, so you
have a baseline.

Use judges only where no program can score, like design or writing.

## Judges

Use the judges the user names. Otherwise use the panel in their `CLAUDE.md`
or `AGENTS.md`. Otherwise use two strong models from different providers,
for example GPT Sol and Claude Opus. Any number works, including one.

In T3 Code, resolve the models with `orchestrator_capabilities` and start
one `delegate_task` per judge in parallel. Elsewhere, use the harness's
subagent tools. If a named judge is unavailable, report it instead of
substituting.

Start fresh judges each round. Give them the output itself (screenshots,
raw replies), not your summary. Ask for a score from 1 to 10 per category
and what would raise it. Keep them read-only.

Put the old version and the best alternatives in the same panel. A judge
gave a UI 9 alone, and 7.4 next to two competing apps.

Do not tell judges the bar. A judge that knows the target drifts toward it.
If a judge gives no score, write `no score`. Do not invent one.

When usage is tight, run one judge until it passes, then add the next.

## The loop

Measure, fix the lowest score first, measure again. Check each finding
before you act on it, because judges are sometimes wrong. Decline feedback
that grows the change past what the user asked for. A note from the user
beats the judges.

Scores are noisy. Measure again before you call the bar met.

For text that loads into a model's context, cut after the bar is met:
delete as much as you can while the score holds.

## Report

Lead with the verdict, then the scores per round, then before and after
side by side. If the work ends in a pull request, put the table in the
description:

```markdown
## Hillclimb

Bar: every judge 9 or higher. Rounds: 3

| Judge | Baseline | Round 1 | Round 2 | Round 3 |
| --- | --- | --- | --- | --- |
| GPT Sol | 6.5 | 8 | 9 | 9 |
| Claude Opus | 6 | not run | 8 | 9 |
```
