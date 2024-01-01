# Use of assert.
#
# Key takeaways:
# - Debugging aid that performs an internal self-check.
# - Should only be used to help developers identify bugs. DO NOT use them to
#   handle run-time errors.
# - Remember, asserts can be disabled via interpreter setting (-O, -OO) so
#   don't count on an assert's presence.


def subtract(a: int, b: int) -> int:
    """Subtracts b from a.

    Args:
        a: An integer representing the first number.
        b: An integer representing the second number.

    Returns:
        The result of subtract operation.
    """
    # For simplicity, just imagine b > a is an impossible condition
    # as per the business logic.
    assert b < a, "b should be less than a"
    return a - b


if __name__ == "__main__":
    # Should pass assertion.
    print("10 - 4 is {}".format(subtract(10, 4)))
    # Should fail assertion. Passing -O with python command should skip
    # the assertion.
    print("10 - 14 is {}".format(subtract(10, 14)))
