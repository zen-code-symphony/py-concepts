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


def tohtmltitle(func):
    """Decorates the str output of given function with HTML title tag.

    Args:
        func: A callable (function) to decorate.

    Returns:
        An HTML <title> string if return value of decorated function
        is of type str; non-str value otherwise.
    """

    def wrapped_func():
        returned_value = func()
        if type(returned_value) is str:
            return f"<title>{returned_value}</title>"
        return returned_value

    return wrapped_func


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


@tohtmltitle
@toupper
def get_title():
    return "hello"


if __name__ == "__main__":
    # Returned string uppercase'd.
    print(f"upper: {greet()}")
    # No-op. Original function gets called.
    print(f"no-op: {greetnoop()}")
    # Decorator stacking.
    print(f"decorator stacking: {get_title()}")
