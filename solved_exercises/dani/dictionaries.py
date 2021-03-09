"""Dcitionary Exercises"""

from datetime import datetime
import timeit
import string


def create_dict(my_keys, my_values):
    """This function Create a dictionary out of the key and value lists."""
    result = dict(zip(my_keys, my_values))
    return result


def create_dict2(my_keys, my_values):
    """This function Create a dictionary out of the key and value lists."""
    result = {k: v for (k, v) in zip(my_keys, my_values)}
    return result


def find_model_and_year(car):
    """This function receive a dictionary describing a car attributes,
    return the model and the year of the car or the string N/A if the value
    is not present.
    """
    model = car.get("model", "N/A")
    year = car.get("year", "N/A")
    result = (model, year)
    return result


def order_dictionary(my_dictionary):
    """This function return all the key value pairs of any dictionary
    in the same order every time (order the keys alphabetically).
    """
    result = []
    my_keys = sorted(my_dictionary.keys())
    for key in my_keys:
        result.append((key, my_dictionary.get(key)))
    return result


def count_frequency(text):
    """This function Count the frequency of all words in the given text."""
    result = {}
    words_count = 0

    text_no_punctuation = text.translate(str.maketrans("", "", string.punctuation))
    words = text_no_punctuation.lower().split()

    for word in words:
        words_count = result.get(word, 0)
        result[word] = words_count + 1

    return result


def test_create_dict():
    """we'll test the correctnes of create_dict function"""

    print("Testing create_dict() function...")

    test_data = [
        # (value, expected)
        (
            ["name", "phone", "email"],
            ["Mike", "+40791882123", "michael@yahoo.com"],
            {"name": "Mike", "phone": "+40791882123", "email": "michael@yahoo.com"},
        ),
        (
            ["name", "phone", "email", "location"],
            ["Mike", "+40791882123", "michael@yahoo.com"],
            {"name": "Mike", "phone": "+40791882123", "email": "michael@yahoo.com"},
        ),
    ]

    fail_count = 0
    for my_keys, my_values, expected in test_data:
        actual = create_dict(my_keys, my_values)
        # actual = create_dict2(my_keys, my_values)
        result = "passed" if actual == expected else "failed"

        if result == "failed":
            print(f"\t -> Actual result {actual}\n\t -> Expected is   {expected}.")
            fail_count += 1

    total_count = len(test_data)
    passed_count = total_count - fail_count
    print(
        f"Ran {total_count} tests out of {passed_count} were successful"
        f" and {fail_count} did failed."
    )


def test_find_model_and_year():
    """we'll test the correctnes of find_model_and_year function"""

    print("Testing find_model_and_year() function...")

    test_data = [
        # (value, expected)
        ({}, ("N/A", "N/A")),
        ({"brand": "Ford", "model": "Mustang", "year": 1964}, ("Mustang", 1964)),
        ({"brand": "Ford", "model": "Mustang"}, ("Mustang", "N/A")),
        ({"brand": "Ford", "year": 1964}, ("N/A", 1964)),
        ({"year": 1964, "model": "Mustang"}, ("Mustang", 1964)),
        (
            {"brand": "Ford", "model": "Mustang", "year": 1964, "Color": "Red"},
            ("Mustang", 1964),
        ),
        (
            {"name": "Mike", "phone": "+40791882123", "email": "michael@yahoo.com"},
            ("N/A", "N/A"),
        ),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = find_model_and_year(value)
        result = "passed" if actual == expected else "failed"

        if result == "failed":
            print(f"\t -> Actual result {actual}\n\t -> Expected is   {expected}.")
            fail_count += 1

    total_count = len(test_data)
    passed_count = total_count - fail_count
    print(
        f"Ran {total_count} tests out of {passed_count} were successful"
        f" and {fail_count} did failed."
    )


def test_order_dictionary():
    """we'll test the correctnes of order_dictionary function"""

    print("Testing order_dictionary() function...")

    test_data = [
        # (value, expected)
        ({}, []),
        (
            {"name": "Mike", "phone": "+40791882123", "email": "michael@yahoo.com"},
            [
                ("email", "michael@yahoo.com"),
                ("name", "Mike"),
                ("phone", "+40791882123"),
            ],
        ),
        (
            {"_name": "Mike", "phone": "+40791882123", "email": "michael@yahoo.com"},
            [
                ("_name", "Mike"),
                ("email", "michael@yahoo.com"),
                ("phone", "+40791882123"),
            ],
        ),
        ({4: "four", 2: "two", 1: "one"}, [(1, "one"), (2, "two"), (4, "four")]),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = order_dictionary(value)
        result = "passed" if actual == expected else "failed"

        if result == "failed":
            print(f"\t -> Actual result {actual}\n\t -> Expected is   {expected}.")
            fail_count += 1

    total_count = len(test_data)
    passed_count = total_count - fail_count
    print(
        f"Ran {total_count} tests out of {passed_count} were successful"
        f" and {fail_count} did failed."
    )


def test_count_frequency():
    """we'll test the correctnes of count_frequency function"""

    print("Testing count_frequency() function...")

    test_data = [
        # (value, expected)
        ("", {}),
        (
            "He ordered his regular breakfast. Two eggs sunnyside up, hash browns, and two strips of bacon. He continued to look at the menu wondering if this would be the day he added something new. This was also part of the routine. A few seconds of hesitation to see if something else would be added to the order before demuring and saying that would be all. It was the same exact meal that he had ordered every day for the past two years.",
            {
                "the": 6,
                "he": 4,
                "two": 3,
                "of": 3,
                "to": 3,
                "would": 3,
                "be": 3,
                "ordered": 2,
                "and": 2,
                "if": 2,
                "this": 2,
                "day": 2,
                "added": 2,
                "something": 2,
                "was": 2,
                "that": 2,
                "his": 1,
                "regular": 1,
                "breakfast": 1,
                "eggs": 1,
                "sunnyside": 1,
                "up": 1,
                "hash": 1,
                "browns": 1,
                "strips": 1,
                "bacon": 1,
                "continued": 1,
                "look": 1,
                "at": 1,
                "menu": 1,
                "wondering": 1,
                "new": 1,
                "also": 1,
                "part": 1,
                "routine": 1,
                "a": 1,
                "few": 1,
                "seconds": 1,
                "hesitation": 1,
                "see": 1,
                "else": 1,
                "order": 1,
                "before": 1,
                "demuring": 1,
                "saying": 1,
                "all": 1,
                "it": 1,
                "same": 1,
                "exact": 1,
                "meal": 1,
                "had": 1,
                "every": 1,
                "for": 1,
                "past": 1,
                "years": 1,
            },
        ),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = count_frequency(value)
        result = "passed" if actual == expected else "failed"

        if result == "failed":
            print(f"\t -> Actual result {actual}\n\t -> Expected is   {expected}.")
            fail_count += 1

    total_count = len(test_data)
    passed_count = total_count - fail_count
    print(
        f"Ran {total_count} tests out of {passed_count} were successful"
        f" and {fail_count} did failed."
    )


def main():
    """self checking part"""
    test_create_dict()
    test_find_model_and_year()
    test_order_dictionary()
    test_count_frequency()


duration = timeit.timeit(main, number=1)
now = datetime.now().strftime("%H:%M:%S")
print(f"[{now}] Finished in {duration:.2f} seconds.")
