from app.greeting import greet


def test_greet():
    assert greet("hi") == "hi, there!"
