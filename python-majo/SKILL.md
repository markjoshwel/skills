---
name: python-majo
description: Python development standards for Mark's workflow. Use when writing Python code. Covers UV project management, basedpyright type checking, ruff formatting, Meadow Docstring Format (MDF), and Python 3.10+ syntax preferences.
license: Unlicense
metadata:
  author: mark@joshwel.co
  version: "2026.2.2"
  requires: python>=3.10
---

# Python Development Standards (Mark)

Python-specific standards following modern tooling and type-safe practices.

## Project Management

**Use UV, not pip**

UV is the preferred project manager, runtime, and tool invoker. Check the project structure first to determine the appropriate tool, then fall back to UV if unsure.

```bash
# Check what the project uses
ls pyproject.toml  # UV/poetry/pipenv
ls poetry.lock     # Poetry
ls Pipfile         # Pipenv
ls requirements.txt # pip

# Project setup (UV)
uv init
uv add <package>
uv remove <package>

# Running commands (UV)
uv run <command>

# Quick tool invocation without installing
uvx <tool>
```

**Do NOT use**:
- `pip install` — use `uv add` instead
- `pip freeze` — use `uv pip freeze` or check `pyproject.toml`
- `poetry add` — use `uv add` instead (unless project already uses poetry)
- `pipenv install` — use `uv add` instead (unless project already uses pipenv)

**When in doubt**: Check for `pyproject.toml`, `poetry.lock`, `Pipfile`, or existing patterns in the codebase. Default to UV for new projects.

## Type Checking

Use both basedpyright and mypy for comprehensive type checking:

```bash
# Run all type checkers
uv run basedpyright
uv run mypy
```

### Diagnostic Suppression by Tool

**Basedpyright** (supports diagnostic-specific ignores):
```python
# Use specific diagnostic names
from typing_extensions import override  # pyright: ignore[reportMissingModuleSource]

# Multiple diagnostics
some_call()  # pyright: ignore[reportUnknownMemberType, reportUnknownVariableType]
```

**Mypy** (does NOT support diagnostic names):
```python
# Suppresses ALL diagnostics on the line
some_call()  # type: ignore
```

**Golden rule**: Exhaust all other options before using ignores:
1. **Type narrowing** - Use `isinstance()`, `hasattr()`, or guard clauses
2. **Type guards** - Use `TypeIs` from `typing_extensions` for custom narrowing
3. **Data contracts** - Define proper protocols or dataclasses
4. **Type stubs** - Create `.pyi` files for untyped third-party libraries
5. **Configuration fixes** - Adjust `pyproject.toml` settings properly

**Avoid**:
- Using `# noqa` for type errors
- Changing configuration just to silence warnings without understanding the root cause
- Adding ignores to "get it working" without documenting why it's necessary
- Using blanket ignores when specific ones are available (for basedpyright)

## Code Style

### Target Python 3.10+

Use modern syntax:

```python
# ✅ CORRECT - Python 3.10+ syntax
from __future__ import annotations

def process(items: list[str]) -> dict[str, int | None]:
    result: list[int] = []
    value: str | None = None
    ...

# ❌ WRONG - Old syntax
from typing import List, Dict, Union, Optional

def process(items: List[str]) -> Dict[str, Optional[int]]:
    result: List[int] = []
    value: Optional[str] = None
    ...
```

### File Structure

**All Python files must start with the full Unlicense header:**

```python
"""
module_name: brief description
--------------------------------
by mark <mark@joshwel.co>

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""
```

### Import Organization

Group imports in this order:
1. Standard library (alphabetical)
2. Third-party packages (alphabetical)
3. Local modules

```python
from argparse import ArgumentParser
from collections import OrderedDict
from datetime import datetime, timedelta, timezone
from enum import Enum
from pathlib import Path
from sys import stderr, stdout
from typing import TYPE_CHECKING, Final, NamedTuple

from tqdm import tqdm

from .utils import Result
```

### Constants

Use `Final` type and UPPER_CASE naming:

```python
# constants
VERSION: Final[str] = "2024.0.0"
MAX_RETRIES: Final[int] = 9
WAIT_SECONDS: Final[int] = 10
```

### Type Hints

Use explicit type annotations for clarity:

```python
# Function signatures
def handle_args() -> Behaviour:
    ...

# Constants with complex types
SHAREABLE_KEYS: Final[dict[str, tuple[str, ...]]] = {
    "default": ("emergency", "historic", ...)
}

# Variables
result: list[int] = []
config: dict[str, Any] = {}
```

### Comments

Use brief inline comments for non-obvious logic:

```python
# adjusts geocoder zoom level when geocoding lat long into an address
LOCALITY_GEOCODER_LEVEL: int = 13

# ignore the first two rows and 'adj' rows
next(data)
next(data)
```

### Error Handling

Print to stderr and use specific exit codes:

```python
from sys import stderr, exit as sysexit

# Error messages to stderr
print("error: surplus is not installed", file=stderr)

# Specific exit codes
exit(1)  # Bad command usage
exit(2)  # Bad target
exit(3)  # Could not send message
```

### Script Metadata (PEP 723)

For standalone scripts, include PEP 723 metadata:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "tqdm",
#     "ziglang",
# ]
# ///
```

### Ruff

Format and lint with ruff:

```bash
# Sort imports first (if new modules imported)
ruff check --select I --fix

# Format code
ruff format

# Check alongside basedpyright
ruff check
```

**Before formatting**: Sort imports if any module has been newly imported using `ruff check --select I --fix`.

## Documentation

### Meadow Docstring Format (MDF)

Use MDF for all docstrings. See [references/mdf-format.md](references/mdf-format.md) for complete specification.

**Quick Reference**:

```python
class Result(NamedTuple, Generic[ResultType]):
    """
    typing.NamedTuple representing a result for safe value retrieval

    attributes:
        `value: ResultType`
            value to return or fallback value if erroneous
        `error: BaseException | None = None`
            exception if any

    methods:
        `def __bool__(self) -> bool: ...`
            boolean comparison for truthiness-based exception safety
        `def get(self) -> ResultType: ...`
            method that raises or returns an error if the Result is erroneous

    returns: `ResultType`
        returns `self.value` if `self.error` is None

    raises: `BaseException`
        if `self.error` is not None
    """
```

**Key Points**:
- Use backticks with Python syntax: `` `variable: Type` ``
- Sections: attributes/arguments, methods, returns, raises, usage
- Optional sections marked with square brackets in spec
- Use latest syntax even if codebase targets older Python

### When NOT to Document

1. **Namespace classes**:
```python
class TomlanticException(Exception):
    """base exception class for all tomlantic errors"""
    pass
```

2. **Obvious returns**:
```python
def difference_between_document(self, incoming_document: TOMLDocument) -> Difference:
    """
    returns a `tomlantic.Difference` namedtuple object of the incoming and
    outgoing fields that were changed between the model and the comparison document

    arguments:
        `incoming_document: tomlkit.TOMLDocument`

    returns: `tomlantic.Difference`
    """
```

## Type Safety Guidelines

### Explicit Types

- Use explicit types for function parameters and return values when they enhance clarity
- Prefer `unknown` over `any` when type is genuinely unknown
- Use const assertions (`as const`) for immutable values
- Leverage type narrowing instead of type assertions

### External References

Reference externally imported/third party classes in full except for function signatures:

```python
class ThirdPartyExample(Exception):
    """
    blah blah

    attributes:
        `field_day: external.ExternalClass`  # <- full class path
          blah blah

    methods:
        `def __init__(self, field_day: ExternalClass) -> None: ...`  # <- note: class name only
            blah blah
    """
```

### Overloads

For overloaded functions, use variable declaration syntax that makes sense:

```python
@overload
def get_field(self) -> object: ...

@overload
def get_field(self, default: DefaultT) -> Union[object, DefaultT]: ...

def get_field(self, default: object = None) -> object:
    """
    ...

    arguments:
        `default: object | None = None`  # <- note: technically mismatches overloads, but works
            ...

    returns: `object`
    """
```

## Workflow

### Before Writing Code

1. Check for existing `AGENTS.md` and read it
2. Understand codebase patterns from existing files
3. Identify Python version target (default to 3.10+)

### While Writing

1. Write type-annotated code
2. Use basedpyright and mypy to check types
3. Format with ruff
4. Sort imports if needed
5. Write MDF docstrings

### Before Committing

**Strict compliance required** — both type checkers must pass without sweeping errors under the rug:

```bash
# Type checking (strict mode)
uv run basedpyright
uv run mypy

# Format and lint
ruff check --select I --fix
ruff format
ruff check
```

**If type errors persist**, exhaust these options before using ignores:
1. Add runtime type checks with `isinstance()` or `hasattr()`
2. Use `TypeIs` from `typing_extensions` for custom type guards
3. Define Protocol classes for structural typing
4. Create type stubs (`.pyi` files) for untyped libraries
5. Adjust pyproject.toml configuration properly

**Only use ignores as a last resort**:
- For basedpyright: Use `# pyright: ignore[specificDiagnostic]` 
- For mypy: Use `# type: ignore`
- Always document why the ignore is necessary

## Temporary Scripts

You may write temporary scripts in Python as needed. Use `uvx` for one-off tools:

```bash
# Example: running a temporary analysis script
uv run python /tmp/analyze.py
```

## CLI Argument Handling

Choose the right tool based on complexity:

### Use `sys.argv` for simple scripts

When you only need to check a few simple flags without complex validation:

```python
import sys

# Simple flag checking
if "-h" in sys.argv or "--help" in sys.argv:
    print("Usage: script.py [-h] [-d] [-v]")
    sys.exit(0)

debug = "-d" in sys.argv or "--debug" in sys.argv
verbose = "-v" in sys.argv or "--verbose" in sys.argv

# Process remaining arguments
files = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
```

### Use `argparse` for complex scripts

When you need any of the following:
- Multiple positional arguments with validation
- Subcommands (like `git commit`, `git push`)
- Complex argument validation (type checking, choices, ranges)
- Automatic help text generation
- Required vs optional arguments with defaults
- Argument groups or mutually exclusive options

```python
import argparse

parser = argparse.ArgumentParser(description="Process some files")
parser.add_argument("files", nargs="+", help="files to process")
parser.add_argument("--format", choices=["json", "yaml", "toml"], default="json")
parser.add_argument("--verbose", "-v", action="store_true")
subparsers = parser.add_subparsers(dest="command")
# ... add subcommands

args = parser.parse_args()
```

### Decision Guidelines

**Use `sys.argv` when:**
- Only 2-5 simple boolean flags (no values)
- No positional arguments or just one simple one
- No validation beyond "is flag present?"
- Quick throwaway scripts

**Use `argparse` when:**
- Arguments have values that need validation
- Multiple positional arguments
- Subcommands needed
- Help text would be useful
- Type conversion required (integers, paths, etc.)
- Arguments have complex relationships (mutually exclusive, dependent)

The boundary is about complexity and maintainability, not just flag count. Even 6-8 simple flags might be fine in `sys.argv` if they're just boolean checks, but one positional argument with validation needs might warrant `argparse`.

## Integration

This skill extends `majo-standards`. Always ensure `majo-standards` is loaded for:
- AGENTS.md maintenance
- Universal code principles
- Documentation policies

Works alongside:
- `git-majo` — For committing Python code changes
- `docs-majo` — For writing Python API documentation
- `shell-majo` — For shell scripting within Python projects
