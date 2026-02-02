---
name: docs-majo
description: Documentation writing standards for Mark's projects. Use when writing README files, changelogs, API documentation, and other user-facing docs. Covers writing style, formatting, structure, and tone.
license: Unlicense OR 0BSD
metadata:
  author: Mark Joshwel <mark@joshwel.co>
  version: "2026.2.2"
---

# Documentation Writing Standards (Mark)

Standards for writing user-facing documentation.

## Writing Style

### Spelling

**Use British English spellings throughout all documentation.** See `majo-standards` for the complete list.

Common documentation words:

- **colour** (not color)
- **licence** (noun) / **license** (verb)
- **behaviour** (not behavior)
- **favourite** (not favorite)
- **center** (technical/abstract, e.g. image center) / **centre** (a physical location, e.g. town centre)

### Tone

- **Casual and conversational** — write like you're talking to a friend
- **Use contractions**: "don't", "it's", "i've"
- **First person**: "i", "my", "me" — this is personal documentation
- **Enthusiasm**: use emoticons like `:D` sparingly but appropriately
- **Self-aware**: acknowledge limitations and beta status honestly

### Example

```markdown
# tomlantic

> [!WARNING]  
> tomlantic is at 0.2.1 and currently, only i use it myself. it isn't battle tested,
> so issues may arise.  
> if you're willing to run into potential bugs and issues, feel free to use it!

marrying [pydantic](https://github.com/pydantic/pydantic) models and
[tomlkit](https://github.com/sdispater/tomlkit) documents for data validated,
style-preserving toml files

uses generics to automagically preserve model types, so you don't lose out on model type
information :D
```

## Formatting

### Line Length

- **100 character limit** for all documentation files
- Exception: code blocks and URLs can exceed if necessary

### Headings

- Use sentence case (not Title Case)
- Examples: `## usage`, `### installation`, `## api reference`
- No punctuation at end of headings

### Lists

- Use `-` for unordered lists
- Use `1.` for ordered lists
- Indent with 3 or 4 spaces for nested items

### Code Blocks

- Use fenced code blocks with language specifiers
- Shell commands use ` ```shell ` or ` ```text `
- Python code uses ` ```python `

### Links

- Use descriptive link text, not raw URLs
- External links to GitHub repos, documentation, etc.
- Internal links use anchors: `[usage](#usage)`

## Structure

### README.md Standard Structure

```markdown
# project-name

> [WARNING/NOTE blocks for important info]

brief one-line description

longer paragraph description if needed

- [section](#section)
  - [subsection](#subsection)

## section

### subsection

content...

## licence

[licence text or reference]
```

### Table of Contents

- Always include a TOC for READMEs over ~50 lines
- Use nested bullet points for hierarchy
- Link to section anchors

### Sections (in order)

1. **Title** — `# project-name`
2. **Warning/Note blocks** — Beta status, important caveats
3. **Description** — One line, then optional longer description
4. **Table of Contents** — For longer docs
5. **Usage** — Installation, quickstart, examples
6. **API Reference** — For libraries/modules
7. **Licence** — Full text or reference

## Content Guidelines

### Developer Handbooks

For developer documentation (not user-facing):

- Use abstract/note admonitions for environment setup information
- Include prerequisite software lists with links
- Provide command examples for starting development environments
- Document workflow steps clearly with numbered lists
- Use `!!! note` or `> **note**` for alternative methods (e.g., "alternatively, run `check.sh`")
- Include platform-specific notes (NixOS, WSL, etc.)

### Licence Pages

For `licence.md` or `licenses.md`:

- Group by project/component with `## [name](link)` headings
- State the primary licence clearly in bold: **The Unlicence**
- Include licence text using MkDocs include syntax:
  ```markdown
  ``` title="path/to/UNLICENCE"
  --8<-- "path/to/UNLICENCE"
  ```
- List dependencies with links, descriptions, and their licences
- Use `---` separators between different projects
- Note when dependencies have different licences
- Use sentence case throughout

Example:
```markdown
# licences

## [project-name](index.md)

**The Unlicence**

project is free and unencumbered software released into the public domain:

``` title="src/project/UNLICENCE"
--8<-- "src/project/UNLICENCE"
```

however, the dependencies project relies on are licenced under different licences:

- [**dependency**](https://pypi.org/project/dependency/) —
  Brief description
  MIT Licence

---

## [another-project](path.md)

**Mozilla Public Licence 2.0**
```

### Contributing Guidelines

Structure for `contributing.md`:

```markdown
# the contributor's handbook

expected details on development workflows? see [the developer's handbook](developing.md)

## which forge do i use?

explain options (GitHub, personal forge, email patches)

## git workflow

1. fork and branch from `future` or `main`
2. make and commit changes
3. pull upstream and resolve conflicts
4. commit copyright waiver if needed
5. submit pull request

### waiving copyright

!!! danger "Warning"
    this section is a **must** to follow if you have modified **any** unlicenced code:
    
    - list of directories/files

!!! info
    the command to create an empty commit is `git commit --allow-empty`

when contributing your first changes, please include an empty commit for a copyright
waiver using the following message (replace `Your Name` with your name or username):

```text
Your Name Copyright Waiver

I dedicate any and all copyright interest in this software to the
public domain...
```

(from <https://unlicense.org/WAIVER>)
```

Key elements:
- Use `!!! danger` for critical requirements (copyright waiver)
- Use `!!! info` for helpful tips
- Include verbatim text blocks for legal text
- Link to original sources (unlicense.org, creative commons, etc.)
- Use sentence case throughout
- Cross-reference other documentation files

### Installation Section

- Multiple methods (PyPI, source, direct download)
- Include shell commands
- Note any special considerations

### Quickstart/Examples

- Working code examples that can be copy-pasted
- Comments explaining key points
- Show realistic use cases

### API Reference

- Use MDF-style documentation (see `python-majo`)
- Link to related functions/classes
- Include signatures and return types
- Show usage examples

### Changelogs

Structure:
```markdown
## project vX.Y.Z

(released on [date] on tag `[tag-name]`)

!!! information
    tentative release notes, beta status, etc.

!!! warning
    breaking changes, api breaks, etc.

### what's new

- added feature X
- added flag `--option`

### what's changed

- deprecated/removed features
- renamed classes/functions

### what's fixed

- bug fixes

### thanks!

- [username](https://github.com/username) for their contribution!

full changelog: <https://github.com/user/repo/compare/vOLD...vNEW>
```

Guidelines:
- Use `!!! information` for tentative/beta releases
- Use `!!! warning` for breaking changes
- Use `!!! note` for versioning scheme changes or important notices
- Include GitHub compare links at the end
- Always thank contributors with links to their profiles
- Use sentence case for bullet points
- Can use `---` separators between version sections for clarity

## Admonitions (Callouts)

**Default: Use plaintext admonitions** (works everywhere):

```markdown
> **note**  
> blah blah blah

> **warning**  
> blah blah blah
```

**Important**: Include two spaces after the bold header line so the second line renders on a new line.

**Only use other styles when explicitly requested or when writing for specific platforms:**

**GitHub-style** (when writing for GitHub):
```markdown
> [!WARNING]  
> This is a breaking change!

> [!NOTE]  
> Additional information here.
```

**MkDocs-style** (when writing for MkDocs/Material):
```markdown
!!! warning
    This is a breaking change!

!!! note
    Additional information here.
```

## Integration

This skill extends `majo-standards`. Always ensure `majo-standards` is loaded for:
- AGENTS.md maintenance
- Universal code principles
- Documentation policies

Works alongside:
- `python-majo` — For Python API documentation
- `js-bun-majo` — For JavaScript/Bun documentation
- `shell-majo` — For shell script documentation
- `git-majo` — For commit messages that reference docs
- `task-planning-majo` — For planning documentation structure
