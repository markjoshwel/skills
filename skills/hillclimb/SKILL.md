---
name: hillclimb
description: Trigger this if the user says "hill climb" or "hillclimb".
---

# Hillclimb

The user wants something made better by measurement, not by one pass of your
own judgment: a UI, a flaky prompt, tool descriptions, a slow path. Turn the
job into a hill: a score, a loop, and a stop. Then climb until the bar is met
or the budget ends. A score you can measure yourself is a score you can push
up.

If the user did not clearly ask for a hill climb, do not start one. A loop
with judges can run for hours and spend a lot of usage.

## Set the hill

Fix four things before round 1. Take them from the request. Ask only when you
cannot tell what to measure.

- **Target.** What you are improving, and what must stay as it is.
- **Score.** A program or judges. See the next two sections.
- **Bar.** "The eval passes 85 of 85." "Every judge gives 9 or higher in
  every category." If the user gave none, use 9 out of 10 for judges. For a
  program with no natural pass mark, ask.
- **Budget.** A number of rounds. If the user gave none, use 10.

## The score

A program is best: tests, an eval, a timer, a byte count. It gives the same
answer every round and costs almost nothing.

- For a prompt, a skill, or tool descriptions, build the eval from real
  failures. Mine the session transcripts (`~/.claude/projects` for Claude
  Code) for the times a model did the wrong thing, sort them into
  categories, and make each one a case.
- Run it before you change anything. That is the baseline. Run it twice to
  see how much it moves on its own.
- Never change the score to make it pass: no deleted cases, loosened checks,
  or special cases for the test. If the score looks wrong, stop and say so.

Use judges only where no program can score: design, writing, taste.

## Judges

- **Who.** The judges the user names in the request. Otherwise the panel in
  their `CLAUDE.md` or `AGENTS.md`. Otherwise two strong models from
  different providers, for example one GPT Sol and one Claude Opus. Any
  number works. One is fine for a small job. A third, for example Claude
  Fable, helps when the score is about taste.
- **How.** In T3 Code, call `orchestrator_capabilities` to resolve the
  models, then `delegate_task` to start one delegate per judge in parallel.
  Elsewhere, use the harness's subagent tools. If a named judge is
  unavailable, report it instead of substituting.
- **Fresh every round.** Start new delegates each round with the same brief.
  A judge that remembers the last round scores the change, not the result.
- **The brief stands alone.** What the thing is for, absolute paths to the
  output, the categories to score, and the reply format: a score from 1 to
  10 per category, and the one change that would raise each. Review only.
  No edits, no subagents.
- **Judge the output, not your summary.** Screenshots, raw replies, command
  output. Make them fresh each round.
- **Anchor the scores.** A judge gave a UI 9 out of 10 alone, and 7.4 next
  to two competing apps. Put the baseline and the best alternatives in the
  same panel and have the judge score all of them. Reference scores drift
  between rounds, so watch the gap as well as the number.
- **Do not tell judges the bar.** A judge that knows the target drifts
  toward it.
- **Spend in order when usage is tight.** Run one judge alone until it
  passes, then add the next. Record the others as `not run`.
- If a judge gives no score, write `no score`. Do not invent one. A timeout,
  an error, or no reply is not a pass.

## Climb

Each round: measure, read the results, fix the lowest score first, measure
again.

- Check each finding against the source before you act on it. Judges are
  sometimes wrong. Decline those with a written reason.
- The target is the scope. Decline feedback that grows the change past it,
  and list it as a follow-up.
- Work on a branch and commit each round that raises the score. If a round
  lowers it, undo that round before you go on.
- A note from the user beats the judges. "Too grayscale, bring the color
  back" becomes a requirement for every later round.
- Keep a table of scores per round.

## Lock, then cut

When the bar is met, measure once more. Scores are noisy, and one good round
is not a pass. If it holds, commit.

For text that loads into a model's context (a prompt, a skill, tool
descriptions), then reverse the job: delete as much as you can while the
score holds. If the user gave a size, like "a third of the size", that is
the new bar. Otherwise cut until the score drops, then step back one.

## Stop and report

Stop when the bar holds on two measurements, when the budget ends, or after
three rounds with no gain. Only the first is a pass.

The user sets the top. To go higher after a pass, start a new branch or
worktree with a higher bar and leave the passing version alone.

Report the verdict first: bar met, budget ended, or stuck, with the scores.
Then the table, before and after side by side (for a UI, screenshots with
the changes marked), what you changed, the findings you declined and why,
and what you could not verify. If the work ends in a pull request, put the
table in the description:

```markdown
## Hillclimb

Bar: every judge 9 or higher in every category. Rounds: 3

| Judge | Baseline | Round 1 | Round 2 | Round 3 |
| --- | --- | --- | --- | --- |
| GPT Sol | 6.5 | 8 | 9 | 9 |
| Claude Opus | 6 | not run | 8 | 9 |
```

If nothing can produce a score, say so. Make a few options that differ, show
before and after side by side, and let the user pick.
