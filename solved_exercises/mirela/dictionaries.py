def create_dict(list1, list2):
    """Create a dictionary out of the two given lists """
    if len(list1) != len(list2):
        raise ValueError("list1 and list2 shall must have the same length.")
    new_dict = dict(zip(list1, list2))
    return new_dict


def car_attribute(car_info):
    """Prints the model and the year of the car or the string N/A if the value is not present"""
    if not isinstance(car_info, dict):
        raise TypeError("Expected input is a dictionary.")
    car_model = car_info.get("model", "N/A")
    car_year = car_info.get("year", "N/A")
    return f"The car is a {car_model} from {car_year}"


def order_dict(given_dict):
    """Prints all the key value pairs of a dictionary with the keys ordered alphabetically"""
    if not isinstance(given_dict, dict):
        raise TypeError("Expected input is a dictionary.")
    ordered_dict = dict(sorted(given_dict.items()))
    return ordered_dict


def test_car_attribute():
    """we'll test the correctness of car_attribute function"""

    print("Testing car_attribute function...")

    test_data = [
        # (value, expected)
        ({'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}, "The car is a Mustang from 1964"),
        ({'sun': 'warm', 'sleep': 'good', 'weekend': 'perfect'}, "The car is a N/A from N/A"),
        ({'brand': 'Ford', 'result': 'ok', 'year': '1964'}, "The car is a N/A from 1964"),

    ]

    fail_count = 0
    for value, expected in test_data:
        actual = car_attribute(value)
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


def test_order_dict():
    """we'll test the correctness of order_dict function"""

    print("Testing order_dict function...")

    test_data = [
        # (value, expected)
        ({'name': 'zoe', 'age': '47', 'drug1': 'algifor','50ml': 'dosage'},
         {'50ml': 'dosage', 'age': '47', 'drug1': 'algifor', 'name': 'zoe'}),
        ({'weekend': 'perfect', 'sleep': 'good', 'sun': 'warm'},
         {'sun': 'warm', 'sleep': 'good', 'weekend': 'perfect'}),
        ({'Xplane': 'Madrid', 'Uplane': 'Roma', 'JPlane': 'France','Cplane': 'London'},
         {'Cplane': 'London', 'JPlane': 'France', 'Uplane': 'Roma', 'Xplane': 'Madrid'}),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = order_dict(value)
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
    test_car_attribute()
    test_order_dict()
    print(create_dict(["name", "phone", "email"], ["Mike", "+40791882123", "michael@yahoo.com"]))

main()

