"""
"coconuts" has 8 letters.
A byte in binary has 8 bits.
A byte can represent a character.
We can use the word "coconuts" to communicate with each other in binary if we
use upper case letters as 1s and lower case letters as 0s.

Create a function that translates a word in plain text, into Coconut.

Worked Example
The binary for "coconuts" is
01100011 01101111 01100011 01101111 01101110 01110101 01110100 01110011
c         o        c       o       n        u        t       s

Since 0s are lowercase and 1s are uppercase, we can map the binary like this.
cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS

coconut_translator("coconuts") ➞ "cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS"
Examples
coconut_translator("Hi") ➞ "cOcoNuts cOCoNutS"

coconut_translator("edabit") ➞ "cOConUtS cOConUts cOConutS cOConuTs cOCoNutS cOCOnUts"

coconut_translator("123") ➞ "coCOnutS coCOnuTs coCOnuTS"
Notes
All inputs will be strings.
Make sure to separate the coconuts with spaces.
"""


def coconut_translator(text):
    eight_letters_word = "coconuts"
    translation = ""
    for letter in text:
        letter_bits = "{0:08b}".format(ord(letter))
        for i, bit in enumerate(letter_bits):
            if bit == "1":
                translation += eight_letters_word[i].upper()
            else:
                translation += eight_letters_word[i]
        translation += " "
    translation = translation[:-1]
    return translation


def test_coconut_translator():
    assert coconut_translator("Hi") == "cOcoNuts cOCoNutS"
    assert (
        coconut_translator("edabit")
        == "cOConUtS cOConUts cOConutS cOConuTs cOCoNutS cOCOnUts"
    )
    assert coconut_translator("123") == "coCOnutS coCOnuTs coCOnuTS"
    assert (
        coconut_translator("coconuts")
        == "cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS"
    )
    assert coconut_translator("") == ""
