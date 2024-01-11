from app.lambdas import make_multiplier, sort_tuples_using_key


def test_closure_with_lambda():
    multiply_3 = make_multiplier(3)
    assert multiply_3(10) == 30


def test_use_as_key_function_to_sort():
    values = [(12, "b"), (100, "a"), (400, "c")]
    new_values = sort_tuples_using_key(values)
    assert new_values == [(100, "a"), (12, "b"), (400, "c")]
