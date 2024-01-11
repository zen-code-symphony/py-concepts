"""Provide example usage of decorators in Python.

Key takeaways:
- Decorators can be used to define reusable behavior without modifying the
  underlying callable being decorated.
- `@<decorator_name>` is a shorthand syntax vs `decorator_name(func)`.
- Multiple decorators can be stacked from bottom to top on a callable. The
  order of call is from bottom to top.
- Use `functools.wraps` to maintain the metadata of the function being
  decorated.
- Remember decorators are nested function calls with closures involved so
  there is a performance cost. Stacking multiple decorators can result in
  performance overhead. Use it based on use case in hand.
"""

import functools


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


def toupper_with_args(func):
    def wrapped_func(*args, **kwargs):
        returned_value = func(*args, **kwargs)
        if type(returned_value) is str:
            return returned_value.upper()
        return returned_value

    return wrapped_func


def toupper_with_metadata(func):
    """Decorates while maintaining metadata of decorated function.

    Args:
        func: A callable (function) to decorate.

    Returns:
        A string in uppercase if return value of decorated function
        is of type str; non-str value otherwise.
    """

    @functools.wraps(func)
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


@toupper_with_args
def greet_with_args(greeting, name):
    return f"{greeting} {name}!"


@toupper_with_metadata
def greet_with_metadata():
    return "hi"


if __name__ == "__main__":
    # Returned string uppercase'd.
    print(f"upper: {greet()}")
    # No-op. Original function gets called.
    print(f"no-op: {greetnoop()}")
    # Decorator stacking.
    print(f"decorator stacking: {get_title()}")
    # Decorator with args.
    print(f"decorator with args: {greet_with_args('hi', 'there')}")
    # Decorator that maintains metadata.
    print(f"upper: {greet_with_metadata()}")
    print(greet_with_metadata.__name__)
    print(greet_with_metadata.__doc__)
