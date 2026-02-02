---
name: docs-majo
description: Documentation writing standards for Mark's projects. Use when writing README files, changelogs, API documentation, and other user-facing docs. Covers writing style, formatting, structure, and tone.
license: Unlicense OR 0BSD
metadata:
  author: Mark Joshwel <mark@joshwel.co>
  version: "2026.2.2"
---

# documentation writing standards

standards for writing user-facing documentation. see [references/REFERENCE.md](references/REFERENCE.md)
for full templates and examples.

## voice and tone

### identity

- **first person, lowercase "i"**: always "i" not "I" in prose
- **casual but technical**: friendly without sacrificing precision
- **honest about limitations**: openly state when things are incomplete or untested
- **personal motivation**: explain *why* something was built, not just *what*

### signature phrases

- **"et voilà!"** — completion/success marker after setup steps
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

## spelling and language

- **british spelling always**: licence, licenced, colour, behaviour, recognised
- exception: PyPI READMEs may use American "License" for compatibility

## formatting

### line length

- **100 character limit** for all documentation files
- exception: code blocks and URLs can exceed if necessary
- documentation should be readable as plaintext in a code editor, not just preview

### headings

- use sentence case (not Title Case)
- examples: `## usage`, `### installation`, `## api reference`
- no punctuation at end of headings

### title formats

```text
# surplus                              ← single lowercase word
# surplus on wheels                    ← lowercase with spaces
# surplus on wheels: WhatsApp Bridge   ← colon hierarchy for subprojects
# zigby: an okay brainfuck interpreter ← name + tagline in title
```

### lists

- use `-` for unordered lists
- use `1.` for ordered lists
- indent with 4 spaces for nested items

### links

- use descriptive link text, not raw URLs
- external links to GitHub repos, documentation, etc.
- internal links use anchors: `[usage](#usage)`

## code blocks

### language tags

| tag | use for |
| --- | --- |
| `text` | shell commands to copy (NOT `bash`) |
| `shell` | shell scripts with shebangs |
| `python` | python code |
| (none) | URLs and plain output |

### MkDocs features

```markdown
``` title="path/to/file.py"
code here
```

--8<-- "path/to/include"
```

## structural patterns

### table of contents

- always include for READMEs over ~50 lines
- use nested bullet points for hierarchy
- question-style headers work: `[what are the features?](#what-are-the-features)`

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

use table style for visual emphasis:

```markdown
| This project has been archived. |
| ---- |
```

### stub READMEs (monorepo subprojects)

minimal pointer to main docs:

```markdown
# project name

brief one-liner

see <https://project.example.com>
or [docs/index.md](../../docs/index.md)
for more information
```

### question-based sections

works well for casual/personal projects:

- `## what are the features?`
- `## cool, how do i use it?`
- `## could it be better?`
- `## frequently questioned answers`

## admonitions (callouts)

**default: use plaintext admonitions** (works everywhere):

```markdown
> **note**
> content here (two spaces after "note" line for linebreak)

> **warning**
> content here
```

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

!!! note "Title"
    Additional information here.
```

## common patterns

### definition lists

use two-space linebreak for options/variables:

```markdown
- `VARIABLE_NAME`
  description of what it does

  ```text
  example value
  ```

  setting it to `n` will also be treated as empty.
```

### CLI documentation

1. embed full `--help` output in code block
2. group options by category (clip options, output options, etc.)
3. separate sections for: querying, defaults, formatting, examples

see [references/REFERENCE.md](references/REFERENCE.md) for full template.

### API reference

API references follow the Meadow Docstring Format (MDF) structure, translated to markdown.
see `mdf-majo` for the full MDF specification.

**header format:**

```markdown
### <def|class> module.Name()
```

**section structure** (in order, all optional except preamble):

1. **preamble** — brief one-line description (no label)
2. **body** — longer explanation if needed (no label)
3. **signature** — python code block with function/class signature
4. **attributes** (for classes) or **arguments** (for functions)
5. **methods** (for classes)
6. **returns** — return type with optional description
7. **raises** — exceptions that may be raised
8. **usage** — code example

**example — function:**

```markdown
### def tomlantic.ModelBoundTOML.set_field()

sets a field by its location. not recommended for general use due to a lack of
type safety, but useful when setting fields programatically

will handle `pydantic.ValidationError` into more toml-friendly error messages.
set `handle_errors` to `False` to raise the original `pydantic.ValidationError`

- signature:

  ```python
  def set_field(
      self,
      location: str | tuple[str, ...],
      value: object,
      handle_errors: bool = True,
  ) -> None: ...
  ```

- arguments:
  - `location: str | tuple[str, ...]`  
    dot-separated location of the field to set
  - `value: object`  
    value to set at the specified location
  - `handle_errors: bool = True`  
    whether to convert pydantic ValidationErrors to tomlantic errors

- raises:
  - `AttributeError` — if the field does not exist
  - [`tomlantic.TOMLValidationError`](#class-tomlantictomlvalidationerror) — if validation fails
  - [`pydantic.ValidationError`](https://docs.pydantic.dev/) — if validation fails and `handle_errors` is `False`
```

**example — class:**

```markdown
### class tomlantic.ModelBoundTOML

glue class for pydantic models and tomlkit documents

- signature:

  ```python
  class ModelBoundTOML(Generic[M]): ...
  ```

- attributes:
  - `model: pydantic.BaseModel`  
    the bound pydantic model instance

- methods:
  - [`def model_dump_toml()`](#def-tomlanticmodelboundtomlmodel_dump_toml)  
    dumps the model as a style-preserved tomlkit.TOMLDocument
  - [`def get_field()`](#def-tomlanticmodelboundtomlget_field)  
    safely retrieve a field by its location
  - [`def set_field()`](#def-tomlanticmodelboundtomlset_field)  
    sets a field by its location

- usage:

  ```python
  toml = ModelBoundTOML(YourModel, tomlkit.parse(...))
  toml.model.message = "hello"
  document = toml.model_dump_toml()
  ```
```

**formatting notes:**

- use backticks around all python code: `` `Type` ``, `` `variable: Type` ``
- link to other sections with anchors: `[`ClassName`](#class-moduleclassname)`
- link to external docs when referencing third-party types
- arguments/attributes use two-space linebreak before description
- omit sections that add no value (e.g., obvious returns)

### installation section

show multiple methods:

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

for single-file modules, mention direct inclusion as public domain.

## licence documentation

### standard pattern

```markdown
## licence

project is free and unencumbered software released into the public domain.
for more information, please refer to [UNLICENCE](/UNLICENCE), <https://unlicense.org>,
or the python module docstring.
```

or the casual version:

```markdown
project is permissively "i do not care" licenced with the zero-clause bsd licence, go ham
```

### dependency licences

nested list with em-dash separator:

```markdown
- [**dependency**](url) —
  brief description
  MIT Licence

    - [**transitive-dep**](url) —
      what it does
      Apache 2.0
```

### dual licensing

when code and assets have different licences:

```markdown
- source code:
  The Unlicence (full text or reference)

- artwork:
  CC BY 4.0 with usage notes
```

see [references/REFERENCE.md](references/REFERENCE.md) for full licence page template.

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

- use ordinal dates: "1st of July 2024", "14th of October 2023"
- use `!!! information` for tentative/beta releases
- use `!!! warning` for breaking changes
- include GitHub compare links at the end
- thank contributors with profile links
- use `---` separators between versions

see [references/REFERENCE.md](references/REFERENCE.md) for full changelog template.

## special elements

### personal rationale sections

frequently include a "rationale" or "why" section explaining personal use case:

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

this skill extends `majo-standards`. works alongside:

- `mdf-majo` — for Meadow Docstring Format specification (API reference structure)
- `python-majo` — for Python code standards
- `shell-majo` — for shell script documentation
- `git-majo` — for commit messages that reference docs
