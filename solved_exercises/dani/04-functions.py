#Calculate the factorial of a number (positive integer).
def factorial (n):
    if n > 0:
        result = n * factorial(n-1)
    else:
        result = 1
    return result
value = int(input("Please enter a numeric value:\n"))
print('Factorial of',value,'is',factorial(value))

#Write a function that flattens a list.
def flat (raw_list, flat_list=[]):
    for elm in raw_list:
        if type(elm) == list:
            flat(elm)
        else:
            flat_list.append(elm)
    return flat_list

given_list = ['a', 13, [16], [56.5], [147], [18.2], [18.0,[14,15]]]
print ('Flatten list',flat(given_list))

#Generate a list with Fibonacci sequence up to a number.
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
    if is_Perfect_Square(formula1) or is_Perfect_Square(formula2):
        return n
    else:
        return None

def is_Perfect_Square(n): 
    if(n >= 0):
        sr = sqrt(n)
        return (int(sr + 0.5) ** 2 == n)
    return False
print('v1 Fibonacci list up to',value,'is',fibonacci(value))

def fibonacci2(n):
	lista = [0,1]
	for i in range(2,value):
		suma = lista[-1]+lista[-2]
		if suma <= value:
		    lista.append(suma)
	return lista
print('v2 Fibbonaci list up to', value,'is',fibonacci2(value))

#Generate a list with all prime numbers less than a number.
def primes(num):
    primes_list = [2]
    for i in range(2,num):
        if is_prime(i):
            primes_list.append(i)
    return primes_list

def is_prime(i):
    for j in range(2,i):
        if (i%j==0):
            return False
        else:
            return True

print("Primes list up to",value,"is",primes(value))