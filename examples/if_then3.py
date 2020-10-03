# scalene triangle: all three sides are different
# isosceles triangle: two sides of the same length
# equilateral triangle: all the sides are equal

a = int(input("The length of side a: "))
b = int(input("The length of side b: "))
c = int(input("The length of side c: "))

if a == b and b == c:
	print("This is an equilateral triangle.")
elif a != b and b != c and a != c:
	print("This is a scalene triangle.")
else:
	print("This is an isosceles triangle.")

