import pytest

from app.function_object import (
    StringConvertor,
    configure_case_converter,
    convert_string_based_on_ask,
    get_string_case_converter,
    greet,
    greet_using,
    stored_functions,
)


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


def test_function_can_be_passed_to_other_function():
    def loud(text: str) -> str:
        return text.upper()

    def soft(text: str) -> str:
        return text.lower()

    assert greet_using(soft) == "hi there!"


def test_function_can_be_nested():
    text = "Hello World"
    assert convert_string_based_on_ask(text, is_lowercase=True) == text.lower()
    assert convert_string_based_on_ask(text, is_lowercase=False) == text.upper()


def test_function_can_be_returned():
    lower_func = get_string_case_converter("lower")
    assert lower_func("HELLO") == "hello"
    upper_func = get_string_case_converter("upper")
    assert upper_func("hello") == "HELLO"


def test_function_can_capture_local_state():
    text = "Hello"
    lower_func = configure_case_converter(text, "lower")
    upper_func = configure_case_converter(text, "upper")
    # Lexical closure with text already configured.
    assert lower_func() == "hello"
    assert upper_func() == "HELLO"


def test_object_can_behave_like_function():
    text = "Hello"
    lower = StringConvertor("lower")
    assert lower(text) == "hello"
    upper = StringConvertor("upper")
    assert upper(text) == "HELLO"

    assert callable(lower)
    assert callable(upper)
    assert callable(text) is False
