"""Provide example usage of decorators in Python.

Key takeaways:
- *args and **kwargs allows to write functions that can take variable number
  of positional (*) and/or keyword (**) arguments. `args` and `kwargs` are
  naming conventions.
- args is a tuple of positional arguments and kwargs is a dictionary of
  keyword arguments.
"""


def add_numbers(*args: int) -> int:
    """Adds given list of numbers.

    Args:
      *args: A list of numbers as positional arguments.

    Returns:
      The sum of all numbers
    """
    sum = 0
    for i in args:
        sum += i
    return sum


def greet(**kwargs: str):
    """Returns a greeting text based on incoming key

    Args:
      *kwargs: A dictionary containing following keyword arguments:
        {
          'greeting': A string containing greeting,
          'text': A string containing following text
        }

    Returns:
        A greeting string composed using the keyword arguments.
    """
    greeting = kwargs.get("greeting", "hi")
    text = kwargs.get("text", "everyone")
    return f"{greeting}, {text}"


if __name__ == "__main__":
    print(add_numbers(1, 2, 3))
