---
name: prompt-writing
description: Trigger this only if the user asks for it by name, for example "prompt skill", "prompt-writing skill", or "/prompt-writing". Do not trigger it just because a task involves writing a prompt or a skill.
---

# Prompt Writing

How to write text that another model will read and act on: a prompt the user
will send, a brief you send to a subagent, a skill, a tool description. A
skill is a prompt that gets saved and loaded later, so everything here applies
to skills too.

If the user did not ask for this skill by name, do not apply it. Write the way
you normally would.

## Before you write

Settle three things first.

- **What does done look like?** State it as something the reader can observe:
  a passing check, a merged PR, a file, a score.
- **Who reads it?** Which model, in which harness, with what already in its
  context. See "Know the reader".
- **Does it ask for the outcome?** People ask for the mechanism they guessed
  at. BAD: "Add a panel that tracks how long each tool call takes." GOOD:
  "Break down every tool call on this machine by duration. I want to find the
  slowest commands and fix my environment."

Look up repo and machine facts yourself. If a missing answer would change the
done condition or what the reader is allowed to do, ask the user before you
write: numbered questions, lettered options, your recommendation first, so
"1A 2C" is a full reply. For anything smaller, assume and say so after.

## What a prompt needs

Most prompts are a few sentences. A reader that already has the thread needs
one or two of these parts. A cold reader or an unattended run needs all seven.

1. **The situation.** Who the user is, what just happened, why they want
   this, what is already known or suspected. The reader makes many choices
   you did not cover, and the reason is what it uses to make them. "The user
   is not watching this thread" does more than ten rules about check-ins.
2. **The goal and the done condition.**
3. **How you would do it.** Give your mental model in the order you would
   work: "look at the new screenshot, compare it with the old one and the
   competitors, score it, fix the weakest part, repeat". Do not script
   branches the reader can handle alone. Number steps only when order matters.
4. **Proof.** Name the most direct check. Proof is something the reader
   observed in this session: command output, a reproduction, a screenshot.
   Its own summary is not proof.
5. **Edges.** Scope: what is out. Budget: how many rounds, when to stop.
   Permissions: what it may do without asking, and what the request does not
   grant. Models balk at risky steps that have no explicit grant, and they
   keep adding work when nothing tells them to stop.
6. **Unknowns.** When to ask and with which tool. What to decide alone and
   list in the report. The safe path when blocked. "Report it instead of
   substituting. Do not guess."
7. **What to send back.** Verdict first. Observed facts apart from judgment.
   What was not verified. Give a literal template only when the format must
   be exact.

## Wording

- **Give the reason with the rule.** "Never write your own polling loop.
  Every watcher on the account shares one rate limit." A rule with a reason
  gets applied to cases you did not list. A bare rule gets followed to the
  letter or dropped.
- **Show BAD and GOOD when the point is taste.** Use real examples of the
  mistake you actually see. The reader copies what the examples show and
  keeps making the mistakes they do not cover.
- **Define the words you lean on.** "blocker = the intended case is wrong.
  nit = everything else."
- **Invite disagreement.** "If you think this is a good idea, do it.
  Otherwise, suggest something else."
- **Guard against growth.** "Make the smallest change that works. Fix the
  case that happened, not every case that could. Push back on feedback that
  grows the scope."
- **Require what the reader may want to hide.** If a reviewer's verdict could
  be bad, make the verdict a required line in the report.
- **Point at material instead of pasting it.** Paths, links, the command that
  shows the diff. When you pass along someone else's notes, say so: "Treat
  this as a guide to what I am looking for, not as exact instructions."
- **Write in the style you want back.** The reader copies what it reads. Em
  dashes in a skill come back as em dashes in every reply. Plain words,
  short sentences. No capitals for emphasis, no em dashes, no emoji, no
  terms coined on the spot.
- **Cut what says nothing.** Cut any sentence you cannot restate as an
  instruction, a fact, a number, or an example. Cut any sentence that could
  sit unchanged in a different prompt: "be thorough", "follow best
  practices", "you are a world-class engineer".

## Know the reader

The user's read of the models, as of November 2026. Edit it when it stops
matching. It describes the model that will read your prompt, not you.

- **Claude Opus** does everything it is told and rarely misses a detail. It
  does not challenge the task, applies every piece of feedback, and does not
  stop on its own. Give it a stop condition, a scope limit, and permission
  to disagree. Best for work that can be proven.
- **Claude Fable** questions the premise, finds the clever fix, and will say
  "this is fine, ship it". It can skim past a detail and let small things
  slide. Put the few requirements that must not be missed at the top, ask
  for proof, and leave the method open. Best for taste, open problems, and
  a thread that runs in circles.
- **GPT Sol** is the most thorough reviewer. It will not merge or push
  without an explicit grant in its context, and on long runs alone its
  writing gets hard to follow. Give it a narrow scope, severity definitions,
  and a fixed reply format.
- **Haiku** is for bulk pattern matching over many files. Not for code.
- **Reader unknown:** write for the literal one. State the scope, the stop
  condition, and the grants.

## Briefs for other agents

Agents write poor briefs for other agents, mostly because they forget the
reader has none of the thread. Reread the brief as if it were all you had.

- Make it stand alone: absolute repo path, base commit, the intent in one or
  two sentences, what is out of scope, which checks ran and their results,
  the command that shows the change.
- Say what it may touch. "Review only. Do not edit, commit, push, comment, or
  start subagents."
- Say what to look for, what to skip, and the reply format. Use stable ids
  if there will be another round.
- To check work that is already done, hand over the work, not your
  conclusion. A reviewer given your theory returns it confirmed. Never tell
  a judge the score you hope for.
- For review, prefer a model from another provider. Different training
  catches different bugs. If a model the user named is unavailable, report
  it. Do not substitute.
- Timeout, error, or no reply is not approval. Check each finding against
  the source yourself before you act on it.

## Skills

Pick the container first. If the user named one, use it, and say in one line
if another fits better.

- Said once: a prompt.
- Said the same way several times, or the same mistake keeps coming back: a
  skill. Not from a clever idea, and not in advance.
- Must hold on every task without a trigger: a line in `CLAUDE.md` or
  `AGENTS.md`. A skill only applies when it loads.
- Must behave the same every time (waiting, polling, parsing): a script in
  the skill's directory. Tell the reader to use it and never write its own.
- A flow with more branches than you can list, like triage or setup: one
  prompt that lays out the playbook, not a state machine in code.

Then:

- **The description is a trigger, not a summary.** It is the only part the
  model sees before it loads the skill. Its one job is to get the right
  agent to load it at the right moment. BAD: "A workflow that gathers
  reviews from several models and iterates until they agree." GOOD:
  "Trigger this if the user says 'council'." A skill the model should pick
  up on its own names the moment: "Use whenever leaving comments on GitHub."
- **Prefer a trigger phrase to `disable-model-invocation`.** A phrase can be
  spoken, stacked in one message ("take over this PR, full stop"), and
  called from other skills. A slash-only skill can do none of that.
- **Open with what the trigger means.** "If the user triggered this, it's
  because they are not watching this thread." Then the stance in one line:
  "Modernize the idea, not just the branch."
- **Add an escape hatch for a mistaken load.** "If the user did not clearly
  ask for a full send, do not assume full autonomy."
- **One job per skill.** Call other skills by name instead of repeating
  them. List the skills it needs.
- **Keep it short.** A skill for one job rarely needs 100 lines. Every line
  is a rule, a reason, a definition, or an example.
- **Name harness tools with a fallback.** "`AskUserQuestion` in Claude Code,
  `request_user_input` in Codex, or the question tool your harness has."
  Personal settings, like which models sit on a council, go in `CLAUDE.md`
  so the skill stays shareable.
- **Put it where the user's skills already live.** Check `~/.claude/skills`,
  the project's `.claude/skills`, and `~/.codex/skills`. Each skill is
  `<name>/SKILL.md` with `name` and `description` frontmatter.

A skill is never finished:

- When a run goes wrong, ask the agent that did it: "Why did you do that?
  What were you missing?" Then fix the line that misled it, or add one line.
  Every rule should trace back to a real failure.
- Watch for the overcorrection. A new "ask the user when stuck" section made
  agents ask all the time. It needed a second line: "Ask only when you
  cannot continue alone."
- When you edit an existing skill, change the fewest lines. Do not rewrite it
  in your own voice or add a section per fix. Skills that agents edit bloat,
  so reread the whole file and delete.
- Test before you install: paste the text into a fresh thread with a real
  task. Read other people's skills and take the parts that fit. Never
  install one unread.

- To improve a prompt, skill, or tool description that already exists but
  misfires, measure it instead of rewriting it by feel. That is the
  `hillclimb` skill.

## Handing it over

- A prompt for the user to send: one fenced block, ready to paste, written as
  the user speaking. Do not walk the user through it line by line.
- A skill: write the file, then give the user the trigger phrase and the
  path. Tell them to read every line. It is theirs to edit.
- After either, list what you invented: assumed facts, reasons the user never
  gave, made-up examples, budget numbers. The user replaces those first.
