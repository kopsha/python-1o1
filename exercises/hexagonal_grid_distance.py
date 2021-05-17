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

import cmath
import math


def print_grid(g, label=None):
    if label:
        print(f" -- {label} --")
    for row in g:
        if isinstance(row, list):
            print(" >> ", " ".join(row))
        else:
            print(" >> ", row)


def distance_h(points):
    assert len(points) == 2
    x1, x2 = tuple(points)

    dy = abs(x2[0] - x1[0])
    dx = abs(x2[1] - x1[1])

    amin = min(dx, dy)
    amax = max(dx, dy)

    diagonalSteps = amin
    straightSteps = amax - amin

    print("\t >> diag, straight: ", diagonalSteps, straightSteps)

    result = round(diagonalSteps + straightSteps)

    return int(result)


def hex_distance_abandoned(grid):
    print("-" * 27)
    print_grid(grid, "given")

    assert len(grid) % 2 != 0
    n = len(grid)
    mid = len(grid) // 2
    sn = n + n - 1

    # print("streched", sn, "x", sn)
    # print("actual", n, "x", n)

    lim = (sn - n) // 2
    streched = [
        list(grid[i - lim])[1:-1] if lim <= i < sn - lim else list(" " * sn)
        for i in range(sn)
    ]
    print_grid(streched, "streched")

    rot45 = cmath.rect(math.sqrt(2), cmath.pi / 4)

    rotated = [list(" " * n) for _ in range(n)]
    points = []

    for r in range(sn):
        for c in range(sn):
            if streched[r][c] != " ":
                rr, rc = (r - n + 1) / 2, (c - n + 1) / 2
                # print((r, c), " => ", (rr, rc))
                z = rc + rr * 1j
                zr = z * rot45
                # print(z, zr)
                tr, tc = round(zr.imag), round(zr.real)
                # print((r, c), " => ", (tr, tc))

                abs_tr, abs_tc = tr + mid, tc + mid
                rotated[abs_tr][abs_tc] = streched[r][c]
                if streched[r][c] == "x":
                    points.append((abs_tr, abs_tc))

    print_grid(rotated, "rotated")
    dist = distance_h(points)
    print(points, "distance:", dist)

    return dist


def rough_distance(points):
    assert len(points) == 2
    x1, x2 = tuple(points)

    dr = abs(x2[0] - x1[0])
    dc = abs(x2[1] - x1[1])

    return max(dr, dc)


def hex_neighbours(point):
    r, c = point

    steps = [(0, 2), (-1, 1), (-1, -1), (0, -2), (1, -1), (1, 1)]
    neighbours = [(r + dr, c + dc) for dr, dc in steps]
    return neighbours


def hex_walk(points):
    start, finish = points
    path = []
    pos = start

    while pos != finish:
        path.append(pos)
        options = hex_neighbours(pos)
        dist = [(rough_distance((step, finish)), step) for step in options]
        _, closest = sorted(dist)[0]
        pos = closest

    print(" >>  distance: ", len(path))

    return len(path)


def hex_distance(grid):
    print("-" * 27)
    print_grid(grid, "the grid")

    points = []
    for ri, row in enumerate(grid):
        for ci, val in enumerate(row):
            if val == "x":
                points.append((ri, ci))

    return hex_walk(points)


def main():
    test_hex_distance()

    print(" -- finished --")


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


if __name__ == "__main__":
    main()
