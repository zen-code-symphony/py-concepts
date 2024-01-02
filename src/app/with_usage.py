"""Provide example usage of `with` in Python.

Key takeaways:
- Simplify exception handling - encapsulate try/finally in context manager.
- Safe aquisition and release of system resources. Resources acquired and
  released automatically as part of entering and exiting the with context.
- Avoid resource leaks and make code easier to read.
"""

from contextlib import contextmanager
from typing import Self, TextIO, Union


class ManagedFile:
    """Represents a file with managed using context manager.

    Attributes:
        name: A string representing the name of the file.
        file: An instance of the actual file with the given file name.
    """

    def __init__(self, name: str) -> None:
        """Initializes the instance based on the given file name.

        Args:
            name: A string representing the name of the file to be managed.
        """
        self.name = name
        self.file: Union[None, TextIO] = None

    def __enter__(self) -> TextIO:
        self.file = open(self.name)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
            self.file = None


@contextmanager
def managed_file(name: str):
    """Manages the given file.

    Args:
        name: A string representing the name of a file to be managed.
    """
    try:
        f = open(name)
        yield f
    finally:
        f.close()


class PrintIndenter:
    """Manages nested indentation levels while printing text.

    Attributes:
        level: An integer representing the current level of indentation.
    """

    def __init__(self) -> None:
        self.level = 0

    def __enter__(self) -> Self:
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.level -= 1

    def print(self, text):
        """Prints the given text with the current indentation level."""
        print("    " * self.level + text)


if __name__ == "__main__":
    # Using class based context manager.
    with ManagedFile("assert.py") as f:
        print(f.read())

    # Using contextmanager decorator to define a generator-based function.
    with managed_file("with.py") as f:
        print(f.read())

    # Example application of context manager for managing indentation level.
    with PrintIndenter() as indenter:
        indenter.print("This")
        with indenter:
            indenter.print("is")
            with indenter:
                indenter.print("sooo")
        indenter.print("cool!")
