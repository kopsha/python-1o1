"""test module for optimal_change"""

from optimal_change import optimize_change

import pytest

def test_optimize_change():
    available_coins = [1, 5, 10, 25, 100]
    assert optimize_change(available_coins, 1) == [1]
    assert optimize_change(available_coins, 100) == [100]
    assert optimize_change(available_coins, 15) == [5, 10]
    assert optimize_change(available_coins, 40) == [5, 10, 25]

def test_optimize_change_invalid_inputs():
    available_coins = [1, 5, 10, 25, 100]

    with pytest.raises(TypeError):
        optimize_change(available_coins, 12.34)
        optimize_change(available_coins, "42")

    with pytest.raises(ValueError):
        optimize_change(available_coins, -1)
