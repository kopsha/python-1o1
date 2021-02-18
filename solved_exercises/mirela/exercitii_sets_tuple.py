# exercise1_sets
# Add a list of elements to a given set.

given = {"Yellow", "Orange", "Black"}
some_items = ["Blue", "Green", "Red"]
given.update(some_items)
print(given)

# exercise2_sets
# Create a new set with all items from both sets by removing duplicates
given_a = {10, 20, 30, 40, 50}
given_b = {30, 40, 50, 60, 70}
expected = given_a.union(given_b)
print(expected)

# exercise3_sets
# Remove 10, 20, 30 elements from the following set
given_a = {10, 20, 30, 40, 50}
delete = [10, 20, 30]
given_a.difference_update(delete)
print(given_a)

given_a = {10, 20, 30, 40, 50}
expected = {val for val in given_a if val >= 40}
print(expected)

# exercise4_sets
# Determine whether or not the following two sets have any elements in common
given_a = {10, 20, 30, 40, 50}
given_b = {60, 70, 80, 90, 10}
print(given_a.intersection(given_b))

# exercise5_sets
# Count the number of vowels in a given string
given = "Understanding sets is easy."
vowels = "aeiouAEIOU"
expected = [val for val in given if val in vowels]
print(len(expected))

# exercise1_tuple
# Check whether an element exists within a tuple
tuple = ("a", 9, False, 3.17, "Ana")
print(False in tuple)

# exercise2_tuple
# Sum up all the number elements within a tuple.
tuple2 = (2, 4, 1, 5, 20, 33)
print(sum(tuple2))

# exercise3_tuple
# Find the repeated items of a tuple.
tuple3 = (5, 7, 8, 5, 12, 6, 5, 5, 12, 8)
repeated_items = set()
repeated_items = {val for val in tuple3 if tuple3.count(val)>1}
print(repeated_items)

# exercise4_tuple
# Print out all pair combinations of two tuples
tuple4 = (3, 5, 7, 8, 9, 36, 56)
tuple5 = (49, 23, 89, "no", 9, "y", "A")
combinations = {(a, b) for a in tuple4 for b in tuple5}
print(combinations)