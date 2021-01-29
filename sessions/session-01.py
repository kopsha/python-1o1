"""We will attempt the first session skipping entry level, main topic lists"""
print("hello world.")

# int, float, string
# if

temperatura = None

if temperatura is None:
	print("please start the sensor.")

# creating a list is as easy as:
ingredients = []
print(ingredients)

ingredients.append("eggs")
ingredients.append("cheese")
ingredients.append("oil")
ingredients.append("pepper")
ingredients.append("onion")
print("full list", ingredients)


# alternative to removing items from a list is to create a new list
print("partial list", ingredients[2:])  # list slicing


# remove last item
ingredients.pop()
print(ingredients)

print("last list item (-1):", ingredients[-1])
print("list item (-2):", ingredients[-2])
print("list item (-3):", ingredients[-3])

print("the python way")
for ingredient in reversed(ingredients):
	print(ingredient)

#print(sorted(ingredients))
#print(sorted(ingredients, reverse=True))
#print(list(reversed(ingredients)))

# list comprehension
ingredients.append(None)
print(ingredients)
short_ingredients = [elem.title() if elem else "N/A" for elem in ingredients]
print(short_ingredients)

