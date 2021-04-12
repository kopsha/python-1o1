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
    # if smaller or equal distance on columns than on lines >> distance = abs(x2-x1)
    # else distance = abs(x2 - x1) + (abs(y2 - y1) - (x2 - x1))//2
    points = []
    for index_line, line in enumerate(grid):
        for index_column, elem in enumerate(line):
            if elem == "x":
                points.append((index_line, index_column))
    
    if abs(points[1][1] - points[0][1]) <= abs(points[1][0] - points[0][0]):
        distance = abs(points[1][0] - points[0][0])
    else:
        distance = abs(points[1][0] - points[0][0]) + \
                    (abs(points[1][1] - points[0][1]) - (points[1][0] - points[0][0]))//2
    return distance


def main():
    hex_distance_input = [
        "   o o o   ",
        "  o o o o  ",
        " o o o o o ",
        "  x o o x  ",
        "   o o o   ",
    ]
    # distance = 3
    print(hex_distance(hex_distance_input))


if __name__ == "__main__":
    main()