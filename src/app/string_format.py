"""Provide example usage of string formatting in Python.

Key takeaways:
- There is more than one way to handle string formatting in Python.
- A given use case should influence the choice of formating used.
- Picked from Dan's Python String Formatting Rule of Thumb:
  - If format strings are user-supplied, use Template Strings to
    avoid security issues.
  - Python 3.6+: use Literal String Interpolation.
  - < Python 3.6: use New Style String Formatting.
"""

from string import Template


def format_using_old_style_formatter(name):
    return "hello, %s" % name


def format_using_new_style_formatter(name):
    return "hello, {}".format(name)


def format_using_formatted_string_literal(name):
    return f"hello, {name}"


def format_using_template_strings(name):
    return Template("hello, $name").substitute(name=name)
