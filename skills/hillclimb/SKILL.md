---
name: hillclimb
description: Trigger this if the user says "hill climb" or "hillclimb".
---

# Hillclimb

Improve the work in rounds until a panel of delegates scores it at or above
the user's bar. If a program can give the score instead (tests, an eval, a
timer), use it in place of delegates and loop the same way.

Before a round, address outstanding PR comments, fix known issues, and run
relevant checks. Give the delegates the updated implementation; do not defer
known fixes until reviews return. If the user wants to discard the
implementation and explore new ideas, skip fixes to code being replaced.

Bring in delegates to score the work. If the user's request or instructions
name them, use those. Otherwise use two strong models from different
providers, at high reasoning effort, for example GPT Sol and Claude Opus.
Any number of delegates works.

In T3 Code, use `orchestrator_capabilities` to resolve the models, then
`delegate_task` to start one delegate per model in parallel. Elsewhere, use
the harness's subagent tools. If a named delegate is unavailable, report it
instead of substituting.

Give each delegate the request and relevant context. Keep their work
read-only. Ask each delegate for a score out of 10. When you can, give them
something to compare against: the version before, and any alternatives the
user points at. Scores given with nothing to compare against run high. Do
not tell delegates the score you are trying to hit.

Do not wait idle. When a result arrives, check its findings against the code
at once and decide what to fix while the other delegates run. Do not edit
files while a delegate still reviews the same checkout. If the user's
instructions mark a delegate as non-blocking, do not wait for it; treat a
late result as feedback and do not record its score.

Count each full review pass as one round.
A fresh review after fixes starts a new round.

If you agree with their recommendations, make the changes and request a fresh
review after. Continue this process until every delegate's score meets the
bar. The bar is the score the user asked for. If they gave none, use 9 out
of 10.

If the work ends in a pull request, put the results in the PR description.
Put this section before the model and harness line at the end:

```markdown
## Hillclimb

Bar: 9/10. Rounds: 2

| Delegate | Round 1 | Round 2 |
| --- | --- | --- |
| GPT Sol | 7/10 | 9/10 |
| Claude Opus | 6/10 | 9/10 |
```

If a delegate gives no score, write `no score`. Do not invent one.
If the PR is open, edit the description. Do not post a comment for this.
If there is no PR, put the same results in the final reply only.

Do not let repeated reviews result in scope creep. It is your job to fight to
keep scope limited.
