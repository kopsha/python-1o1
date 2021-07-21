"""
A maze can be represented by a 2D matrix, where 0s represent walkeable areas,
and 1s represent walls. You start on the upper left corner and the exit is on
the most lower right cell.

Create a function that returns true if you can walk from one end of the maze to
the other. You can only move up, down, left and right.
You cannot move diagonally.

Examples
can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]) ➞ true

can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
]) ➞ false

# This maze only has dead ends!

can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1]
]) ➞ false

# Exit only one block away, but unreachable!

can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 0]
]) ➞ true

Notes
In a maze of size m x n, you enter at [0, 0] and exit at [m-1, n-1].
There can be dead ends in a maze.
One exit path is sufficient.
"""


def find_exit(pos, exit_pos, visited, maze):
    row, col = pos
    if maze[row][col] != 0:
        return False

    if exit_pos == pos:
        return True

    possible_neighbours = [
        (row + 1, col),
        (row, col + 1),
        (row - 1, col),
        (row, col - 1),
    ]
    for next_pos in possible_neighbours:
        r, c = next_pos
        if 0 <= r <= exit_pos[0] and 0 <= c <= exit_pos[1] and next_pos not in visited:
            visited.append(next_pos)
            if find_exit(next_pos, exit_pos, visited, maze):
                return True

    return False


def can_exit(maze):
    exit_pos = (len(maze) - 1, len(maze[0]) - 1)
    return find_exit((0, 0), exit_pos, [], maze)


def test_can_exit():

    assert (
        can_exit(
            [
                [0, 1, 1, 1, 1, 1, 1],
                [0, 0, 1, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 1, 1],
                [1, 1, 1, 1, 0, 0, 1],
                [1, 1, 1, 1, 1, 0, 0],
            ]
        )
        == True
    )
    assert (
        can_exit(
            [
                [0, 1, 1, 1, 1, 1, 1],
                [0, 0, 1, 0, 0, 1, 1],
                [1, 0, 0, 0, 0, 1, 1],
                [1, 1, 0, 1, 0, 0, 1],
                [1, 1, 0, 0, 1, 1, 1],
            ]
        )
        == False
    )
    assert (
        can_exit(
            [
                [0, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1],
            ]
        )
        == False
    )
    assert (
        can_exit(
            [
                [0, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 0],
            ]
        )
        == True
    )
    assert (
        can_exit(
            [
                [0, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1, 1],
                [1, 1, 1, 1, 0, 0, 0],
            ]
        )
        == True
    )
    assert (
        can_exit(
            [
                [0, 1, 1, 1, 1, 0, 1],
                [0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1, 1],
                [1, 1, 1, 1, 0, 1, 1],
            ]
        )
        == False
    )
    assert (
        can_exit(
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1, 0],
                [1, 1, 1, 1, 0, 1, 0],
            ]
        )
        == True
    )
    assert (
        can_exit(
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 1],
            ]
        )
        == False
    )
    assert (
        can_exit(
            [
                [0, 0, 1, 1, 1, 1, 1],
                [1, 0, 0, 1, 1, 1, 1],
                [1, 1, 0, 0, 1, 1, 1],
                [1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 0],
            ]
        )
        == True
    )
    ## More False Tests
    assert (
        can_exit(
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 1, 0],
            ]
        )
        == False
    )
    assert (
        can_exit(
            [
                [0, 1, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 1, 0],
            ]
        )
        == False
    )
    ## More Tests
    assert (
        can_exit(
            [
                [0, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 1, 0, 1, 0],
                [1, 0, 0, 0, 0, 1, 0],
                [1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 0],
            ]
        )
        == True
    )
    assert (
        can_exit(
            [
                [0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 1, 0],
                [0, 1, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 1, 1, 0],
            ]
        )
        == True
    )
