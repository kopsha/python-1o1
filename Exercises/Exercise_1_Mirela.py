"""Exercise 1 Marius - playing with lists"""

"""Ex 1 - Given a Python list you should be able to display Python list in the reversed order
given = [100, 200, 300, 400, 500]
expected = [500, 400, 300, 200, 100]
"""

given = [100, 200, 300, 400, 500]
given.reverse()
print(given)

"""Ex 2 Remove empty strings from the list of strings
given = ["Mike", "", "Emma", "Kelly", "", "Brad"]
expected = ["Mike", "Emma", "Kelly", "Brad"]
"""
given2 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
expected2 =[name for name in given2 if len(name) != 0]
print(expected2)

"""Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of the value.
given = [5, 10, 15, 20, 25, 50, 20]
expected = [5, 10, 15, 200, 25, 50, 20]
"""
given3 = [5, 10, 15, 20, 25, 50, 20]
index = given3.index(20)
given3[index]= 200
print(given3)

"""Ex 4 - Given a Python list, remove all occurrence of 20 from the list.
given = [5, 20, 15, 20, 25, 50, 20]
expected = [5, 15, 25, 50]
"""
given4 = [5, 20, 15, 20, 25, 50, 20]

expected = [i for i in given4 if i != 20]
print(expected)

"""Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ri"]
list2 = ["y", "me", "s", "ck"]
expected = ["My", "name", "is", "Rick"]
"""
list1 = ["M", "na", "i", "Ri"]
list2 = ["y", "me", "s", "ck"]
expected = []
for i in range(len(list1)):
	expected.append(list1[i] + list2[i])
print(expected)
