# Dictionary Functions exercises 1, 2, 3 and 4
import string
import pytest

def create_dict(keys, values):
    """ Creates a dictionary out of two lists """
    if len(keys) != len(values):
        raise ValueError("Keys input list and values input list must have same length.")
    dictionary = dict(zip(keys, values))
    return dictionary


def print_car_model(car_info):
    """ print car model and year based on input dictionary with information """
    if not isinstance(car_info, dict):
        raise TypeError("Expected input is a dictionary with car/'s information")
    car_model = car_info.get("model", "N/A")
    year_model = car_info.get("year", "N/A")
    return f"This car is a {year_model} {car_model}."


def print_dict_sorted(input_dict):
    """ Creates a sorted dictionary based on a given dictionary"""
    sorted_dict = dict(sorted(input_dict.items()))
    return sorted_dict


def count_freq_words(text):
    """Count the frequency of all words in the given text:"""
    if not isinstance(text, str):
        raise TypeError("Expected input is a string.")
    all_words = text.split()
    freq_words = {}
    for word in all_words:
        clean_word = word.strip(string.punctuation).lower()
        freq_words[clean_word] = freq_words.get(clean_word, 0) + 1
    return freq_words

def test_create_dict():
    assert create_dict(["name", "phone", "email"], ["Mike", "+40791882123", "michael@yahoo.com"]) == {'email': 'michael@yahoo.com', 'name': 'Mike', 'phone': '+40791882123'}

def test_print_car_model():
    assert print_car_model({'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}) == "This car is a 1964 Mustang."
    assert print_car_model({'sun': 'warm', 'sleep': 'good', 'weekend': 'perfect'}) == "This car is a N/A N/A."
    assert print_car_model({'brand': 'Ford', 'result': 'ok', 'year': '1964'}) == "This car is a 1964 N/A."

def test_dict_sorted():
    assert print_dict_sorted({'name': 'zoe', 'age': '47', 'drug1': 'algifor','50ml': 'dosage'}) == {'50ml': 'dosage', 'age': '47', 'drug1': 'algifor', 'name': 'zoe'}
    assert print_dict_sorted({'weekend': 'perfect', 'sleep': 'good', 'sun': 'warm'}) == {'sun': 'warm', 'sleep': 'good', 'weekend': 'perfect'}
    assert print_dict_sorted({'Xplane': 'Madrid', 'Uplane': 'Roma', 'JPlane': 'France','Cplane': 'London'}) == {'Cplane': 'London', 'JPlane': 'France', 'Uplane': 'Roma', 'Xplane': 'Madrid'}

def test_count_freq_words():
    text = "He ordered his regular breakfast. Two eggs sunnyside up, hash browns, and two strips of bacon. He continued to look at the menu wondering if this would be the day he added something new. This was also part of the routine. A few seconds of hesitation to see if something else would be added to the order before demuring and saying that would be all. It was the same exact meal that he had ordered every day for the past two years."
    assert count_freq_words(text) == {'he': 4, 'ordered': 2, 'his': 1, 'regular': 1, 'breakfast': 1, 'two': 3, 'eggs': 1, 'sunnyside': 1, 'up': 1, 'hash': 1, 'browns': 1, 'and': 2, 'strips': 1, 'of': 3, 'bacon': 1, 'continued': 1, 'to': 3, 'look': 1, 'at': 1, 'the': 6, 'menu': 1, 'wondering': 1, 'if': 2, 'this': 2, 'would': 3, 'be': 3, 'day': 2, 'added': 2, 'something': 2, 'new': 1, 'was': 2, 'also': 1, 'part': 1, 'routine': 1, 'a': 1, 'few': 1, 'seconds': 1, 'hesitation': 1, 'see': 1, 'else': 1, 'order': 1, 'before': 1, 'demuring': 1, 'saying': 1, 'that': 2, 'all': 1, 'it': 1, 'same': 1, 'exact': 1, 'meal': 1, 'had': 1, 'every': 1, 'for': 1, 'past': 1, 'years': 1}
    assert count_freq_words("I love Python") == {'i': 1, 'love': 1, 'python': 1}
