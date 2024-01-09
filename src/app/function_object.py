"""Provide examples of functions as first-class objects in Python.

Key takeaways:
- Everything in Python is an object including functions. Functions can be
  assigned to variables, stored in data structures, passed to / returned from
  functions.
"""


def greet(text):
    """Returns given test in upper case."""
    return f"{text}!".upper()


def stored_functions():
    # Store functions in a data structure.
    return [greet, str.lower]


def greet_using(func):
    """Returns greeting by applying the passed function."""
    return func("Hi there!")


def convert_string_based_on_ask(text, is_lowercase):
    """Converts the given string to upper or lower case using inner func."""

    def upper(text: str) -> str:
        return text.upper()

    def lower(text: str) -> str:
        return text.lower()

    if is_lowercase:
        return lower(text)
    else:
        return upper(text)


def get_string_case_converter(converter_type):
    """Returns a string converter for the requested type."""

    def upper(text: str) -> str:
        return text.upper()

    def lower(text: str) -> str:
        return text.lower()

    if converter_type == "lower":
        return lower
    elif converter_type == "upper":
        return upper
    return None
