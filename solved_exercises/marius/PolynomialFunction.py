import cmath
import math

def calculate_polynomial_second_grade(a, b, c):
    """This function calculated the second grade polynomial"""
    delta = b ** 2 - 4 * a * c
    if delta == 0:
        x1 = -c/b
        x2 = x1
    else:
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    return x1, x2

def test_calculate_polynomial_second_grade():
    assert calculate_polynomial_second_grade(1, 1, -6) == (2.0, -3.0)
    assert calculate_polynomial_second_grade(2, 4, 2) == (-0.5, -0.5)
    assert calculate_polynomial_second_grade(1, 2, 2) == (-1+1j, -1-1j)
