# Functions exercises 1 and 3

def calculate_factorial(x):
    ''' Calculates the factorial of a number (positive integer) '''
    factorial = 1
    if (x < 0):
        return "Factorial can't be calculated for negative numbers "
    elif(x == 0):
        return 1
    else:
        for i in range(1, x+1):
            factorial = factorial *i
        return factorial
print(calculate_factorial(5))

def Fibonacci(n):
    ''' Generates a list with Fibonacci sequence up to a given n number. '''
    a = 0
    b = 1
    list = [a, b]
    if (n < 0):
        return "Please insert a positive integer "
    elif(n == 0):
        return a
    else:
        while a + b < n:
            a, b = b, a+b
            list.append(b)
        return list
print(Fibonacci(63))





