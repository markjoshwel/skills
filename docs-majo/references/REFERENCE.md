# docs-majo reference

detailed examples and templates for documentation patterns.

## full README example

```markdown
# surplus

> [!WARNING]
> surplus is currently in beta. issues may arise.

a Python script to convert coordinates or Plus Codes to shareable text

- [installation](#installation)
  - [from pypi](#from-pypi)
  - [from source](#from-source)
- [usage](#usage)
- [licence](#licence)

## installation

### from pypi

```text
pip install surplus
```

### from source

```text
pip install git+https://github.com/markjoshwel/surplus.git
```

**nix users, rejoice:** `nix run github:markjoshwel/surplus`

## usage

```text
$ surplus 8QMF+FX Singapore
Blk 109, Clementi Street 11
Clementi
Singapore 120109
```

see `surplus --help` for more options.

## licence

surplus is free and unencumbered software released into the public domain.
for more information, please refer to [UNLICENCE](/UNLICENCE), <https://unlicense.org>,
or the python module docstring.
```

## contributing.md template

```markdown
# the contributor's handbook

expected details on development workflows? see [the developer's handbook](developing.md)

## which forge do i use?

i am actively using both [GitHub](https://github.com/markjoshwel/project) and my
[personal forge](https://forge.joshwel.co/mark/project). use whatever is more comfortable
to you.

don't want to make an account for either? feel free to mail in a patch.

## git workflow

1. fork and branch from `future` (or `main` if `future` doesn't exist)
2. make and commit your changes (_see [waiving copyright](#waiving-copyright)_)
3. pull the upstream branch and resolve any conflicts
4. **commit your copyright waiver** (_see [waiving copyright](#waiving-copyright)_)
5. submit a pull request (_or mail in a patch_)

### waiving copyright

!!! danger "Warning"
    this section is a **must** to follow if you have modified **any** unlicenced code:

    - `src/project/`

!!! info
    the command to create an empty commit is `git commit --allow-empty`

when contributing your first changes to the codebase, please include an empty commit
for a copyright waiver using the following message (replace `Your Name` with your name
or username):

```text
Your Name Copyright Waiver

I dedicate any and all copyright interest in this software to the
public domain. I make this dedication for the benefit of the public at
large and to the detriment of my heirs and successors. I intend this
dedication to be an overt act of relinquishment in perpetuity of all
present and future rights to this software under copyright law.
```

(from <https://unlicense.org/WAIVER>)

---

when contributing your first changes to the documentation, please include an empty
commit for a copyright waiver using the following message:

```text
Your Name Copyright Waiver (Documentation)

To the extent possible under law, Your Name has waived all copyright
and related or neighboring rights to the documentation of project.
This work is published from: Country.
```

(adapted from the CC0 deed at <https://creativecommons.org/publicdomain/zero/1.0/>)
```

## licence page template

```markdown
# licences

## [project](index.md)

**The Unlicence**

project is free and unencumbered software released into the public domain:

``` title="src/project/UNLICENCE"
--8<-- "src/project/UNLICENCE"
```

however, the dependencies project relies on are licenced under different licences:

- [**pydantic**](https://github.com/pydantic/pydantic) —
  data validation library using python type annotations
  MIT Licence

    - [**typing-extensions**](https://github.com/python/typing_extensions) —
      backport of new typing features
      Python Software Foundation Licence

- [**requests**](https://github.com/psf/requests) —
  simple HTTP library
  Apache 2.0 Licence

---

## [project-cli](cli/index.md)

**The Unlicence**

the cli is free and unencumbered software released into the public domain.

---

## documentation

**CC0 1.0 Universal**

all textual documentation content, by [Mark Joshwel](https://joshwel.co), is marked with
[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

the site itself was built with MkDocs and Material for MkDocs, which are licenced as
follows:

- [**mkdocs**](https://github.com/mkdocs/mkdocs/) —
  project documentation with Markdown
  BSD-2-Clause Licence

- [**mkdocs-material**](https://github.com/squidfunk/mkdocs-material) —
  documentation framework on top of MkDocs
  MIT Licence
```

## developer handbook template

```markdown
# the developer's handbook

!!! abstract
    i (mark), heavily use nix for reproducible development environments across machines.
    here's why you might care:

    1. **reproducibility** — the exact same tools, versions, and configurations
       - what does this mean for you? no "works on my machine" issues

    2. **isolation** — development dependencies don't pollute your system
       - what does this mean for you? easy cleanup, no conflicts

    3. **declarative** — everything is defined in code (flake.nix)
       - what does this mean for you? onboarding is just `nix develop`

    tl;dr: if you have nix, just run `nix develop` and you're good (●'◡'●)

---

## project

### environment setup

!!! note
    all prerequisite software are available in a nix flake. enter with `nix develop`

prerequisite software:

- [Python 3.12+](https://www.python.org/)
- [uv](https://github.com/astral-sh/uv): fast python package installer

to start a development environment:

```text
uv sync
```

### workflow for python code

1. write code
2. check with mypy and ruff:
    1. `mypy src/`
    2. `ruff check src/`
    3. `ruff format src/`

    !!! note
        alternatively, run `check.sh` inside `src/project/`

3. test your changes

### workflow for documentation

1. write markdown
2. run it through a spell checker
3. ensure line length is under 100 characters
4. documentation should be readable as-is in a code editor, **not the markdown preview**

i personally don't use a linter for markdown files — if it looks good on my code editor,
then whatever :)

### versioning

format: `YEAR.MAJOR.MINOR[-PRERELEASE]`
example: `2024.0.0`, `2024.0.0-beta`
change: update the `__version__` variable in `src/project/__init__.py`

the year resets major and minor when it changes. breaking changes bump major within
the same year.
```

## changelog template

```markdown
# changelog

## project v2.1.0

(released on the 14th of October 2023)

!!! warning
    this release contains breaking API changes. see [what's changed](#whats-changed)

quality of life improvements and bug fixes

### what's new

- added `--verbose` flag for detailed output
- added support for stdin input with `-`

### what's changed

- deprecated `old_function()` in favour of `new_function()`
- renamed `Config` class to `Settings`

### what's fixed

- fixed crash when input file doesn't exist
- fixed incorrect timezone handling

### thanks!

- [contributor](https://github.com/contributor) for their first contribution!
- [helper](https://github.com/helper) for reporting the timezone bug

full changelog: <https://github.com/user/project/compare/v2.0.0...v2.1.0>

---

## project v2.0.0

(released on the 1st of July 2023)

the great api break

### what is new

- completely rewritten core module
- new plugin architecture

### what has been removed

- removed deprecated `legacy_mode` option
- removed Python 3.8 support

### what has remained

- all CLI flags remain compatible
- configuration file format unchanged

### what has changed

detailed parameter changes:

1. `process(input)` → `process(input, options=None)`
2. `Result.value` → `Result.data`
3. `Error.message` → `Error.details`

full changelog: <https://github.com/user/project/compare/v1.0.0...v2.0.0>
```

## API reference template

```markdown
## api reference

### class project.Settings

configuration container for project behaviour.

- signature:
  ```python
  class Settings:
      def __init__(
          self,
          verbose: bool = False,
          output_format: str = "text",
      ) -> None: ...
  ```

- attributes:
  - `verbose: bool` — enable detailed logging
  - `output_format: str` — one of "text", "json", or "markdown"

- usage:
  ```python
  from project import Settings

  settings = Settings(verbose=True, output_format="json")
  ```

---

### def project.process()

main processing function.

- signature:
  ```python
  def process(
      input: str | Path,
      settings: Settings | None = None,
  ) -> Result: ...
  ```

- arguments:
  - `input: str | Path` — file path or raw content to process
  - `settings: Settings | None` — configuration options (uses defaults if None)

- returns: `Result` — processing result with `.data` and `.metadata`

- raises:
  - `InputError` — when input is invalid or unreadable
  - `ProcessingError` — when processing fails

- usage:
  ```python
  from project import process, Settings

  result = process("input.txt")
  print(result.data)

  # with custom settings
  result = process("input.txt", Settings(verbose=True))
  ```
```

## CLI documentation template

embed full `--help` output:

```markdown
## usage

```text
$ project --help
usage: project [-h] [-v] [-o FORMAT] [-q] [input]

process input files

positional arguments:
  input                 input file (or - for stdin)

options:
  -h, --help            show this help message and exit
  -v, --verbose         enable verbose output
  -o FORMAT, --output FORMAT
                        output format: text, json, markdown (default: text)
  -q, --quiet           suppress all output except errors
```

### querying

project accepts various input types:

1. file path: `project document.txt`
2. stdin: `cat document.txt | project -`
3. URL: `project https://example.com/document.txt`

### examples

1. basic usage

   ```text
   project input.txt
   ```

2. verbose json output

   ```text
   project -v -o json input.txt
   ```

3. process from stdin

   ```text
   echo "content" | project -
   ```
```

## environment variable documentation

```markdown
## configuration

project is configured via environment variables:

1. `PROJECT_VERBOSE`  
   enable verbose logging

   ```text
   PROJECT_VERBOSE=1
   ```

   setting it to `n` or `0` will be treated as disabled.

2. `PROJECT_OUTPUT_DIR`  
   directory for output files

   ```text
   PROJECT_OUTPUT_DIR=/path/to/output
   ```

   !!! warning
       this directory must exist and be writable

3. `PROJECT_CONFIG_FILE`  
   path to configuration file (optional)

   ```text
   PROJECT_CONFIG_FILE=~/.config/project/config.toml
   ```

   if not set, project looks in the current directory for `project.toml`.
```
