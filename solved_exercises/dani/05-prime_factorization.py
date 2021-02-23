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


def prime_factorization(number):
    """This function calculates the primes factors for
    a positive integer number and return a list of tuples as:
    [(prime_1,prime_pow_1), prime_2,prime_pow_2), ... prime_n,prime_pow_n)]
    """
    factors = []
    primes_list = primes(number)
    for element in primes_list:
        prime_pow = 0
        while number % element == 0:
            number /= element
            prime_pow += 1
        if prime_pow > 0:
            factors.append((element, prime_pow))
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
        (4, [(2, 2)]),
        # (
        #    1111,
        #    [(3, 1), (7, 1), (11, 1), (37, 1)],
        # ),
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
    test_prime_factorization()


main()
