def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def test_add_function():
    result = add_numbers(5, 3)
    assert result == 8


def test_multiply_function():
    result = multiply_numbers(4, 2)
    assert result == 8