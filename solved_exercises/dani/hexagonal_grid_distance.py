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
    for row in grid:
        print(row)
    elements = []
    for y, row in enumerate(grid):
        for x, element in enumerate(row):
            if element == "x":
                elements.append((y, x))

    x1, x2 = elements
    diff_cols = abs(x1[1] - x2[1])
    diff_rows = abs(x1[0] - x2[0])
    
    # any diagonal move is using same number of moves on row and columns
    if diff_cols <= diff_rows:
        # the shortest path is done only from diagonal movements
        # the rows diff is the shortest path is equal to diag movements
        value = diff_rows
    else:
        # diagonal movements can be done up to min of diff rows and diff columns
        # the shortest path is rows diff + remaining colums as horizontal movements
        # remaining columns movements are divide by 2 because of horizinatl gaps
        value = diff_rows + (diff_cols - diff_rows) / 2
        
    return value


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
                " o o o o o o o o o ",
                "  o o o o o o o o  ",
                "   o o o o o o o   ",
                "    o o o o o o    ",
                "     o x o o o     ",
            ]
        )
        == 8
    )
    assert (
        hex_distance(
            [
                "    o o o o o    ",
                "   o o o o o x   ",
                "  o o o o o o o  ",
                " o o o o o o o o ",
                "o o o o x o o o o",
                " o o o o o o o o ",
                "  o o o o o o o  ",
                "   o o o o o o   ",
                "    o o o o o    ",
            ]
        )
        == 4
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
                "     o o o o x     ",
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
                "     o o o o x     ",
                "    o o o o o o    ",
                "   x o o o o o o   ",
                "  o o o o o o o o  ",
                " o o o o o o o o o ",
                "  o o o o o o o o  ",
                "   o o o o o o o   ",
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
                "     x o o o o     ",
                "    o o o o o o    ",
                "   o o o o o o o   ",
                "  o o o o o o o o  ",
                " o o o o o o o o o ",
                "  x o o o o o o o  ",
                "   o o o o o o o   ",
                "    o o o o o o    ",
                "     o o o o o     ",
            ]
        )
        == 5
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

def main():
    test_hex_distance()

if __name__ == "__main__":
    main()
