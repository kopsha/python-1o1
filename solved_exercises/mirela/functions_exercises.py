# Functions exercises 1 and 3


def calculate_factorial(x):
    """ Calculates the factorial of a number (positive integer) """
    if type(x) is not int:
        raise TypeError("Expected a positive integer.")

    if x < 0:
        raise ValueError("Factorial function expected a positive integer.")

    factorial = 1
    if x > 0:
        for i in range(1, x + 1):
            factorial *= i

    return factorial


print(calculate_factorial(5))


def fibonacci(n):
    """ Generates a list with Fibonacci sequence up to a given n number. """
    if n < 0:
        raise ValueError("Please insert a positive integer.")

    a, b = 0, 1
    fibo_list = [a]

    if n > 0:
        while b <= n:
            a, b = b, a + b
            fibo_list.append(a)

    return fibo_list

print(fibonacci(54))
print(fibonacci(55))
print(fibonacci(56))
