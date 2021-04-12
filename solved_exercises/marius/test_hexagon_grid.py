import pytest
from hexagon_grid import hex_distance


def test_hex_distance():

    assert (
        hex_distance(
            [
                "  o o  ",
                " o x o ",
                "  o x  ",
            ]
        )
        == 1
    )

    assert (
        hex_distance(
            [
                "  x o  ",
                " o o x ",
                "  o o  ",
            ]
        )
        == 2
    )

    assert (
        hex_distance(
            [
                "   o o o   ",
                "  o o o o  ",
                " o o o o o ",
                "  x o o x  ",
                "   o o o   ",
            ]
        )
        == 3
    )

    assert (
        hex_distance(
            [
                "   o x o   ",
                "  o x o o  ",
                " o o o o o ",
                "  o o o o  ",
                "   o o o   ",
            ]
        )
        == 1
    )

    assert (
        hex_distance(
            [
                "    o o o o    ",
                "   o o o o o   ",
                "  x o o o o o  ",
                " o o o o o o o ",
                "  o o o o o x  ",
                "   o o o o o   ",
                "    o o o o    ",
            ]
        )
        == 6
    )

    assert (
        hex_distance(
            [
                "    o o o o    ",
                "   o o x o o   ",
                "  o o o o o o  ",
                " o o o o o o o ",
                "  o o o o o o  ",
                "   o o x o o   ",
                "    o o o o    ",
            ]
        )
        == 4
    )

    assert (
        hex_distance(
            [
                "     x o o o o     ",
                "    o o o o o o    ",
                "   o o o o o o o   ",
                "  o o o o o o o o  ",
                " o o o o o o o o o ",
                "  o o o o o o o o  ",
                "   o o o o o o o   ",
                "    o o o o o o    ",
                "     o o o o x     ",
            ]
        )
        == 8
    )

    assert (
        hex_distance(
            [
                "     x o o o o     ",
                "    o o o o o o    ",
                "   o o o o o o o   ",
                "  o o o o o o o o  ",
                " o o o o o o o o o ",
                "  o o o o o o o o  ",
                "   o o o o o o o   ",
                "    o o o o o o    ",
                "     x o o o o     ",
            ]
        )
        == 8
    )

    assert (
        hex_distance(
            [
                "     o o o o x     ",
                "    o o o o o o    ",
                "   o o o o o o o   ",
                "  o o o o o o o o  ",
                " x o o o o o o o o ",
                "  o o o o o o o o  ",
                "   o o o o o o o   ",
                "    o o o o o o    ",
                "     o o o o o     ",
            ]
        )
        == 8
    )

    assert (
        hex_distance(
            [
                "     o o o o o     ",
                "    o o o o o o    ",
                "   o o o o o o o   ",
                "  o o o o o x o o  ",
                " o o o o o o o o o ",
                "  o o o o o o o o  ",
                "   o o o x o o o   ",
                "    o o o o o o    ",
                "     o o o o o     ",
            ]
        )
        == 3
    )

    assert (
        hex_distance(
            [
                "     o o o o o     ",
                "    o o o o o o    ",
                "   o x o o o o o   ",
                "  o o o o o x o o  ",
                " o o o o o o o o o ",
                "  o o o o o o o o  ",
                "   o o o o o o o   ",
                "    o o o o o o    ",
                "     o o o o o     ",
            ]
        )
        == 4
    )

    assert (
        hex_distance(
            [
                "     x o o o o     ",
                "    o o o o o o    ",
                "   o o o o o o o   ",
                "  o o o o o o o o  ",
                " o o o o o o o o o ",
                "  o o o o o o o o  ",
                "   o o o x o o o   ",
                "    o o o o o o    ",
                "     o o o o o     ",
            ]
        )
        == 6
    )

    assert (
            hex_distance(
                [
                    "     x o o o o     ",
                    "    o o o o o o    ",
                    "   o o o o o o o   ",
                    "  o o o o o o o o  ",
                    " o o o o o o o o o ",
                    "  o o o o o o o o  ",
                    "   o o x o o o o   ",
                    "    o o o o o o    ",
                    "     o o o o o     ",
                ]
            )
            == 6
    )

    assert (
        hex_distance(
            [
                "     o o o o o     ",
                "    o o o o o o    ",
                "   o o o o o o o   ",
                "  o o o o o o o o  ",
                " o o o o o o o o o ",
                "  o o o o o o o o  ",
                "   o o x x o o o   ",
                "    o o o o o o    ",
                "     o o o o o     ",
            ]
        )
        == 1
    )

    assert (
        hex_distance(
            [
                "     o o o o o     ",
                "    o o o o o o    ",
                "   o o o o o o o   ",
                "  o o o o o o o o  ",
                " o o o o o o o o o ",
                "  o x o o o o o o  ",
                "   o o o x o o o   ",
                "    o o o o o o    ",
                "     o o o o o     ",
            ]
        )
        == 3
    )
