import pytest
from coconuts import coconut_translator

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

if __name__ == "__main__":
    test_coconut_translator()