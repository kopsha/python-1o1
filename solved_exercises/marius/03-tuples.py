"""Exercise 3 Marius - tuples"""

"""Check whether an element exists within a tuple.
"""

given = ("Yellow", "Orange", "Black")
elem = "Orange"
if elem in given:
	print("Element is in tuple")
else:
	print("Element is not in tuple")

"""Sum up all the number elements within a tuple
"""
given_a = (10, 20, 30, 40, 50)
sum = 0
for i in given_a:
	sum += i
print(sum)

"""Find the repeated items of a tuple.
"""
given_a = (10, 20, 30, 40, 10, 50, 20)
elements = set()
for i in given_a:
	if given_a.count(i) > 1:
		elements.add(i)
print(elements)

"""Print out all pair combinations of two tuples.
"""
given_a = (10, 20, 30)
given_b = (50, 60, 70)
for i in given_a:
	for j in given_b:
		print(i, j)
