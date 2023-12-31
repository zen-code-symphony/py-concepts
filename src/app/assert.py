# Use of assert.


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
