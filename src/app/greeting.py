# greeting.py

"""Provide utility greeting related functions.

The module contains the following functions:

- `greet(greeting_prefix)` - Returns the greeting with given greeting_prefix.
"""


def greet(greeting_prefix: str) -> str:
    """Greet using the specific greeting prefix.

    Examples:
        >>> greet("hi")
        'hi, there!'
        >>> greet("hello")
        'hello, there!'

    Args:
        greeting_prefix: A string representing the greeting prefix to be used.

    Returns:
        A string representing the greeting.
    """
    return "{}, there!".format(greeting_prefix)
