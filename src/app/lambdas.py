"""Provide example usage of lambda in Python.

Key takeaways:
- Lambda functions are single-expression that are not necessarily bound to a
  name i.e. anonymous.
- Lambda functions cannot use regular Python statements and have implicit
  return statement.
- Use lambda function wisely. When using a regular function makes the code
  look cleaner and easy to understand - always prefer that instead of lambda
  wizardry.
"""


def sort_tuples_using_key(values):
    """Sorts given list of tuples using second value in the tuple."""
    return sorted(values, key=lambda x: x[1])


def make_multiplier(n):
    """Creates a multiplier function for 'n' using closure."""
    return lambda x: x * n


if __name__ == "__main__":
    multiply_3 = make_multiplier(3)
    print(f"10 x 3: {multiply_3(10)}")
    multiply_10 = make_multiplier(10)
    print(f"10 x 10: {multiply_3(10)}")
