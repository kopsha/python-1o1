import string

def create_dict(keys, values):
    """Create a dictionary out of the two given lists """
    if len(keys) != len(values):
        raise ValueError("keys and values shall have the same length.")
    new_dict = dict(zip(keys, values))
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

"""Count the frequency of all words in the given text:"""
def count_freq_words(text):
    """Counts the frequency of all words in a given text"""
    new_text = text.split()
    count_words = {}
    for element in new_text:
        word = element.strip(string.punctuation).lower()
        count_words[word] = count_words.get(word, 0) + 1
    return count_words

def test_create_dict():
    assert create_dict(["name", "phone", "email"], ["Mike", "+40791882123", "michael@yahoo.com"]) == {'email': 'michael@yahoo.com', 'name': 'Mike', 'phone': '+40791882123'}

def test_car_attribute():
    assert car_attribute({'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}) == "The car is a Mustang from 1964"
    assert car_attribute({'sun': 'warm', 'sleep': 'good', 'weekend': 'perfect'}) == "The car is a N/A from N/A"
    assert car_attribute({'brand': 'Ford', 'result': 'ok', 'year': '1964'}) == "The car is a N/A from 1964"

def test_order_dict():
    assert order_dict({'name': 'zoe', 'age': '47', 'drug1': 'algifor','50ml': 'dosage'}) == {'50ml': 'dosage', 'age': '47', 'drug1': 'algifor', 'name': 'zoe'}
    assert order_dict({'weekend': 'perfect', 'sleep': 'good', 'sun': 'warm'}) == {'sun': 'warm', 'sleep': 'good', 'weekend': 'perfect'}
    assert order_dict({'Xplane': 'Madrid', 'Uplane': 'Roma', 'JPlane': 'France','Cplane': 'London'}) == {'Cplane': 'London', 'JPlane': 'France', 'Uplane': 'Roma', 'Xplane': 'Madrid'}

def test_count_freq_words():
    text = "He ordered his regular breakfast. Two eggs sunnyside up, hash browns, and two strips of bacon. He continued to look at the menu wondering if this would be the day he added something new. This was also part of the routine. A few seconds of hesitation to see if something else would be added to the order before demuring and saying that would be all. It was the same exact meal that he had ordered every day for the past two years."
    assert count_freq_words(text) == {'he': 4, 'ordered': 2, 'his': 1, 'regular': 1, 'breakfast': 1, 'two': 3, 'eggs': 1, 'sunnyside': 1, 'up': 1, 'hash': 1, 'browns': 1, 'and': 2, 'strips': 1, 'of': 3, 'bacon': 1, 'continued': 1, 'to': 3, 'look': 1, 'at': 1, 'the': 6, 'menu': 1, 'wondering': 1, 'if': 2, 'this': 2, 'would': 3, 'be': 3, 'day': 2, 'added': 2, 'something': 2, 'new': 1, 'was': 2, 'also': 1, 'part': 1, 'routine': 1, 'a': 1, 'few': 1, 'seconds': 1, 'hesitation': 1, 'see': 1, 'else': 1, 'order': 1, 'before': 1, 'demuring': 1, 'saying': 1, 'that': 2, 'all': 1, 'it': 1, 'same': 1, 'exact': 1, 'meal': 1, 'had': 1, 'every': 1, 'for': 1, 'past': 1, 'years': 1}
    assert count_freq_words("I love Python") == {'i': 1, 'love': 1, 'python': 1}
