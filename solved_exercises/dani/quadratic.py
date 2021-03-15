import pytest
from cmath import sqrt


def solve_quadratic_polynome(a, b, c):
    """This function calculates values of a univariate quadratic equation
    x1 = (-b + sqrt(b^2 - 4ac))/2a
    x2 = (-b - sqrt(b^2 - 4ac))/2a
    """
    for i in [a, b, c]:
        if not isinstance(i, (int, complex, float)):
            raise TypeError()

    delta = pow(b, 2) - (4 * a * c)
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    return x1, x2


def test_solve_quadratic_polynome_valid_inputs():
    assert solve_quadratic_polynome(1, 4, 3) == (-1, -3)
    assert solve_quadratic_polynome(4, -1, 0) == (0.25, 0)
    assert solve_quadratic_polynome(4, 0, 0) == (0, 0)
    assert solve_quadratic_polynome(1, 0, -1) == (1, -1)
    assert solve_quadratic_polynome(1, -4, 3) == (3, 1)
    assert solve_quadratic_polynome(1, 2, 2) == (-1 + 1j, -1 - 1j)
    assert solve_quadratic_polynome(1, 2j, -2) == (-1j + 1, -1j - 1)
    assert solve_quadratic_polynome(1j, 2j, 0) == (0, -2)
    assert solve_quadratic_polynome(1j, 2j, 1j) == (-1, -1)


def test_solve_quadratic_polynome_zero_division():
    with pytest.raises(ZeroDivisionError):
        solve_quadratic_polynome(0, 4, 3)


def test_solve_quadratic_polynome_invalid_inputs():
    with pytest.raises(TypeError):
        solve_quadratic_polynome("a", 4, 3)
    with pytest.raises(TypeError):
        solve_quadratic_polynome(0, "a", 3)
    with pytest.raises(TypeError):
        solve_quadratic_polynome(0, 5, "a")
