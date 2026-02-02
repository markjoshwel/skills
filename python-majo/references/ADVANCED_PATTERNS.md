# Python Advanced Patterns (Mark)

Extended patterns and techniques for Python development. Load this file when you need detailed examples of specific patterns.

## Walrus Operator (`:=`)

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

## Match/Case (Python 3.10+)

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

## for...else Pattern

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

## Numbered Steps in main()

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

## Jupyter-like Cells

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

## Generator Functions

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

## Nested Helper Functions

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

## Progress Bars

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

## pathlib Operations

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

## Function Overloads

For overloaded functions, use variable declaration syntax that makes sense:

```python
@overload
def get_field(self) -> object: ...

@overload
def get_field(self, default: DefaultT) -> Union[object, DefaultT]: ...

def get_field(self, default: object = None) -> object:
    """...

    arguments:
        `default: object | None = None`
            ...

    returns: `object`
    """
```

## Long Declarations in Docstrings

Split long declarations across multiple lines within the same indentation:

```text
methods:
    `def woah_many_argument_function(
        ...
    ) -> None`
        blah blah blah blah blah blah
```

## External References in Docstrings

Reference externally imported/third party classes in full except for function signatures:

```python
class ThirdPartyExample(Exception):
    """blah blah

    attributes:
        `field_day: external.ExternalClass`  # <- full class path
          blah blah

    methods:
        `def __init__(self, field_day: ExternalClass) -> None: ...`  # <- note: class name only
            blah blah
    """
```

## Script Metadata (PEP 723)

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
