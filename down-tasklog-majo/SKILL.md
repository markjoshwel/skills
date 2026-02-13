---
name: down-tasklog-majo
description: >
  Update and manage the "down" tasklog format - a countdown timer and speedrun split tracker.
  Use when reading, writing, or modifying tasklog files for the down timer application.
  Handles @countdownStarts/@countdownEnds directives and HHMM: completed/eta HHMM: pending task entries.
license: Unlicense OR 0BSD
metadata:
  author: Mark Joshwel <mark@joshwel.co>
  version: "1.0.0"
  tags: [tasklog, countdown, timer, productivity, tracking]
---

# Down Tasklog Skill

## Goal

Manage the plaintext tasklog format used by the "down" countdown timer and speedrun split tracker. Read existing tasklogs, add new completed or pending tasks, update countdown periods, and copy updates between source and destination files.

## When to Use This Skill

**Use this skill when:**
- Reading or parsing an existing tasklog file
- Adding new completed tasks (HHMM: message)
- Adding new pending tasks with ETA (eta HHMM: message)
- Updating @countdownStarts or @countdownEnds directives
- Copying tasklog updates from B:\down\assets\data.txt to P:\down\tasklog.txt
- Converting task information into the tasklog format

**Do NOT use this skill when:**
- Working with other productivity/todo formats (not the down format)
- Creating entirely new file formats
- The file is marked read-only (e.g., P:\ files)

## Process

### Reading a Tasklog

1. Read the file at the specified path
2. Parse the structure:
   - @countdownStarts DD/MM/YYYY HHMM - when countdown begins
   - @countdownEnds DD/MM/YYYY HHMM - when countdown ends
   - [DD/MM/YYYY] - date section header
   - HHMM: message - completed task at that time
   - eta HHMM: message - pending task with estimated completion
   - # comment - inline comment for context

### Adding New Tasks

1. **Check current time first** - Run `Get-Date -Format 'HHmm'` to get accurate current time
2. Determine the date section (create new [DD/MM/YYYY] if needed)
3. Insert completed tasks as: `HHMM: task description` (use current time from step 1)
4. Insert pending tasks as: `eta HHMM: task description`
5. Add comments with `#` if additional context is needed
6. Maintain chronological order within each date section

### Updating Countdown Period

1. Update @countdownStarts with new start date/time
2. Update @countdownEnds with new end date/time
3. Format: DD/MM/YYYY HHMM (24-hour format)

### Copying to P: Drive

When the user mentions P: drive (which is read-only for direct writes):

1. Use PowerShell Copy-Item to copy the file:
   ```powershell
   Copy-Item 'source.txt' 'P:\path\tasklog.txt'
   ```

2. Alternatively use cmd:
   ```cmd
   copy "source.txt" "P:\path\tasklog.txt"
   ```

## Constraints

- **ALWAYS check current time first** - Run `Get-Date -Format 'HHmm'` before adding any completed task timestamps. Never assume or guess the time.
- **NEVER write directly to P: drive files** - use copy commands instead
- **Always use DD/MM/YYYY date format** for countdown directives and date sections
- **Always use HHMM 24-hour format** for times (e.g., 1500 not 3:00 PM)
- **Maintain consistent indentation** - tasks should align under their date section
- **Preserve existing comments** starting with #
- **Use Windows commands** (PowerShell Copy-Item) when working with P: drive

## Examples

**Example 1: Adding completed tasks**
```text
[09/02/2026]
1500: continue project from past attempt
# wheelchair movement interaction fix

1550: first prebuild
# friend: urban sprawl env ready by 7pm
```

**Example 2: Adding pending tasks with ETA**
```text
eta 1630: list one unique mechanic per member
# one line description for each person's XR mechanic

eta 1700: note basic failure scenarios
# object lost, stuck, out of bounds → how to recover
```

**Example 3: Full countdown setup**
```text
@countdownStarts 9/2/2026 1500
@countdownEnds 10/2/2026 0900

[09/02/2026]
1500: first task completed
eta 1600: upcoming task
```

**Example 4: Copying to P: drive**
```powershell
Copy-Item 'B:\down\assets\data.txt' 'P:\down\tasklog.txt'
```

## Integration

This skill works alongside:
- `running-windows-commands-majo` — For Windows-specific copy commands to P: drive
- `dev-standards-majo` — For file handling best practices

## References

- The "down" application README explains the full format at B:\down\README.md
- Example tasklog at B:\down\assets\data.txt
