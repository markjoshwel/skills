# Meadow Docstring Format (MDF)

A plaintext-first alternative documentation string style for Python.

## Why Another Format?

It's really just for me, but I think it's an okay-ish format:

- It's easy and somewhat intuitive to read and write, especially because it's just plaintext
- It closely follows Python syntax where it should, which includes type annotations

**(bonus!)** it works:
- Best on Zed
- Okay-ish on Visual Studio Code
- Eh on PyCharm

## The Format

The format is comprised of multiple sections:

### 1. Preamble (Required)

A mandatory short one-line description.

```python
"""a baker's confectionery, usually baked, a lie"""
```

### 2. Body (Optional)

A longer, potentially multi-line description.

```python
"""a baker's confectionery, usually baked, a lie

this is a longer description that explains more about cakes
and why they might be lies in certain contexts.
"""
```

### 3. Accepted (Incoming) Signatures

For classes: `attributes`  
For functions: `arguments` or `parameters`

General format:
```text
{attributes,arguments,parameters}:
    `<python variable declaration syntax>`
        <description>
```

Example:
```python
"""
attributes:
    `name: str`
        name of the cake
    `ingredients: list[Ingredient]`
        ingredients of the cake
    `baking_temperature: int = 4000`
        temperature in degrees kelvin
"""
```

### 4. Exported (Outgoing) Signatures

For modules: `functions`  
For classes: `methods`

General format:
```text
{functions,methods}:
    `<python function declaration syntax without trailing colon>`
        <description of the function>
```

Example:
```python
"""
methods:
    `def bake(self, override: BakingOverride | None = None) -> bool`
        bakes the cake and returns True if successful
"""
```

### 5. Returns and Raises

**Single type format:**
```text
{returns,raises}: `<return type annotation>`
    <description>
```

**Multiple types format:**
```text
{returns,raises}:
    `<first possible return type annotation/exception class>`
        <description>
    `<second possible return type annotation/exception class>`
        <description>
```

Examples:
```python
def certain_unsafe_div(a: int | float, b: int | float) -> float:
    """divide a by b

    arguments:
        `a: int | float`
            numerator
        `b: int | float`
            denominator

    raises:
        `ZeroDivisionError`
            raised when denominator is 0
        `OverflowError`
            raised when the resulting number is too big

    returns: `float`
        the result, a divided by b
    """
    return a / b
```

### 6. Usage (Optional)

A markdown triple backtick block with usage examples.

```python
"""
usage:
    ```python
    cake = Cake(name="Chocolate", ingredients=[...])
    result = cake.bake()
    ```
"""
```

### Section Layout

| Section | Required | Position |
|---------|----------|----------|
| 1. `preamble` | Yes | Start |
| 2. `body` | No | Start or End |
| 3. `accepted (incoming) signatures` | If applicable | Middle |
| 4. `exported (outgoing) signatures` | If applicable | Middle |
| 5. `returns` | If not None | Middle |
| 6. `raises` | If applicable | Middle |
| 7. `usage` | No | Start or End |

## Guidelines When Writing Docstrings

### What to Care About

**Use Latest Syntax**

Use the latest/most succinct forms of syntax, so even if a codebase is for Python 3.9:
```python
optional_argument: T | None = None
```

**External References**

Externally imported/third party classes should be referenced in full:

```python
class ThirdPartyExample(Exception):
    """blah blah

    attributes:
        `field_day: external.ExternalClass`
            blah blah

    methods:
        `def __init__(self, field_day: ExternalClass) -> None: ...`
            blah blah
    """
```

**Overloads**

If having a singular docstring for overloads, use variable declaration syntaxes that make sense:

```python
@overload
def get_field(self) -> object: ...

@overload
def get_field(self, default: DefaultT) -> Union[object, DefaultT]: ...

def get_field(self, default: object = None) -> object:
    """...

    arguments:
        `default: object | None = None`  # <- note: technically mismatches, but works
            ...

    returns: `object`
    """
    ...
```

### When to Not Care

**1. Classes Inherited for Namespacing**

```python
class TomlanticException(Exception):
    """base exception class for all tomlantic errors"""
    pass
```

**2. Return Descriptions When Painfully Obvious**

```python
def difference_between_document(
    self, incoming_document: TOMLDocument
) -> Difference:
    """returns a `tomlantic.Difference` namedtuple object of the incoming and
    outgoing fields that were changed between the model and the comparison document

    arguments:
        `incoming_document: tomlkit.TOMLDocument`

    returns: `tomlantic.Difference`
    """
    ...
```

## Frequently Questioned Answers

### Why do the `body` and `usage` sections appear multiple times?

Depending on your use case, you may have a postamble after the usage, or if your body is a postamble after the torso section (and other similar use cases depending on reading flow).

### What about custom text?

Any other text will just be parsed as-is as body text, so there's no stopping you from adding an `example:` section (but cross-IDE compatibility is finicky, especially with PyCharm).

### How does the parser detect sections?

The parser will only attempt compliance when matching a line with the following pattern:
```text
{attributes,arguments,parameters,functions,methods,returns,raises,usage}:
```

### What if a declaration is really long?

You _could_ split the declaration into multiple lines, all within the same indentation level. But unless your function takes in dozens of arguments, a single-line declaration is preferred due to much wackier differences in LSP popover rendering strategies across different mainstream editors.

```text
methods:
    `def woah_many_argument_function(
        ...
    ) -> None`
        blah blah blah blah blah blah
```

## Examples

### Class with Attributes and Methods

```python
class Result(NamedTuple, Generic[ResultType]):
    """typing.NamedTuple representing a result for safe value retrieval

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
        `def cry(self, string: bool = False) -> str: ...`
            method that returns the result value or raises an error
    """

    value: ResultType
    error: BaseException | None = None

    def __bool__(self) -> bool:
        """boolean comparison for truthiness-based exception safety
        
        returns: `bool`
            that returns True if `self.error` is not None
        """
        ...

    def cry(self, string: bool = False) -> str: ...  # noqa: FBT001, FBT002
        """raises or returns an error if the Result is erroneous

        arguments:
            `string: bool = False`
                if `self.error` is an Exception, returns it as a string error message
        
        returns: `str`
            returns `self.error` if it is a string, or returns an empty string if
            `self.error` is None
        """
        ...

    def get(self) -> ResultType:
        """returns the result value or raises an error

        returns: `ResultType`
            returns `self.value` if `self.error` is None

        raises: `BaseException`
            if `self.error` is not None
        """
        ...
```

### Complex Class with Usage

```python
class ModelBoundTOML(Generic[M]):
    """glue class for pydantic models and tomlkit documents

    attributes:
        `model: BaseModel`

    methods:
        `def __init__(self, model: type[M], document: TOMLDocument, handle_errors: bool = True) -> None: ...`
            instantiates the class with a `pydantic.BaseModel` and a `tomlkit.TOMLDocument`
        `def model_dump_toml(self) -> TOMLDocument: ...`
            dumps the model as a style-preserved `tomlkit.TOMLDocument`
        `def get_field(self, location: str | Sequence[str], default: object | None = None) -> object | None: ...`
            safely retrieve a field by it's location
        `def set_field(self, location: str | Sequence[str], value: object) -> None: ...`
            sets a field by it's location
        `def from_another_model_bound_toml(cls, model_bound_toml: ModelBoundToml[M]) -> "ModelBoundToml": ...`
             classmethod that fully initialises from the data from another ModelBoundToml

    usage:
        ```py
        # instantiate the class
        toml = ModelBoundTOML(YourModel, tomlkit.parse(...))
        # access your model with .model
        toml.model.message = "blowy red vixens fight for a quick jump"
        # dump the model back to a toml document
        toml_document = toml.model_dump_toml()
        # or to a toml string
        toml_string = toml.model_dump_toml().as_string()
        ```
    """

    def set_field(
        self,
        location: Union[str, tuple[str, ...]],
        value: object,
        handle_errors: bool = True,
    ) -> None:
        """sets a field by it's location.
        
        not recommended for general use due to a lack of type safety, but useful when
        setting fields programatically

        will handle `pydantic.ValidationError` into more toml-friendly error messages.
        set `handle_errors` to `False` to raise the original `pydantic.ValidationError`

        arguments:
            `location: Union[str, tuple[str, ...]]`
                dot-separated location of the field to set
            `value: object`
                value to set at the specified location
            `handle_errors: bool = True`
                whether to convert pydantic ValidationErrors to tomlantic errors

        raises:
            `AttributeError`
                if the field does not exist
            `tomlantic.TOMLValidationError`
                if the document does not validate with the model
            `pydantic.ValidationError`
                if the document does not validate with the model and `handle_errors` is `False`
        """
        ...
```

## Format Summary

| Section | Required | Syntax |
|---------|----------|--------|
| preamble | Yes | Plain text |
| body | No | Plain text |
| attributes/arguments/parameters | If applicable | `` `name: Type` `` + description |
| functions/methods | If applicable | `` `def name(...) -> Return` `` + description |
| returns | If not None | `` `ReturnType` `` + description |
| raises | If applicable | `` `ExceptionClass` `` + description |
| usage | No | Code block with example |

**Always use backticks** around Python code in docstrings.
