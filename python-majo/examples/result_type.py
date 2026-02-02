"""
result_type: Result NamedTuple for safe value retrieval (railway-oriented programming)
  with all my heart, 2024-2025, mark joshwel <mark@joshwel.co>
  SPDX-License-Identifier: Unlicense OR 0BSD
"""

from dataclasses import dataclass
from functools import wraps
from pathlib import Path
from typing import Callable, Generic, NamedTuple, ParamSpec, TypeVar


# === Result Type ===

ResultType = TypeVar("ResultType")


class Result(NamedTuple, Generic[ResultType]):
    """
    `typing.NamedTuple` representing a result for safe value retrieval

    attributes:
        `value: ResultType`
            value to return or fallback value if erroneous
        `error: BaseException | None = None`
            exception if any

    methods:
        `def __bool__(self) -> bool: ...`
            method for boolean comparison for exception safety
        `def get(self) -> ResultType: ...`
            method that raises or returns an error if the Result is erroneous
        `def cry(self, string: bool = False) -> str: ...`
            method that returns the result value or raises an error
    """

    value: ResultType
    error: BaseException | None = None

    def __bool__(self) -> bool:
        """
        method for boolean comparison for easier exception handling

        returns: `bool`
            that returns True if `self.error` is not None
        """
        return self.error is None

    def cry(self, string: bool = False) -> str:  # noqa: FBT001, FBT002
        """
        method that raises or returns an error if the Result is erroneous

        arguments:
            `string: bool = False`
                if `self.error` is an Exception, returns it as a string
                error message

        returns: `str`
            returns `self.error` as a string if `string` is True,
            or returns an empty string if `self.error` is None
        """

        if isinstance(self.error, BaseException):
            if string:
                message = f"{self.error}"
                name = self.error.__class__.__name__
                return f"{message} ({name})" if (message != "") else name

            raise self.error

        return ""

    def get(self) -> ResultType:
        """
        method that returns the result value or raises an error

        returns: `ResultType`
            returns `self.value` if `self.error` is None

        raises: `BaseException`
            if `self.error` is not None
        """
        if self.error is not None:
            raise self.error
        return self.value


# === Result Decorator ===

P = ParamSpec("P")
R = TypeVar("R")


def _result_wrap(default: R) -> Callable[[Callable[P, R]], Callable[P, Result[R]]]:
    """decorator that wraps a non-Result-returning function to return a Result"""

    def result_decorator(func: Callable[P, R]) -> Callable[P, Result[R]]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Result[R]:
            try:
                return Result(func(*args, **kwargs))
            except Exception as exc:
                return Result(default, error=exc)

        return wrapper

    return result_decorator


# =============================================================================
# USAGE EXAMPLES
# =============================================================================


# === Example 1: Factory Method Pattern ===
#
# Use @classmethod or @staticmethod returning Result for parsing/construction.
# This is the most common pattern for NamedTuple types.


class RepositoryFileState(NamedTuple):
    """represents the state of files in a git repository"""

    git_hash: str
    tracked_files: list[Path]
    dirty_files: list[Path]
    untracked_files: list[Path]

    @classmethod
    def init_from_repo(cls, repo: Path) -> Result["RepositoryFileState"]:
        """factory method that returns Result for safe error handling"""
        from subprocess import run

        try:
            # get current git commit hash
            hash_result = run(
                ["git", "rev-parse", "HEAD"],
                cwd=repo,
                capture_output=True,
                text=True,
                check=True,
            )

            return Result(
                value=cls(
                    git_hash=hash_result.stdout.strip(),
                    tracked_files=[],
                    dirty_files=[],
                    untracked_files=[],
                ),
            )

        except Exception as e:
            # return empty state with error attached
            return Result(
                value=cls(
                    git_hash="",
                    tracked_files=[],
                    dirty_files=[],
                    untracked_files=[],
                ),
                error=e,
            )


# === Example 2: Using the @_result_wrap Decorator ===
#
# Use this decorator to wrap functions that don't naturally return Result.
# Provide a default value that will be returned if an exception occurs.


@dataclass
class File:
    """a file with metadata"""

    path: Path
    checksum: str = ""
    mtime: float = 0.0

    @_result_wrap(default="")
    def resolve_checksum(self) -> str:
        """calculates the blake2b checksum of the file"""
        from hashlib import blake2b

        if self.checksum != "":
            return self.checksum

        contents = self.path.read_bytes()
        self.checksum = blake2b(contents).hexdigest()
        return self.checksum

    @_result_wrap(default=0.0)
    def resolve_mtime(self) -> float:
        """resolves the modification time from the file's path"""
        if self.mtime == 0.0:
            self.mtime = self.path.stat().st_mtime
        return self.mtime

    @_result_wrap(default=None)
    def resolve(self) -> None:
        """resolves all metadata fields, chaining .get() calls"""
        _ = self.resolve_mtime().get()
        _ = self.resolve_checksum().get()


# === Example 3: Checking Results ===
#
# Use boolean check (`if not result:`) then `.cry()` or `.get()`.


def example_check_result() -> int:
    """demonstrates checking and handling Result values"""
    from sys import stderr

    repo = RepositoryFileState.init_from_repo(Path.cwd())

    # pattern 1: check with if not, then cry(string=True) for error message
    if not repo:
        print(f"error: {repo.cry(string=True)}", file=stderr)
        return 1

    # pattern 2: use .get() after successful check (safe, won't raise)
    state = repo.get()
    print(f"git hash: {state.git_hash}")

    return 0


def example_chain_results() -> int:
    """demonstrates chaining multiple Result operations"""
    from sys import stderr

    file = File(path=Path("example.txt"))

    # pattern: chain .get() calls inside a try block
    # if any fail, the exception propagates
    try:
        _ = file.resolve_mtime().get()
        _ = file.resolve_checksum().get()
    except Exception as exc:
        print(f"error: failed to resolve file metadata: {exc}", file=stderr)
        return 1

    print(f"mtime: {file.mtime}, checksum: {file.checksum[:16]}...")
    return 0


def example_cry_patterns() -> int:
    """demonstrates the two cry() patterns"""
    from sys import stderr

    repo = RepositoryFileState.init_from_repo(Path.cwd())

    if not repo:
        # pattern 1: cry(string=True) returns error as string
        error_msg = repo.cry(string=True)
        print(f"error: {error_msg}", file=stderr)
        return 1

        # pattern 2: cry() with no args raises the exception
        # repo.cry()  # would raise the stored exception

    return 0


# === Example 4: Result with Initialisation Methods ===
#
# Common pattern: an init() method that returns Result for setup operations.


class Manager:
    """manager class with Result-returning init method"""

    data: dict[str, str]

    @_result_wrap(default=None)
    def init(self) -> None:
        """initialises the manager, returns Result for error handling"""
        self.data = {}
        # do setup that might fail...
        self._load_config()

    def _load_config(self) -> None:
        """internal method that might raise"""
        # ... loading logic ...
        pass


def example_init_pattern() -> int:
    """demonstrates the init() Result pattern"""
    from sys import stderr

    manager = Manager()

    # check if init succeeded
    if not (init_result := manager.init()):
        print(f"error: failed to init: {init_result.cry(string=True)}", file=stderr)
        return 1

    # now safe to use manager
    print(f"manager initialised with {len(manager.data)} items")
    return 0
