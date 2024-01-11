from app.decorators import noop, tohtmltitle, toupper


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
