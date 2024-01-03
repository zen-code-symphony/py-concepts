from app.string_format import (
    format_using_formatted_string_literal,
    format_using_new_style_formatter,
    format_using_old_style_formatter,
    format_using_template_strings,
)

_FULL_TEXT = "hello, world"
_TEXT_SUFFIX = "world"


def test_format_using_old_style_formatter():
    assert format_using_old_style_formatter(_TEXT_SUFFIX) == _FULL_TEXT


def test_format_using_new_style_formatter():
    assert format_using_new_style_formatter(_TEXT_SUFFIX) == _FULL_TEXT


def test_format_using_formatted_string_literal():
    assert format_using_formatted_string_literal(_TEXT_SUFFIX) == _FULL_TEXT


def test_format_using_template_strings():
    assert format_using_template_strings(_TEXT_SUFFIX) == _FULL_TEXT
