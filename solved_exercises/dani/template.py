""".... Exercises"""

from datetime import datetime
import timeit
from math import sqrt


def function_name(number):
    """This function ..."""
    pass


def test_function_name():
    """we'll test the correctnes of function_name function"""

    print("Testing function_name() function...")

    test_data = [
        # (value, expected)
        ("", ""),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = function_name(value)
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
    test_function_name()


duration = timeit.timeit(main, number=1)
now = datetime.now().strftime("%H:%M:%S")
print(f"[{now}] Finished in {duration:.2f} seconds.")
