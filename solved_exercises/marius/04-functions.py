"""Exercise 1 - Calculate the factorial of a number (positive integer)."""

import math

def calc_factorial(n):
    """calculates factorial of a positive integer number - to be refactored"""
    if not isinstance(n, int):
        raise TypeError("Provided input number must be an integer.")
    if n <= 0:
        raise ValueError("Invalid input. Please provide positive integer")
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    # values for test: 1,5,1000
    return fact



"""Generate a list with Fibonacci sequence up to a number."""


def fibonacci(n):
    """function generates Fibonacci list until a given input - to be refactored"""
    if n < 0:
        raise ValueError("Invalid number; input number must be at least equal to 1")
    a, b = 0, 1
    fib_list = [a]

    if n > 0:
        while b <= n:
            a, b = b, a + b
            fib_list.append(a)

    return fib_list


# TODO refactor and use classical recursive function
#flat = lambda given_list: [elem for item in given_list for elem in flat(item)] if isinstance(given_list, list) else [
#    given_list]



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

def gibberish_translate(text):
    translated_text = ""
    extra_char = "p"
    vowels = ["a", "e", "i", "o", "u"]
    for letter in text:
        translated_text += letter
        if letter.lower() in vowels:
            translated_text += extra_char + letter.lower()
    return translated_text

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

#test functions

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

def test_calc_factorial():
    """we'll test the correctness of list_flatten function"""

    print("Testing list_flatten() function...")

    test_data = [
        # (value, expected)
        (1, 1),
        (2, 2),
        (9, 362880),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = calc_factorial(value)
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


def test_gibberish_translate():
    """we'll test the correctness of list_flatten function"""

    print("Testing gibberish_translate() function...")

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
        actual = gibberish_translate(value)
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

def main():
    #test_get_primes()
    test_gibberish_translate()
    #test_calc_factorial()
    #test_flatten()
    #test_fibonacci()

main()