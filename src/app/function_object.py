"""Provide examples of functions as first-class objects in Python.

Key takeaways:
- Everything in Python is an object including functions. Functions can be
  assigned to variables, stored in data structures, passed to / returned from
  functions.
"""


def greet(text):
    return f"{text}!".upper()


def stored_functions():
    # Store functions in a data structure.
    return [greet, str.lower]
