"""Provide example usage of decorators in Python.

Key takeaways:
"""


def noop(func):
    """Represents a no-op decorator that returns original function.

    Args:
        func: A callable (function) to decorate.

    Returns:
        The original input callable without any decorating behavior.
    """
    return func


def toupper(func):
    """Decorates given function by changing returned string to uppercase.

    Args:
        func: A callable (function) to decorate.

    Returns:
        A string in uppercase if return value of decorated function
        is of type str; non-str value otherwise.
    """

    def wrapped_func():
        returned_value = func()
        if type(returned_value) is str:
            return returned_value.upper()
        return returned_value

    return wrapped_func


@toupper
def greet():
    return "hi"


@noop
def greetnoop():
    return "hi"


if __name__ == "__main__":
    # Returned string uppercase'd.
    print(greet())
    # No-op. Original function gets called.
    print(greetnoop())
