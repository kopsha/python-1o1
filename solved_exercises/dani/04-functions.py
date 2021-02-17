print("Calculate the factorial of a number (positive integer).")
def factorial (n):
    if n > 0:
        result = n * factorial(n-1)
    else:
        result = 1
    return result
value = int(input("Please enter a numeric value:\n"))
print("Factorial of",value,"is",factorial(value))

print("Write a function that flattens a list.")
def flat (lista):
	return [val for sublist in lista for val in sublist]
given_list = [[18.0], [13.8], [16.2], [56.5], [147], [18.2]]
print (flat(given_list))

print("Generate a list with Fibonacci sequence up to a number.")
from math import sqrt
def fibonacci (n):
    result = []
    for i in range(n):
        if is_fibonaci(i) != None:
            result.append(i)
            if i == 1:
                result.append(i)
    return result

def is_fibonaci (n):
    formula1=5 * n**2 + 4
    formula2=5 * n**2 - 4
    if isPerfectSquare(formula1) or isPerfectSquare(formula2):
        return n
    else:
        return None

def isPerfectSquare(n): 
    if(n >= 0):
        sr = sqrt(n)
        return (int(sr + 0.5) ** 2 == n)
    return False
print("Fibonacci list up to",value,"is",fibonacci(value))

def fib2(n):
	lista = [0,1]
	for i in range(2,value):
		suma = lista[-1]+lista[-2]
		if suma <= value:
		    lista.append(suma)
	return lista
print("fibbonaci ver2",fib2(value))

print("Generate a list with all prime numbers less than a number.")
def primes(num):
    primes_list = []
    for num in range(2,num):
        prime = True
        for i in range(2,num):
            if (num%i==0) and (i<num):
                prime = False
        if prime:
            primes_list.append(num)
    return primes_list
print("Primes list up to",value,"is",primes(value))