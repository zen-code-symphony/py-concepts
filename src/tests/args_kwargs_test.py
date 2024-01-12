from app.args_kwargs import add_numbers, greet


def test_args_can_accept_variable_number_of_arguments():
    assert add_numbers(1, 2, 3) == 6
    assert add_numbers(1, 2, 3, 4, 5, 6) == 21


def test_kwargs_can_be_used_for_keyword_arguments():
    kwargs = {"greeting": "hello", "text": "everyone"}
    text = greet(**kwargs)
    assert text == "hello, everyone"
