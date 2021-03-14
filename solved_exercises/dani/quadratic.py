import pytest
from cmath import sqrt


def polynome(a, b, c):
    """This function calculates values of a univariate quadratic equation
    x1 = -b + sqrt(b^2 - 4ac)
    x2 = -b - sqrt(b^2 - 4ac)
    """
    if not all(isinstance(i, (int, complex, float)) for i in [a, b, c]):
        raise TypeError()

    if a == 0:
        raise ZeroDivisionError(a)

    factor = b ** 2 - (4 * a * c)
    print(factor)
    x = (-b + sqrt(factor)) / 2
    y = (-b - sqrt(factor)) / 2
    return x, y


def test_polynome_valid_inputs():
    assert polynome(1, 4, 3) == ((-1), (-3))
    assert polynome(1, -4, 3) == ((3), (1))
    assert polynome(1, 2, 2) == ((-1 + 1j), (-1 - 1j))
    assert polynome(1, 2j, -2) == ((-1j + 1), (-1j - 1))


def test_polynome_zero_division():
    with pytest.raises(ZeroDivisionError):
        polynome(0, 4, 3)


def test_polynome_invalid_inputs():
    with pytest.raises(TypeError):
        polynome("a", 4, 3)
    with pytest.raises(TypeError):
        polynome(0, "a", 3)
