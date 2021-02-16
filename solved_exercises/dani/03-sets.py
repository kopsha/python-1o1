print("exercise 1")
given = {"Yellow", "Orange", "Black"}
some_items = ["Blue", "Green", "Red"]
expected = {"Green", "Yellow", "Black", "Orange", "Red", "Blue"}

union_set = given.union(some_items)
print("output set is: ",union_set)

print("exercise 2")
given_a = {10, 20, 30, 40, 50}
given_b = {30, 40, 50, 60, 70}
expected = {70, 40, 10, 50, 20, 60, 30}

union_set = given_a.union(given_b)
print("output set is: ",union_set)

print("exercise 3")
given_a = {10, 20, 30, 40, 50}
expected = {40, 50}

intersection_set = given_a.intersection([40,50])
print("output set is: ",intersection_set)

print("exercise 3")

given = "Understanding sets is easy."
vowels = ['a','e','i','o','u']
all_vowels = [letter for letter in given.lower() if letter in vowels]
vowels_counter = len(all_vowels)
print("The given string has ", vowels_counter, " vowels")