"""Exercise 1 - Calculate the factorial of a number (positive integer)."""

import math

def calc_factorial(n):
    """calculates factorial of a positive integer number - to be refactored"""
    if n <= 0:
        return "Invalid input. Please provide positive integer"
    if type(n) != int:
        return "Provided input number must be an integer."
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


#print(calc_factorial(7))

"""Generate a list with Fibonacci sequence up to a number."""


def fibonacci(n):
    """function generates Fibonacci list until a given input - to be refactored"""
    if n < 2:
        return "Invalid number; input number must be at least equal to 2"
    a, b = 0, 1
    fib_list = [a, b]
    while b < n - a:
        a, b = b, a + b
        fib_list.append(b)
    return fib_list

"""to discuss"""
flat = lambda given_list: [elem for item in given_list for elem in flat(item)] if isinstance(given_list, list) else [
    given_list]
#print(flat([[1, 2, 3], [3, 6, 7], [7, 5, 4], 7]))


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        raise ValueError("Expected input is an integer greater than 1")
    if not isinstance(n,int):
        raise TypeError("Expected input is an integer greater than 1")
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    """Return a list with all prime numbers until given n number"""
    if n < 2:
        raise ValueError("Expected input is an integer greater or equal to 2")
    if not isinstance(n, int):
        raise TypeError("Expected input is an integer greater than 1")
    list_primes = []
    for i in range(2, n):
        if is_prime(i):
            list_primes.append(i)
    return list_primes

def test_get_primes():
    """test the correctness of get_primes function"""

    print("Testing get_primes() function...")

    test_data = [
        # (value, expected)
        (5, [2,3]),
        (2, []),
        (15, [2,3,5,7,11,13]),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = get_primes(value)
        result = "passed" if actual == expected else "failed"

        if result == "failed":
            print(f"\t -> Actual {actual} is different from {expected}.")
            fail_count += 1

    total_count = len(test_data)
    passed_count = total_count - fail_count
    print(
        f"Ran {total_count} tests out of with {passed_count} were successful"
        f" and {fail_count} did failed."
    )

def main():
    test_get_primes()


main()