from app.decorators import (
    noop,
    tohtmltitle,
    toupper,
    toupper_with_args,
    toupper_with_metadata,
)


def test_noop_does_nothing_and_returns_original_function():
    @noop
    def greet():
        return "hi"

    assert noop(greet) == greet
    assert greet() == "hi"


def test_toupper_changes_returned_value_to_uppercase_if_string():
    @toupper
    def greet():
        return "hi"

    assert toupper(greet) != greet
    assert greet() == "HI"

    @toupper
    def get_number():
        return 1

    assert get_number() == 1


def test_decorator_stacking():
    @tohtmltitle
    @toupper
    def get_title():
        return "learn decorator"

    assert get_title() == "<title>LEARN DECORATOR</title>"


def test_decorator_to_maintain_args_kwargs():
    @toupper_with_args
    def greet(greeting, name):
        return f"{greeting} {name}!"

    assert greet("hi", "there") == "HI THERE!"


def test_decorator_maintains_metadata_of_decorated_callable():
    @toupper_with_metadata
    def greet_with_metadata():
        """Greets with uppercase string."""
        return "hi"

    assert greet_with_metadata.__name__ == "greet_with_metadata"
    assert greet_with_metadata.__doc__ == "Greets with uppercase string."
