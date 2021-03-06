"""The fastest prime factorization I could come up with"""

from datetime import datetime
import timeit
from math import sqrt


def prime_factorization(number):
    """This function calculates the primes factors for
    a positive integer number and return a list of tuples as:
    [(prime_1,prime_pow_1), prime_2,prime_pow_2), ... prime_n,prime_pow_n)]
    """
    factors = []
    dividend = number
    divisor_limit = dividend
    exponent = 0
    is_prime = True
    gap = 1
    divisor = 2
    while divisor <= number:
        divisor_limit = int(sqrt(dividend))
        if divisor == 3:
            gap = 2
        if (dividend % divisor) == 0:
            dividend //= divisor
            exponent += 1
            continue  # we want to attempt this divisor again
        if exponent > 0:
            factors.append((divisor, exponent))

            exponent = 0
            is_prime = False
            if divisor > dividend or divisor > divisor_limit:
                break  # there is no need to explore furthers
        if divisor > divisor_limit:
            factors.append((dividend, 1))
            break  # there is no need to explore further
        divisor += gap

    return factors


def test_prime_factorization():
    """we'll test the correctnes of test_prime_factorization function"""

    print("Testing test_prime_factorization() function...")

    test_data = [
        # (value, expected)
        # (140, [(2, 2), (5, 1), (7, 1)]),
        # (420, [(2, 2), (3, 1), (5, 1), (7, 1)]),
        # (2, [(2, 1)]),
        # (11, [(11, 1)]),
        # (12, [(2, 2), (3, 1)]),
        # (4, [(2, 2)]),
        # (7, [(7, 1)]),
        # (15, [(3, 1), (5, 1)]),
        # (10_999, [(17, 1), (647, 1)]),
        # (109_999, [(317, 1), (347, 1)]),
        # (10_099_999, [(7, 1), (13, 1), (110989, 1)]),
        # (8547, [(3, 1), (7, 1), (11, 1), (37, 1)]),
        # (1_000_000_000_000, [(2, 12), (5, 12)]),
        # (
        #    999_999_999_999,
        #    [(3, 3), (7, 1), (11, 1), (13, 1), (37, 1), (101, 1), (9901, 1)],
        # ),
        # (100_999_999_999_999, [(31, 2), (607, 1), (173144737, 1)]),  # ~21s
        # (
        #    10_099_999_999_999_999_999,
        #    [(7, 1), (13, 1), (317, 1), (1051, 1), (33409, 1), (9971363, 1)],
        # ),  # ~1.3s
        (
            100_099_999_999_999_999_999,
            [(31, 1), (2029, 1), (1591440245472901, 1)],
        ),  # before sqrt(n) not ending, after ~13s
        # (9_971_363, [(9971363, 1)]),  # before sqrt(n) ~1.2s, after 0
        # (17_051_887, [(17051887, 1)]),  # before sqrt(n) ~2.2s after 0
        # (122_164_969, [(122164969, 1)]),  # before sqrt(n) ~15s after 0
        # (191_913_031, [(191913031, 1)]),  # before sqrt(n) ~24s after 0
        # (1_294_268_779, [(1294268779, 1)]),  # before sqrt(n) ~240s after 0
        # (1_346_294_311_331, [(1346294311331, 1)]), # after sqrt(n) 0.41s
        # (7_177_162_612_387, [(7177162612387, 1)]),  # 13 digits after sqrt(n) 1.07s
        # (999_998_727_899_999, [(999998727899999, 1)]), # 15 digits prime ~10s
        (9_957_969_395_462_467, [(9957969395462467, 1)]),  # oesis 4162 16 digits ~40s
        # (99_957_969_395_462_467, [(99957969395462467, 1)]), # oesis 4204 17 digits ~100s
        # (992_429_121_339_693_967, [(992429121339693967, 1)]), # oesis 4228 18 digits prime ~333s
        # (8_963_315_421_273_233_617, [(8963315421273233617, 1)]), # oesis 4241 19 digits prime ~1184s
        # (86_312_646_216_567_629_137, [(86312646216567629137, 1)]), #oesis 4247 20 digits prime estimated~3650s
        # (99_999_999_999_999_999_999_977, []), #23digits actual speed ~
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
