"""Exercise 1 Marius - playing with lists"""

"""Ex 1 - Given a Python list you should be able to display Python list in the reversed order
given = [100, 200, 300, 400, 500]
expected = [500, 400, 300, 200, 100]
"""

given1 = [100, 200, 300, 400, 500]
print(list(reversed(given1)))

"""Ex 2 Remove empty strings from the list of strings
given = ["Mike", "", "Emma", "Kelly", "", "Brad"]
expected = ["Mike", "Emma", "Kelly", "Brad"]
"""
given2 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
lstNoEmptyStr = [elem for elem in given2 if elem != ""]
print(lstNoEmptyStr)

"""Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of the value.
given = [5, 10, 15, 20, 25, 50, 20]
expected = [5, 10, 15, 200, 25, 50, 20]
"""
given3 = [5, 10, 15, 20, 25, 50, 20]
lstReplaceValue = []
count = 0
for value in given3:
	if value == 20 and count == 0:
		lstReplaceValue.append(200)
		count += 1
	else:
		lstReplaceValue.append(value)

print(lstReplaceValue)

#alterntaive
indFound = None
for index, value in enumerate(given3):
	if value == 20:
		indFound = index
		break
if indFound:
	given3[indFound] = 200
print(given3)

"""Ex 4 - Given a Python list, remove all occurrence of 20 from the list.
given = [5, 20, 15, 20, 25, 50, 20]
expected = [5, 15, 25, 50]
"""
given4 = [5, 20, 15, 20, 25, 50, 20]
valToRemove = 20
lstRemVal = [elem for elem in given4 if elem != valToRemove]
print(lstRemVal)

"""Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ri"]
list2 = ["y", "me", "s", "ck"]
expected = ["My", "name", "is", "Rick"]
"""
list1 = ["M", "na", "i", "Ri"]
list2 = ["y", "me", "s", "ck"]
expected = []
zipped = list(zip(list1, list2))
print(zipped)
expected =	map(, zipped)
print(list(expected))