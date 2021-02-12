"""Exercise 2 Marius - sets"""

"""Add a list of elements to a given set.

given = {"Yellow", "Orange", "Black"}
some_items = ["Blue", "Green", "Red"]
expected = {"Green", "Yellow", "Black", "Orange", "Red", "Blue"}
"""

given = {"Yellow", "Orange", "Black"}
some_items = ["Blue", "Green", "Red"]
my_set = set(some_items).union(given)
print(my_set)

"""Create a new set with all items from both sets by removing duplicates

given_a = {10, 20, 30, 40, 50}
given_b = {30, 40, 50, 60, 70}
expected = {70, 40, 10, 50, 20, 60, 30}
"""
given_a = {10, 20, 30, 40, 50}
given_b = {30, 40, 50, 60, 70}
expected = given_b.union(given_a)
print(expected)

"""Remove 10, 20, 30 elements from the following set
given_a = {10, 20, 30, 40, 50}
expected = {40, 50}
"""
given_a = {10, 20, 30, 40, 50}
given_a.discard(10)
given_a.discard(20)
given_a.discard(30)
print(given_a)

"""Determine whether or not the following two sets have any elements in common
given_a = {10, 20, 30, 40, 50}
given_b = {60, 70, 80, 90, 10}
# Expected output:
The two sets have items in common.
{10}
"""
given_a = {10, 20, 30, 40, 50}
given_b = {60, 70, 80, 90, 10}
print(given_a.intersection(given_b))

"""Count the number of vowels in a given string
given = "Understanding sets is easy."
# Expected output
The given string has 7 vowels.
"""
given = "Understanding sets is easy."
vowels = {"a", "e", "i", "o", "u"}
cnt = 0
for i in given:
	if i in vowels:
		cnt += 1
print(cnt)