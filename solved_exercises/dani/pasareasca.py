"""Translate from Romanian to Pasareasca"""

from datetime import datetime
import timeit


def translate_pasareasca(text):
    """This function adds after each vowel is added "p" + that vowel
    """
    vowels = "aăâeiîou"
    result = ""
    for letter in text:
        result += letter
        if letter.lower() in vowels:
            result += "p" + letter.lower()
    return result

def test_translate_pasareasca():
    """we'll test the correctnes of pasareasca function"""

    print("Testing test_pasareasca() function...")

    test_data = [
        # (value, expected)
        ("", ""),
        ("Câine", "Câpâipinepe"),
        ("Ce mai faci?", "Cepe mapaipi fapacipi?"),
        ("Unde mergi?", "Upundepe mepergipi?"),
        ("Îmi este dor de tine.", "Îpîmipi epestepe dopor depe tipinepe."),
        ("Pe mine mă cheamă Daniel", "Pepe mipinepe măpă chepeapamăpă Dapanipiepel"),
        ("Pisică", "Pipisipicăpă"),
        ("Pe mine ma cheama, Daniel", "Pepe mipinepe mapa chepeapamapa, Dapanipiepel"),
        ("Salut! Ce mai faci?", "Sapaluput! Cepe mapaipi fapacipi?"),
        ("Salut! Ai mere?", "Sapaluput! Apaipi meperepe?"),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = translate_pasareasca(value)
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
    test_translate_pasareasca()


duration = timeit.timeit(main, number=1)
now = datetime.now().strftime("%H:%M:%S")
print(f"[{now}] Finished in {duration:.2f} seconds.")
