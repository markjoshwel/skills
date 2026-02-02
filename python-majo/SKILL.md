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

All Python files must include a license header.

**Canonical header format:**

```python
"""
project-name: brief description
  with all my heart, 2024-2025, mark joshwel <mark@joshwel.co>
  SPDX-License-Identifier: Unlicense OR 0BSD
"""
```

Key points:
- First line: project name and brief description
- Second line: attribution with year range (indented 2 spaces)
- Third line: SPDX identifier (indented 2 spaces)
- Use year range for ongoing projects (e.g., `2024-2025`), single year for one-off scripts

**Standard file organisation:**

```python
"""
project-name: brief description
  with all my heart, 2024-2025, mark joshwel <mark@joshwel.co>
  SPDX-License-Identifier: Unlicense OR 0BSD
"""

# Standard library imports
from pathlib import Path
from typing import Final, NamedTuple

# Third-party imports (prefix to avoid pollution)
from somelib import Thing as _Thing

# Local imports
from .utils import Result

# === Constants ===
VERSION: Final[str] = "1.0.0"

# === Type Aliases ===
Query: TypeAlias = str | Path

# === Exceptions ===
class ProjectError(Exception): ...

# === Data Types ===
class Config(NamedTuple):
    debug: bool = False

# === Helper Functions ===
def _internal_helper(): ...

# === Core Functions ===
def process(config: Config) -> Result[Output]: ...

# === CLI ===
def cli() -> int: ...

if __name__ == "__main__":
    exit(cli())
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

## Data Types

### NamedTuple Over Dataclass

**Strongly prefer `NamedTuple` for structured data.** Only use `dataclass` when mutability is required.

```python
# ✅ PREFERRED - NamedTuple (immutable, hashable, unpacking)
class Behaviour(NamedTuple):
    """typed configuration object"""
    query: str | list[str] = ""
    geocoder: SurplusGeocoderProtocol = default_geocoding.geocoder
    debug: bool = False

class AfterlifeValues(NamedTuple):
    # grouped with comments
    lust: float
    gluttony: float
    greed: float

# ❌ AVOID - dataclass (unless mutability required)
@dataclass
class Config:
    debug: bool = False
```

**When to use dataclass**: Only when you need mutability, and prefer `@dataclass(frozen=True)` when possible.

### Result Type Pattern

Use a railway-oriented `Result` type for safe error handling. See [examples/result_type.py](examples/result_type.py) for the full implementation.

**Core pattern:**

```python
class Result(NamedTuple, Generic[ResultType]):
    """
    result type for safe value retrieval
    
    - Falsy when error is present (use `if not result:`)
    - `.get()` returns value or raises stored error
    - `.cry()` raises error or returns error as string
    """
    value: ResultType
    error: BaseException | None = None

    def __bool__(self) -> bool:
        return self.error is None

    def get(self) -> ResultType:
        if self.error is not None:
            raise self.error
        return self.value

    def cry(self, string: bool = False) -> str:
        if self.error is None:
            return ""
        if string:
            return f"({self.error.__class__.__name__}) {self.error}"
        raise self.error
```

**Usage:**

```python
def parse_file(path: Path) -> Result[Data]:
    try:
        data = do_parsing(path)
        return Result(data)
    except Exception as exc:
        return Result(EMPTY_DATA, error=exc)

# Caller
result = parse_file(some_path)
if not result:
    print(f"error: {result.cry(string=True)}", file=stderr)
    exit(1)
data = result.get()
```

### Factory Methods

Use `from_*` static methods returning `Result`:

```python
class DaycircleDate(NamedTuple):
    day: int
    month: int
    year: int

    @staticmethod
    def from_str(date: str) -> Result["DaycircleDate"]:
        try:
            parts = date.split("-")
            return Result(DaycircleDate(int(parts[0]), int(parts[1]), int(parts[2])))
        except Exception as exc:
            return Result(DaycircleDate(0, 0, 0), error=exc)
```

### Exception Hierarchies

Use `...` (ellipsis) for empty class bodies:

```python
class SurplusError(Exception):
    """base exception for surplus"""

class NoSuitableLocationError(SurplusError): ...
class IncompletePlusCodeError(SurplusError): ...
class PlusCodeNotFoundError(SurplusError): ...
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

## Python-Specific Patterns

### Walrus Operator (`:=`)

Use assignment expressions for inline binding:

```python
# In conditionals
if (match := pattern.search(text)) is not None:
    process(match.group(1))

# In list comprehensions
results = [y for x in data if (y := transform(x)) is not None]

# With path operations
if (config := Path("config.toml")).exists():
    load_config(config)

# Creating and using directory
(output_dir := Path.cwd().joinpath("output")).mkdir(parents=True, exist_ok=True)
```

### Match/Case (Python 3.10+)

Use structural pattern matching for dispatch:

```python
# Command dispatch
match argv[1:]:
    case ["validate"]:
        validate()
    case ["process", filename]:
        process(Path(filename))
    case ["convert", *files]:
        for f in files:
            convert(Path(f))
    case _:
        print_usage()

# Type dispatch
match input_value:
    case str():
        return parse_string(input_value)
    case Path():
        return parse_file(input_value)
    case list():
        return [process(item) for item in input_value]
    case _:
        raise TypeError(f"unexpected type: {type(input_value)}")

# Tuple destructuring
match instruction:
    case (Operation.POINTER_LEFT, count):
        return f"left({count})"
    case (Operation.OUTPUT, 1):
        return "output()"
    case _:
        raise NotImplementedError(instruction)
```

### for...else Pattern

Use `else` clause after loops (runs only if loop completed without `break`):

```python
for candidate in candidates:
    if is_valid(candidate):
        result = candidate
        break
else:
    # Only runs if loop completed without break
    result = default_value
    print("warn: no valid candidate found, using default", file=stderr)
```

### Numbered Steps in main()

Use numbered comments to structure main functions:

```python
def main() -> None:
    # 0. parse arguments
    behaviour = parse_args()
    
    # 1. validate inputs
    if error := validate(behaviour):
        print(f"error: {error}", file=stderr)
        exit(1)
    
    # 2. load data
    data = load_data(behaviour.input_path)
    
    # 3. process
    result = process(data)
    
    # 4. output
    write_output(result, behaviour.output_path)
    
    # 5. cleanup
    cleanup()
```

### Jupyter-like Cells

For scripts meant for interactive development, use `# %%` cell markers:

```python
# %% setup
import ...
constants = ...

# %% get data
data = fetch_data()

# %% process
results = process(data)

# %% visualise
plot(results)
```

### Generator Functions

Use generators with `yield from` for nested iteration:

```python
def walk_targets(targets: list[Path]) -> Generator[Path, None, None]:
    for target in targets:
        if not target.exists():
            print(f"warn: '{target}' does not exist, skipping", file=stderr)
            continue
        
        if target.is_file():
            yield target
        elif target.is_dir():
            print(f"info: recursively entering '{target}'", file=stderr)
            yield from target.rglob("*")
```

### Nested Helper Functions

For scoped logic that shouldn't be module-level:

```python
def process_document(doc: Document) -> Result[Output]:
    def validate_section(section: Section) -> bool:
        # Only used within process_document
        return section.is_valid()
    
    def transform_content(content: str) -> str:
        # Captures doc from outer scope
        return content.replace(doc.old_pattern, doc.new_pattern)
    
    for section in doc.sections:
        if not validate_section(section):
            return Result(EMPTY, error=ValidationError(section))
        section.content = transform_content(section.content)
    
    return Result(Output(doc))
```

### Progress Bars

Use `tqdm` for progress bars, else use `rich` if already being used in the project.

```python
from tqdm import tqdm

# Basic iteration
for file in tqdm(files, desc="processing files"):
    process(file)

# With walrus operator
for idx, char in (pbar := tqdm(enumerate(source), desc="pass 1: parsing", unit="chars")):
    pbar.set_description(f"pass 1: {idx}/{len(source)}")

# Parallel processing
from tqdm.contrib.concurrent import process_map
results = process_map(process_file, files, desc="converting", max_workers=4)
```

### pathlib Exclusively

**Never use `os.path`; always use `pathlib.Path`:**

```python
from pathlib import Path

# Relative to script location
script_dir = Path(__file__).parent
config_file = script_dir.joinpath("config.toml")

# Home directory paths (XDG-like)
cache_dir = Path.home().joinpath(".cache/project")
data_dir = Path.home().joinpath(".local/share/project")
config_dir = Path.home().joinpath(".config/project")

# Create with parents
cache_dir.mkdir(parents=True, exist_ok=True)

# Modern Path operations
if path.exists() and path.is_file():
    content = path.read_text(encoding="utf-8")
    path.write_text(new_content, encoding="utf-8")
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
