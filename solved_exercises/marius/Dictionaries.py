# Functions exercises 1, 2, 3 and 4
import re
import operator
import math

"""Create a dictionary out of the lists below:

keys = ["name", "phone", "email"]
values = ["Mike", "+40791882123", "michael@yahoo.com"]

# Expected output
{'name': 'Mike', 'phone': '+40791882123', 'email': 'michael@yahoo.com'}"""

def create_dict(list_keys, list_values):
    """ Creates a dictionary out of two lists """
    if len(list_keys) != len(list_values):
        raise ValueError("Keys input list and values input list must have same length.")
    dict_new = dict(zip(list_keys, list_values))
    return dict_new

"""Given a dictionary describing a car attributes, print the model and the year of the car or the string N/A if the value is not present.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}"""

def print_car_model(car_info):
    """ print car model and year based on input dictionary with information """
    if not isinstance(car_info, dict):
        raise TypeError("Expected input is a dictionary with car/'s information")
    car_brand = car_info.get("brand", "N/A")
    car_model = car_info.get("model", "N/A")
    year_model = car_info.get("year", "N/A")
    return f"This car is a {year_model} {car_brand} {car_model}."

"""Print all the key value pairs of any dictionary, but make sure they are shown in the same order every time (order the keys alphabetically)."""

def print_dict_sorted(input_dict):
    """ Creates a sorted dictionary based on a given dictionary"""
    sorted_dict = dict(sorted(input_dict.items()))
    return sorted_dict

"""Count the frequency of all words in the given text:"""
def count_freq_words(text):
    all_words = re.findall(r"[\w']+", text)
    new_dict = {word: all_words.count(word) for word in all_words}
    sorted_dict = dict(sorted(new_dict.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_dict
text = "He ordered his regular breakfast. Two eggs sunnyside up, hash browns, and two strips of bacon. He continued to look at the menu wondering if this would be the day he added something new. This was also part of the routine. A few seconds of hesitation to see if something else would be added to the order before demuring and saying that would be all. It was the same exact meal that he had ordered every day for the past two years."
print(count_freq_words(text))

def calculate_polynom_second_grade(xtwo, xone, xzero):
    delta = xone**2 - 4*xtwo*xzero
    if delta < 0:
        raise ValueError("Solutions of this polynom are complex numbers")
    solution1 = (-xone + math.sqrt(delta))/2*xzero
    solution2 = (-xone - math.sqrt(delta))/2*xzero
    return solution1, solution2

print(calculate_polynom_second_grade(2,-6,4))


def test_create_dict():
    """we'll test the correctness of dict function"""

    print("Testing dict const() function...")

    test_data = [
        # (value, expected)
        ([["name", "phone", "email"], ["Mike", "+40791882123", "michael@yahoo.com"]], {'name': 'Mike', 'phone': '+40791882123', 'email': 'michael@yahoo.com'}),

    ]

    fail_count = 0
    for value, expected in test_data:
        actual = create_dict(value, )
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

def test_print_car_model():
    """we'll test the correctness of print_car_model function"""

    print("Testing print_car_model() function...")

    test_data = [
        # (value, expected)
        ({'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}, "This car is a 1964 Ford Mustang."),
        ({'brand1': 'Ford', 'model1': 'Mustang', 'year1': '1964'}, "This car is a N/A N/A N/A."),
        ({'brand1': 'Ford', 'model': 'Mustang', 'year': '1964'}, "This car is a 1964 N/A Mustang."),

    ]

    fail_count = 0
    for value, expected in test_data:
        actual = print_car_model(value)
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

def test_print_dict_sorted():
    """we'll test the correctness of print_car_model function"""

    print("Testing print_car_model() function...")

    test_data = [
        # (value, expected)
        ({'name': 'Mike', 'phone': '+40791882123', 'email': 'michael@yahoo.com'}, {'email': 'michael@yahoo.com', 'name': 'Mike', 'phone': '+40791882123'}),

    ]

    fail_count = 0
    for value, expected in test_data:
        actual = print_dict_sorted(value)
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
    #test_create_dict()
    #print(create_dict(["name", "phone", "email"], ["Mike", "+40791882123", "michael@yahoo.com"]))
    #test_print_car_model()
    test_print_dict_sorted()


main()
