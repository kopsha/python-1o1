"""
Given a set of 3 jugs of water that have capacities of a, b, and c liters, find
the minimum number of operations performed before each jug has x, y, and z
liters. Only jug C will start completely filled.

An operation is any of the following:
A jug is emptied, a jug is filled,
or water is poured from one jug to another until one of the jugs is either empty
or full.

For example, jugs "A", "B", and "C" with capacities of 3, 5, and 8,
where jugs "A" and "B" start empty and "C" has the full 8, require 2 operations
to reach the state of 0, 3, and 5 liters in the jugs.

Create a function that, given an array of jug capacities [A, B, C] and an goal
state array [x, y, z], returns the minimum number of operations needed to reach
the goal state. If the inputs are invalid or there is no solution,
return "No solution."

Examples
waterjug([3, 5, 8], [0, 3, 5]) ➞ 2

waterjug([1, 3, 4],  [0, 2, 2]) ➞ 3

waterjug([8, 17, 20], [0, 10, 10]) ➞ 9

waterjug([4, 17, 22], [2, 5, 15]) ➞ "No solution."

waterjug([3, 5, 8], [0, 0, 9]) ➞ "No solution."
Notes
The amount of water in a jug can never exceed the capacity of that jug.
The total liters in the goal state must be equal to the capacity of jug "C".
"""


def waterjug(jugs, goal):
    pass


def test_waterjug():
    assert waterjug([3, 5, 8], [0, 3, 5]) == 2
    assert waterjug([1, 3, 4], [0, 2, 2]) == 3
    assert waterjug([8, 17, 20], [0, 10, 10]) == 9
    assert waterjug([4, 17, 22], [2, 5, 15]) == "No solution."
    assert waterjug([3, 5, 8], [0, 5, 3]) == 1
    assert waterjug([3, 5, 8], [0, 6, 2]) == "No solution."
    assert waterjug([6, 7, 10], [0, 0, 10]) == 0
    assert waterjug([3, 5, 8], [4, 0, 4]) == "No solution."
    assert waterjug([3, 5, 8], [2, 1, 4]) == "No solution."
    assert waterjug([3, 5, 8], [0, 2, 6]) == 3
    assert waterjug([6, 7, 10], [5, 5, 0]) == "No solution."
    assert waterjug([30, 45, 50], [25, 25, 0]) == "No solution."
    assert waterjug([3, 5, 8], [0, 4, 4]) == 7
    assert waterjug([4, 7, 10], [0, 5, 5]) == 8
