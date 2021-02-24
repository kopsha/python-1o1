from math import sqrt

from datetime import datetime
import timeit


def primes_fast(number):
    dropped = set()
    kept = set()
    i = 2
    while i <= number:
        if i not in dropped:
            kept.add(i)
        dropped.update(set(range(i + i, number + 1, i)))
        # print(i, "dropped ",dropped)
        # print(i + i, limit, i)
        i += 1
    return kept


def prime_factorization(number):
    """This function calculates the primes factors for
    a positive integer number and return a list of tuples as:
    [(prime_1,prime_pow_1), prime_2,prime_pow_2), ... prime_n,prime_pow_n)]
    """
    factors = []
    primes = primes_fast(number)
    # print("DEBUG",primes)
    for prime in primes:
        exponent = 0
        # print(number % prime == 0, number, prime)
        while number % prime == 0:
            number //= prime
            exponent += 1
        if exponent > 0:
            factors.append((prime, exponent))
    return factors


def test_prime_factorization():
    """we'll test the correctnes of test_prime_factorization function"""

    print("Testing test_prime_factorization() function...")

    test_data = [
        # (value, expected)
        (140, [(2, 2), (5, 1), (7, 1)]),
        (420, [(2, 2), (3, 1), (5, 1), (7, 1)]),
        (1, []),
        (2, [(2, 1)]),
        (11, [(11, 1)]),
        (4, [(2, 2)]),
        (7, [(7, 1)]),
        (15, [(3, 1), (5, 1)]),
        (10_999, [(17, 1), (647, 1)]),
        (109_999, [(317, 1), (347, 1)]),
        (10_099_999, [(29, 1), (83, 1), (457, 1)]),
        (
            8547,
            [(3, 1), (7, 1), (11, 1), (37, 1)],
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
    # self checking part
    # primes_fast(7)
    test_prime_factorization()


duration = timeit.timeit(main, number=1)
now = datetime.now().strftime('%H:%M:%S')
print(f'[{now}] Finished in {duration:.2f} seconds.')
