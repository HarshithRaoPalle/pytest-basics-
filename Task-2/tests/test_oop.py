class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


def test_calculator_add():
    calc = Calculator()
    result = calc.add(4, 3)

    assert result == 7


def test_calculator_multiply():
    calc = Calculator()
    result = calc.multiply(5, 2)

    assert result == 10