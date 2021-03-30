# Functions exercises 1, 2, 3 and 4

import math

def factorial(x):
    """ Calculates the factorial of a number (positive integer) """
    if not isinstance(x, int):
        raise TypeError("Expected a positive integer.")

    if x < 0:
        raise ValueError("Factorial function expected a positive integer.")

    factorial = 1
    if x > 0:
        for i in range(1, x + 1):
            factorial *= i

    return factorial


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


def is_prime(nr):
    """Determines if a number is prime"""
    for i in range(2, int(math.sqrt(nr) + 1)):
        if nr % i == 0:
            return False
    return True


def generate_primes(nr):
    """Generates a list with all prime numbers less than a number"""
    # TODO: try to reuse the list of primes already calculated
    if not isinstance(nr, int):
        raise TypeError("Expected a positive integer.")
    if nr < 2:
        raise ValueError("Primes function expected a positive integer greater or equal to 2")
    primes = []
    for i in range(2, nr):
        if is_prime(i):
            primes.append(i)
    return primes


def flatten(given_list):
    """This function flattens a given list"""
    new_list = []
    for elem in given_list:
        if isinstance(elem, list):
            temp_list = flatten(elem)
            new_list.extend(temp_list)
        else:
            new_list.append(elem)
    return new_list


def gibberish(given_string):
    """ Adds after each vowel in a string the letter 'p' followed by that vowel """
    vowels = "aeiouAEIOU"
    new_string = ""
    extra_letter = "p"
    for letter in given_string:
        if letter in vowels:
            new_string += letter + extra_letter + letter.lower()
        else:
            new_string += letter
    return new_string


def test_factorial():
    """we'll test the correctness of factorial function"""

    print("Testing factorial() function...")

    test_data = [
        # (value, expected)
        (0, 1),
        (1, 1),
        (2, 2),
        (9, 362880),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = factorial(value)
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

def test_fibonacci():
    """we'll test the correctness of fibonacci function"""

    print("Testing fibonacci() function...")

    test_data = [
        # (value, expected)
        (54, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
        (55, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
        (120, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = fibonacci(value)
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


def test_generate_primes():
    """we'll test the correctness of generate_primes function"""

    print("Testing generate_primes() function...")

    test_data = [
        # (value, expected)
        (2, []),
        (3, [2]),
        (43, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]),
        (8, [2, 3, 5, 7])
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = generate_primes(value)
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

def test_flatten():
    """we'll test the correctness of list_flatten function"""

    print("Testing list_flatten() function...")

    test_data = [
        # (value, expected)
        ([1, 6, [6, 32, "a", 17], 19, 17, 25, [20, 19]], [1, 6, 6, 32, "a", 17, 19, 17, 25, 20, 19]),
        ([[0, 3], [0, 3], [19, 17, 25, [20, 19]]], [0, 3, 0, 3, 19, 17, 25, 20, 19]),
        ([1, 5, 7], [1, 5, 7]),
        ([], []),
        ([[[1, 2, 3]]], [1, 2, 3]),
        ([1, 2, 3, []], [1, 2, 3]),

    ]

    fail_count = 0
    for value, expected in test_data:
        actual = flatten(value)
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

def test_gibberish():
    """we'll test the correctness of list_flatten function"""

    print("Testing gibberish() function...")

    test_data = [
        # (value, expected)
        ("", ""),
        ("e!", "epe!"),
        ("ctrl", "ctrl"),
        ("Pe mine ma cheama Ion", "Pepe mipinepe mapa chepeapamapa Ipiopon"),
        ("Pe mine ma cheama Don", "Pepe mipinepe mapa chepeapamapa Dopon"),
        ("Azi ai treaba?", "Apazipi apaipi trepeapabapa?"),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = gibberish(value)
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
    """all executable code in this module lives here"""

    # self checking part
    test_factorial()
    test_fibonacci()
    test_generate_primes()
    test_gibberish()
    test_flatten()


main()
