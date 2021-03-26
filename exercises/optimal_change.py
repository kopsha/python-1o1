"""
Correctly determine the fewest number of coins to be given to a customer such
that the sum of the coins' value would equal the correct amount of change.

For example
An input of 15 with [1, 5, 10, 25, 100] should return one nickel (5) and one
dime (10) or [5, 10]
An input of 40 with [1, 5, 10, 25, 100] should return one nickel (5) and one
dime (10) and one quarter (25) or [5, 10, 25]

Edge cases
^^^^^^^^^^
Does your algorithm work for any given set of coins?
* when it is not possible function should return an empty list
Can you ask for negative change?
* not applicable, raise ValueError
Can you ask for a change value smaller than the smallest coin value?
* not possible, we'll return an empty list
"""


def optimize_change(available_coins, amount):
    """Breaks down the amount into the given available coins"""

    if not isinstance(amount, int):
        raise TypeError("Amount must be a positive integer.")

    if amount <= 0:
        raise ValueError("Amount must be a positive integer.")

    all_coins = sorted(available_coins, reverse=True)
    result = []

    for coin in all_coins:
        divisor = amount // coin
        if divisor > 0:
            result.append((divisor, coin))
        amount -= coin * divisor

    if amount > 0:
        result = []

    return result


def main():
    """local testing of optimal changes"""

    print("-"*25)
    print("runda noua")

    available_coins = [5, 10, 25, 100]
    print(" >> having these coins", available_coins)

    amount = 15
    result = optimize_change(available_coins, amount)
    print(" >> the amount", amount, "breaks down to", result)

    amount = 40
    result = optimize_change(available_coins, amount)
    print(" >> the amount", amount, "breaks down to", result)

    amount = 100
    result = optimize_change(available_coins, amount)
    print(" >> the amount", amount, "breaks down to", result)

    amount = 3
    result = optimize_change(available_coins, amount)
    print(" >> the amount", amount, "breaks down to", result)

    amount = 401
    result = optimize_change(available_coins, amount)
    print(" >> the amount", amount, "breaks down to", result)

    amount = 99
    result = optimize_change(available_coins, amount)
    print(" >> the amount", amount, "breaks down to", result)


if __name__ == '__main__':
    main()
