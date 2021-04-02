"""
A hexagonal grid is a commonly used game board design based on hexagonal tiling.
In the following grid, the two marked locations have a minimum distance of 6
because at least 6 steps are needed to reach the second location starting from
the first one.



Write a function that takes a hexagonal grid with two marked locations as input
and returns their distance.

The input grid will be a list of strings in which each tile is represented with
o and the two marked locations with x.

Examples
hex_distance([
  "  o o  ",
  " o x o ",
  "  o x  ",
]) ➞ 1

hex_distance([
  "  o o  ",
  " x o o ",
  "  o x  ",
]) ➞ 2

hex_distance([
  "   o o o   ",
  "  o o o o  ",
  " o o o o o ",
  "  x o o x  ",
  "   o o o   ",
]) ➞ 3
"""


def hex_distance(grid):
    pass


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
