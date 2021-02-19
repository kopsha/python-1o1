# Functions exercises 1 and 3


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
        f"Ran {total_count} tests out of with {passed_count} were successful"
        f" and {fail_count} did failed."
    )


def main():
    """all executable code in this module lives here"""

    # self checking part
    test_factorial()

    # print(factorial(5))
    # print(fibonacci(54))


main()
