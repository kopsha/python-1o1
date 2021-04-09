"""Test module for tournament exercise"""

from tournament import tally_tournament, pretty_tournament

import pytest


def test_tally_tournament():
    text = """
Barcelona;Juventus;win
Dortmund;Chelsea;draw
Dortmund;Barcelona;win
Chelsea;Juventus;loss
Juventus;Dortmund;loss
Barcelona;Chelsea;win
"""
    expected = {
        "Dortmund": (3,  2,  1,  0,  7),
        "Barcelona":  (3,  2,  0,  1,  6),
        "Juventus": (3,  1,  0,  2,  3),
        "Chelsea": (3,  0,  1,  2,  1),
    }

    assert tally_tournament(text) == expected


def test_tally_tournament_invalid():
    with pytest.raises(TypeError):
        tally_tournament(-1)



def test_pretty_tournament():
    given = {
        "Dortmund": (3,  2,  1,  0,  7),
        "Barcelona":  (3,  2,  0,  1,  6),
        "Juventus": (3,  1,  0,  2,  3),
        "Chelsea": (3,  0,  1,  2,  1),
    }
    expected = """Team                          | MP | W  | D  | L  | P 
Dortmund                      | 3  | 2  | 1  | 0  | 7 
Barcelona                     | 3  | 2  | 0  | 1  | 6 
Juventus                      | 3  | 1  | 0  | 2  | 3 
Chelsea                       | 3  | 0  | 1  | 2  | 1 
"""
    assert pretty_tournament(given) == expected


if __name__ == '__main__':
    test_tally_tournament()
    test_tally_tournament_invalid()
    test_pretty_tournament()
