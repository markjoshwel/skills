---
name: prompt-writing
description: Trigger this only if the user asks for it by name, for example "prompt skill" or "/prompt-writing". Do not trigger it just because a task involves writing a prompt or a skill.
---

# Prompt Writing

The user wants a prompt, a brief for another agent, or a skill. Most bad
prompts are over-engineered. Say what you want the way you would say it to a
smart coworker, then stop. Most prompts are a few sentences. Match the length
to the ask.

If the user did not ask for this skill by name, do not apply it.

## The prompt

Ask for the outcome, not the mechanism the user guessed at.

BAD

> Add a panel that tracks how long each tool call takes.

GOOD

> Break down every tool call on this machine by duration. I want to find the slowest commands and fix my environment.

Say why. The reader makes many choices you did not cover, and the reason is
what it uses to make them. "I am not watching this thread" does more than ten
rules about when to check in.

Say what done looks like and how to prove it. Proof is something the reader
saw in this session: command output, a reproduction, a screenshot.

Describe how you would do the job, in the order you would do it. Do not
script every branch. The reader is smart.

Add a limit only where a run goes wrong without it:

- A stop. Models keep adding work when nothing tells them to. "Make the
  smallest change that works. Push back on feedback that grows the scope."
- A grant. Models balk at risky steps like merging unless the permission is
  in their context.
- Room to disagree. "If you think this is a good idea, do it. Otherwise,
  suggest something else."

Give each rule its reason, so the reader can apply it to cases you did not
list. Cut any sentence that could sit unchanged in a different prompt, like
"be thorough". Do not invent thresholds or steps to make the prompt look
complete. Leave them out, or ask.

The reader copies the style it reads. Plain words, short sentences, no em
dashes.

## A brief for another agent

The reader has none of this thread. Give it the path, the intent, what is
out of scope, what it may touch, and the reply format. To check finished
work, hand over the work, not your conclusion. On an open problem, share
your leads and call them guesses. If a model the user named is unavailable,
report it. Do not substitute.

## A skill

A skill is a prompt the user got tired of repeating. Make one for something
they have said several times, not for a clever idea. A rule that must hold
on every task belongs in `CLAUDE.md` instead, because a skill only applies
when it loads.

The description is a trigger, not a summary. It is the only part the model
sees before it loads the skill.

BAD

> description: A workflow that gathers reviews from several models and iterates until they agree.

GOOD

> description: Trigger this if the user says 'council'.

Open with what the trigger means: "If the user triggered this, it's because
they are not watching this thread." Add one line for a mistaken load: "If
the user did not clearly ask for this, do not assume it."

Keep it under 100 lines. Do not write rules in advance. When a run goes
wrong, ask the agent that did it why, then fix the line that misled it or
add one. Put the skill where the user's other skills live.

## Hand it over

One fenced block, ready to paste, written as the user speaking. Below it,
list anything you assumed. No walkthrough. For a skill, give the path and
the trigger phrase.

To fix a prompt or skill that misfires, measure it with the `hillclimb`
skill instead of rewriting it by feel.
