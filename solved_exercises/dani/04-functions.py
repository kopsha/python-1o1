from math import sqrt

# Calculate the factorial of a number (positive integer).
def factorial(n):
    if n > 0:
        result = n * factorial(n - 1)
    else:
        result = 1
    return result


# Write a function that flattens a list.
def flatten(raw_list):
    flat_list = []
    if not isinstance(raw_list, list):
        flat_list = []
    else:
        for element in raw_list:
            if type(element) == list:
                flat_list.extend(flatten(element))
            else:
                flat_list.append(element)
    return flat_list


# Generate a list with Fibonacci sequence up to a number.


def fibonacci(n):
    result = [1]
    if n < 1:
        result = []
    for i in range(1, n + 1):
        if is_fibonaci(i):
            result.append(i)
    return result


def is_fibonaci(n):
    formula1 = 5 * n ** 2 + 4
    formula2 = 5 * n ** 2 - 4
    return is_perfect_square(formula1) or is_perfect_square(formula2)


def is_perfect_square(n):
    if n >= 0:
        sr = sqrt(n)
        return int(sr + 0.5) ** 2 == n
    return False


def fibonacci2(value):
    lista = [1, 1]
    if value < 1:
        lista = []
    for i in range(2, value + 1):
        suma = lista[-1] + lista[-2]
        if suma <= value:
            lista.append(suma)
    return lista


# Generate a list with all prime numbers less than a number.
def primes(number):
    primes_list = []
    for i in range(2, number + 1):
        if is_prime(i):
            primes_list.append(i)
    return primes_list


def is_prime(number):
    all_mod_multiplied = 1
    for i in range(2, number):
        all_mod_multiplied *= number % i
    return all_mod_multiplied > 0


def test_factorial():
    """we'll test the correctnes of factorial function"""

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
        f"Ran {total_count} tests out of {passed_count} were successful"
        f" and {fail_count} did failed."
    )


def test_fibonnaci():
    """we'll test the correctnes of fibonacci function"""

    print("Testing fibonacci() function...")

    test_data = [
        # (value, expected)
        (-1, []),
        (0, []),
        (1, [1, 1]),
        (2, [1, 1, 2]),
        (3, [1, 1, 2, 3]),
        (15, [1, 1, 2, 3, 5, 8, 13]),
    ]

    fail_count = 0
    for value, expected in test_data:
        # actual = fibonacci2(value)
        actual = fibonacci(value)
        result = "passed" if actual == expected else "failed"

        if result == "failed":
            print(f"\t -> test {value} Actual {actual} is different from {expected}.")
            fail_count += 1

    total_count = len(test_data)
    passed_count = total_count - fail_count
    print(
        f"Ran {total_count} tests out of {passed_count} were successful"
        f" and {fail_count} did failed."
    )


def test_flatten():
    """we'll test the correctnes of flatten function"""

    print("Testing flatten() function...")

    test_data = [
        # (value, expected)
        (
            ["a", 13, [-16], [56.5], [147], [18.2], [18.0, [14, 15]]],
            ["a", 13, -16, 56.5, 147, 18.2, 18.0, 14, 15],
        ),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = flatten(value)
        result = "passed" if actual == expected else "failed"

        if result == "failed":
            print(f"\t -> test Actual {actual} is different from {expected}.")
            fail_count += 1

    total_count = len(test_data)
    passed_count = total_count - fail_count
    print(
        f"Ran {total_count} tests out of {passed_count} were successful"
        f" and {fail_count} did failed."
    )


def test_primes():
    """we'll test the correctnes of primes function"""

    print("Testing primes() function...")

    test_data = [
        # (value, expected)
        (-1, []),
        (0, []),
        (1, []),
        (2, [2]),
        (3, [2, 3]),
        (15, [2, 3, 5, 7, 11, 13]),
    ]

    fail_count = 0
    for value, expected in test_data:
        # actual = fibonacci2(value)
        actual = primes(value)
        result = "passed" if actual == expected else "failed"

        if result == "failed":
            print(f"\t -> test {value} Actual {actual} is different from {expected}.")
            fail_count += 1

    total_count = len(test_data)
    passed_count = total_count - fail_count
    print(
        f"Ran {total_count} tests out of {passed_count} were successful"
        f" and {fail_count} did failed."
    )


def main():
    # self checking part
    test_factorial()
    test_fibonnaci()
    test_flatten()
    test_primes()


main()
