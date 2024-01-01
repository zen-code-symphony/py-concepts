# Use of with.


from contextlib import contextmanager


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
        self.file = None

    def __enter__(self):
        print("__enter__ called")
        self.file = open(self.name)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("__exit__ called")
        if self.file:
            self.file.close()


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


if __name__ == "__main__":
    # Using class based context manager.
    with ManagedFile("assert.py") as f:
        print(f.read())

    # Using contextmanager decorator to define a generator-based function.
    with managed_file("with.py") as f:
        print(f.read())
