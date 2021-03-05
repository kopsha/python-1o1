"""Translate from Romanian to Pasareasca"""

from datetime import datetime
import timeit


def pasareasca(text):
    # TODO change the code without modifing parsed text
    """This function adds after each vowel is added "p" + that vowel
    In case the word is ending with a consonat îpî is added
    """
    vowels = "aăâeiîou"
    i = 0
    while i < len(text):
        if text[i].lower() in vowels:
            if i == 0:
                text = text[: i + 1] + "p" + text[i:].lower()
            else:
                text = text[: i + 1] + "p" + text[i:]
            i += 2  # increment iterator to exclude p and the vowel inserted above
        i += 1
    return text


def test_pasareasca():
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
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = pasareasca(value)
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
    test_pasareasca()


duration = timeit.timeit(main, number=1)
now = datetime.now().strftime("%H:%M:%S")
print(f"[{now}] Finished in {duration:.2f} seconds.")
