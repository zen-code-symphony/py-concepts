import pytest

from app.under_dunder import UnderDunder


@pytest.fixture(scope="module")
def under_dunder():
    return UnderDunder()


def test_single_leading_underscore_accesssed_as_member_variable(under_dunder):
    # Member accessible but naming convention is used to hint developers
    # about internal-only usage of the member.
    assert under_dunder._single_lead_under == "i'm _single_lead_under"


def test_dunder_cannot_be_accesssed_as_member_variable(under_dunder):
    with pytest.raises(AttributeError):
        # __dunder cannot be accessed via name access.
        _ = under_dunder.__dunder


def test_dunder_accesssed_via_mangled_name(under_dunder):
    # Member name is internally mangled.
    assert under_dunder._UnderDunder__dunder == "i'm __dunder"


def test_dunder_accesssed_via_method(under_dunder):
    # Can be accessed by method without mangled name access.
    assert under_dunder.get_dunder() == "i'm __dunder"


def test_single_trailing_underscore_keyword_member_variable(under_dunder):
    # Naming convention to avoid conflicts with Python keywords.
    assert under_dunder.class_ == "i'm class_"


def test_leading_trailing_dunder_accessible(under_dunder):
    # Avoid creating such methods as the naming convention is for special
    # methods in Python laguage. Avoid future conflict.
    assert under_dunder.__dunder__() == "avoid me"
