import pytest

from app.function_object import greet, stored_functions


def test_function_name_and_object_are_separate_concerns():
    new_greet = greet
    # Variable points to the same function object.
    assert new_greet == greet
    # Both return same result.
    assert new_greet("hi") == greet("hi")

    from app.function_object import greet as extra_greet

    ref_extra_greet = extra_greet
    # Name matches the function name as per function definition.
    assert extra_greet.__name__ == "greet"
    assert ref_extra_greet.__name__ == "greet"

    # Deleting a reference doesn't delete the function object.
    del extra_greet
    with pytest.raises(NameError):
        extra_greet  # noqa


def test_functions_can_be_stored_in_data_structures():
    funcs = stored_functions()
    # Function objects can be stored in list or other data strcutures.
    assert funcs[0] == greet
    assert funcs[1] == str.lower

    # They can be called without assigning to variable.
    assert funcs[0]("hi") == "HI!"  # greet
    assert funcs[1]("HI") == "hi"  # str.lower
