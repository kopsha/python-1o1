# Calculate the factorial of a number (positive integer).
def factorial(n):
    if n > 0:
        result = n * factorial(n - 1)
    else:
        result = 1
    return result
value = int(input("Please enter a numeric value:\n"))
print('Factorial of', value, 'is', factorial(value))

# Write a function that flattens a list.
def flatten(raw_list):
    flat_list = []
    for element in raw_list:
        if type(element) == list:
            flat_list.extend(flatten(element))
        else:
            flat_list.append(element)
    return flat_list

given_list = ['a', 13, [16], [56.5], [147], [18.2], [18.0,[14,15]]]
print ('Flattened list', flatten(given_list))

# Generate a list with Fibonacci sequence up to a number.
from math import sqrt
def fibonacci(n):
    result = [1]
    for i in range(1, n + 1):
        if is_fibonaci(i):
            result.append(i)
    return result

def is_fibonaci(n):
    formula1 = 5 * n**2 + 4
    formula2 = 5 * n**2 - 4
    return is_perfect_square(formula1) or is_perfect_square(formula2)

def is_perfect_square(n): 
    if(n >= 0):
        sr = sqrt(n)
        return (int(sr + 0.5) ** 2 == n)
    return False

print('v1 Fibonacci list up to', value, 'is', fibonacci(value))

def fibonacci2(n):
	lista = [1, 1]
	for i in range(2, value):
		suma = lista[-1] + lista[-2]
		if suma <= value:
		    lista.append(suma)
	return lista

print('v2 Fibbonaci list up to', value, 'is', fibonacci2(value))

# Generate a list with all prime numbers less than a number.
def primes(num):
    if num < 2:
        return []
    primes_list = [2]
    for i in range(2, num):
        if is_prime(i):
            primes_list.append(i)
    return primes_list

def is_prime(i):
    for j in range(2, i):
        if (i % j == 0):
            return False
        else:
            return True

print("Primes list up to", value, "is", primes(value))
