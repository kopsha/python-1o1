"""Exercise 1 - Calculate the factorial of a number (positive integer)."""


def calc_factorial(n):
	"""calculates factorial of a positive integer number"""
	if n <= 0:
		return "Invalid input. Please provide positive integer"
	if type(n) != int:
		return "Provided input number must be an integer."
	fact = 1
	for i in range(1,n+1):
		fact *= i
	return fact

print(calc_factorial(7))

"""Generate a list with Fibonacci sequence up to a number."""
def fibonacci(n):
	"""function generates Fibonacci list until a given input"""
	if n < 2:
		return "Invalid number; input number must be at least equal to 2"
	a,b = 0,1
	fib_list = [a]
	while b < n-a:
		a,b = b, a + b
		fib_list.append(b)
	return fib_list
print(fibonacci(50))


