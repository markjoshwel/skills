---
name: docs-majo
description: |
  Documentation writing standards for Mark's projects.
  Use when writing READMEs, changelogs, API docs, or user-facing documentation.
  Covers writing style, formatting, structure, and tone.
license: Unlicense OR 0BSD
metadata:
  author: Mark Joshwel <mark@joshwel.co>
  version: "2026.2.2"
---

# documentation writing standards

Standards for writing user-facing documentation. See [references/REFERENCE.md](references/REFERENCE.md)
for full templates.

## Goal

Produce documentation that is clear, consistent with Mark's personal style, and readable as plaintext.

## When to Use This Skill

- Writing or editing README files
- Creating changelogs or release notes
- Drafting API documentation
- Writing installation or usage instructions
- Formatting user-facing documentation

## Do NOT Use

- Code comments (use `mdf-majo` or `python-majo`)
- Git commit messages (use `git-majo`)
- Internal technical notes or TODOs
- Generated API docs

## Process

1. **Identify document type** (README, changelog, API reference)
2. **Apply voice and tone** rules
3. **Follow formatting constraints** (100 char limit, British English)
4. **Structure sections** by document type
5. **Review against this skill** before finalising

## Constraints

- **British spelling**: licence, colour, behaviour, recognised (PyPI READMEs may use "License")
- **100 character limit** for prose (code blocks and URLs can exceed)
- **Readable as plaintext** in a code editor, not just preview
- **Sentence case for headings** (not Title Case)

## Testing Skills

- [ ] 100 character line length limit (except code/URLs)
- [ ] British spelling used throughout
- [ ] First person with lowercase "i"
- [ ] Sentence case headings
- [ ] Proper code block language tags
- [ ] Voice and tone matches examples
- [ ] Structure follows document type patterns

## voice and tone

### identity

- **first person, lowercase "i"**: "i" not "I" in prose
- **casual but technical**: friendly without sacrificing precision
- **honest about limitations**: openly state when things are incomplete
- **personal motivation**: explain *why*, not just *what*

### signature phrases

- **"et voilà!"** — completion/success marker after setup
- **"go ham"** — permission to use freely (licence sections)
- **emoticons**: `(●'◡'●)`, `:D`, `(❁´◡`❁)`, `:)`
- **self-deprecating qualifiers**: "an okay interpreter", "(unserious)", "you probably shouldn't"

### example

```markdown
# tomlantic

> [!WARNING]
> tomlantic is at 0.2.1 and currently, only i use it myself. it isn't battle tested,
> so issues may arise.
> if you're willing to run into potential bugs and issues, feel free to use it!

marrying [pydantic](https://github.com/pydantic/pydantic) models and
[tomlkit](https://github.com/sdispater/tomlkit) documents for data validated,
style-preserving toml files

uses generics to automagically preserve model types, so you don't lose out on model
type information :D
```

## formatting

### line length

- **100 character limit** for prose (code blocks and URLs can exceed)
- Must be readable as plaintext in a code editor

### headings

- **sentence case** (not Title Case): `## usage`, `### installation`
- No punctuation at end

### title formats

```text
# surplus                              ← single lowercase word
# surplus on wheels                    ← lowercase with spaces
# surplus on wheels: WhatsApp Bridge   ← colon hierarchy for subprojects
# zigby: an okay brainfuck interpreter ← name + tagline in title
```

### lists

- `-` for unordered lists
- `1.` for ordered lists
- 4 spaces for nested items

### links

- Use descriptive link text, not raw URLs
- External: GitHub repos, documentation
- Internal: `[usage](#usage)`

### code blocks

| tag | use for |
| --- | --- |
| `text` | shell commands to copy (NOT `bash`) |
| `shell` | shell scripts with shebangs |
| `python` | python code |
| (none) | URLs and plain output |

**MkDocs features:**

```markdown
``` title="path/to/file.py"
code here
```

--8<-- "path/to/include"
```

## structural patterns

### table of contents

Include for READMEs over ~50 lines. Use nested bullets for hierarchy.

```markdown
- [section](#section)
  - [subsection](#subsection)
- [what are the features?](#what-are-the-features)
```

### sections (in order)

1. **title** — `# project-name`
2. **warning/note blocks** — beta status, important caveats
3. **description** — one line, then optional longer description
4. **table of contents** — for longer docs
5. **usage** — installation, quickstart, examples
6. **api reference** — for libraries/modules
7. **licence** — full text or reference

### deprecation/archive notices

```markdown
| This project has been archived. |
| ---- |
```

### stub READMEs (monorepo subprojects)

```markdown
# project name

brief one-liner

see <https://project.example.com>
or [docs/index.md](../../docs/index.md)
for more information
```

### question-based sections

```markdown
## what are the features?
## cool, how do i use it?
## could it be better?
## frequently questioned answers
```

## admonitions (callouts)

**plaintext** (default, works everywhere):

```markdown
> **note**
> content here (two spaces after "note" line)

> **warning**
> content here
```

**GitHub-style** (for GitHub):

```markdown
> [!WARNING]
> This is a breaking change!

> [!NOTE]
> Additional information here.
```

**MkDocs-style** (for MkDocs/Material):

```markdown
!!! warning
    This is a breaking change!

!!! note "Title"
    Additional information here.
```

## common patterns

### definition lists

Use two-space linebreak for options/variables:

```markdown
- `VARIABLE_NAME`
  description of what it does

  ```text
  example value
  ```

  setting it to `n` will also be treated as empty.
```

### CLI documentation

1. Embed full `--help` output in code block
2. Group options by category
3. Separate sections for: querying, defaults, formatting, examples

See [references/REFERENCE.md](references/REFERENCE.md) for full template.

### API reference

For detailed API reference documentation following MDF structure, see `mdf-md-api-docs-majo`.

Brief overview:
- Headers: `### def|class module.Name()`
- Use backticks around all Python code
- Two-space linebreak before descriptions
- Sections: signature → arguments/attributes → methods → returns → raises → usage

### installation section

```markdown
## installation

install from PyPI:

```text
pip install project
```

install from source:

```text
pip install git+https://github.com/user/project.git
```

**nix users, rejoice:** `nix run github:user/project`
```

For single-file modules, mention direct inclusion as public domain.

## licence documentation

### standard pattern

```markdown
## licence

project is free and unencumbered software released into the public domain.
for more information, please refer to [UNLICENCE](/UNLICENCE), <https://unlicense.org>,
or the python module docstring.
```

Casual version:

```markdown
project is permissively "i do not care" licenced with the zero-clause bsd licence, go ham
```

### dependency licences

```markdown
- [**dependency**](url) —
  brief description
  MIT Licence

    - [**transitive-dep**](url) —
      what it does
      Apache 2.0
```

### dual licensing

```markdown
- source code:
  The Unlicence (full text or reference)

- artwork:
  CC BY 4.0 with usage notes
```

See [references/REFERENCE.md](references/REFERENCE.md) for full licence page template.

## changelog format

```markdown
## project vX.Y.Z

(released on the 14th of October 2023)

!!! warning
    breaking changes here

brief summary of release

### what's new

- added feature X

### what's changed

- deprecated Y

### what's fixed

- bug in Z

### thanks!

- [contributor](url) for their first contribution!

full changelog: <https://github.com/user/repo/compare/vOLD...vNEW>

---
```

### guidelines

- Use ordinal dates: "1st of July 2024", "14th of October 2023"
- Use `!!! information` for tentative/beta releases
- Use `!!! warning` for breaking changes
- Include GitHub compare links
- Thank contributors with profile links
- Use `---` separators between versions

See [references/REFERENCE.md](references/REFERENCE.md) for full changelog template.

## special elements

### personal rationale sections

Explain personal use case:

```markdown
## rationale

i have a Mac mini that i use for... (explains personal setup)

there is a good chance that... (explains logical chain)

so this tool... (ties back to purpose)
```

### strikethrough for playful emphasis

```markdown
~~a good~~ an okay-ish format
~~yell~~ gently remind
```

### backslash line continuation

```markdown
- feature description \
  (note: this is optional but helpful)
```

## integration

This skill extends `majo-standards`. Works alongside:

- `mdf-majo` — Meadow Docstring Format specification
- `python-majo` — Python code standards
- `shell-majo` — Shell script documentation
- `git-majo` — Commit messages that reference docs
