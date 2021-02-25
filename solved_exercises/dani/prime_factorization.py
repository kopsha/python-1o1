"""The fastest prime factorization I could come up with"""

from datetime import datetime
import timeit


def prime_factorization(number):
    """This function calculates the primes factors for
    a positive integer number and return a list of tuples as:
    [(prime_1,prime_pow_1), prime_2,prime_pow_2), ... prime_n,prime_pow_n)]
    """
    factors = []
    dividend = number
    exponent = 0
    is_prime = True

    divisor = 2
    while divisor <= number:
        if (dividend % divisor) == 0:
            dividend //= divisor
            exponent += 1
            continue  # we want to attempt this divisor again
        if exponent > 0:
            factors.append((divisor, exponent))
            exponent = 0
            is_prime = False
            if divisor > dividend:
                break  # there is no need to explore further
        divisor += 1

    if is_prime:
        factors.append((dividend, 1))

    return factors


def test_prime_factorization():
    """we'll test the correctnes of test_prime_factorization function"""

    print("Testing test_prime_factorization() function...")

    test_data = [
        # (value, expected)
        (140, [(2, 2), (5, 1), (7, 1)]),
        (420, [(2, 2), (3, 1), (5, 1), (7, 1)]),
        (2, [(2, 1)]),
        (11, [(11, 1)]),
        (12, [(2, 2), (3, 1)]),
        (4, [(2, 2)]),
        (7, [(7, 1)]),
        (15, [(3, 1), (5, 1)]),
        (10_999, [(17, 1), (647, 1)]),
        (109_999, [(317, 1), (347, 1)]),
        (10_099_999, [(7, 1), (13, 1), (110989, 1)]),
        (8547, [(3, 1), (7, 1), (11, 1), (37, 1)]),
        (1_000_000_000_000, [(2, 12), (5, 12)]),
        (
            999_999_999_999,
            [(3, 3), (7, 1), (11, 1), (13, 1), (37, 1), (101, 1), (9901, 1)],
        ),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = prime_factorization(value)
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
    """self checking part"""
    test_prime_factorization()


duration = timeit.timeit(main, number=1)
now = datetime.now().strftime("%H:%M:%S")
print(f"[{now}] Finished in {duration:.2f} seconds.")
