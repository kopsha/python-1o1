"""test module for optimal_change"""

from optimal_change import optimize_change
import pytest


def test_optimize_change():
    """positive tests"""
    available_coins = [5, 10, 25, 100]
    assert optimize_change(available_coins, 1) == []
    assert optimize_change(available_coins, 100) == [(1, 100)]
    assert optimize_change(available_coins, 15) == [(1, 10), (1, 5)]
    assert optimize_change(available_coins, 40) == [(1, 25), (1, 10), (1, 5)]
    assert optimize_change(available_coins, 400) == [(4, 100)]
    assert optimize_change(available_coins, 401) == []


def test_optimize_change_invalid_inputs():
    """negative tests"""
    available_coins = [1, 5, 10, 25, 100]

    with pytest.raises(TypeError):
        optimize_change(available_coins, 12.34)

    with pytest.raises(TypeError):
        optimize_change(available_coins, "42")

    with pytest.raises(ValueError):
        optimize_change(available_coins, -1)


if __name__ == "__main__":
    test_optimize_change()
    test_optimize_change_invalid_inputs()
