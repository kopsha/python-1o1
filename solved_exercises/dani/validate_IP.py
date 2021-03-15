"""Validate IP Address Exercise"""
import pytest
from datetime import datetime
import timeit
import ipaddress


def is_valid_IPv4(value):
    """This function is chcking if an IP v4 address is valid"""
    pieces = value.split(".")

    if len(pieces) != 4:
        return False

    for piece in pieces:
        if not piece.isnumeric():
            return False
        as_str = str(int(piece))
        as_int = int(piece)
        if as_str != piece or as_int < 0 or as_int > 255:
            return False

    return True


def is_valid_IPv6(value):
    """This function is chcking if an IP v6 address is valid"""

    pieces = value.split(":")
    hex_values = "0123456789abcdefABCDEF"

    for letter in value:
        if letter not in hex_values and letter not in ":":
            return False

    if len(pieces) != 8:
        return False

    for piece in pieces:
        if len(piece) == 0:
            return False
        as_int = int(piece, 16)
        if len(piece) > 4 or as_int < 0 or as_int > int("FFFF", 16):
            return False
    return True


def is_valid_IP(value):
    try:
        ipaddress.ip_address(value)
        return True
    except:
        return False


def test_is_valid_IPv4():
    assert is_valid_IPv4("") == False
    assert is_valid_IPv4("192.168.0.1") == True
    assert is_valid_IPv4(".192.168.0.1") == False
    assert is_valid_IPv4(" 192.168.0.1") == False
    assert is_valid_IPv4("0.34.82.53") == True
    assert is_valid_IPv4("123.045.067.089") == False
    assert is_valid_IPv4("192.168. 1.1") == False
    assert is_valid_IPv4("0192.168.0.1") == False
    assert is_valid_IPv4("0.0.0.0") == True
    assert is_valid_IPv4("255.255.255.255") == True
    assert is_valid_IPv4("192.168.1.256") == False
    assert is_valid_IPv4("abc.def.ghi.jkl") == False
    assert is_valid_IPv4("abc.def.ghi.1") == False
    assert is_valid_IPv4("12.34.56") == False
    assert is_valid_IPv4("12.34.56 .1") == False
    assert is_valid_IPv4("12.34.56.-1") == False


def test_is_valid_IPv6():
    assert is_valid_IPv6("") == False
    assert is_valid_IPv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == True
    assert is_valid_IPv6(":2001:0db8:85a3:0000:0000:8a2e:0370:7334:") == False
    assert is_valid_IPv6(" 2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert is_valid_IPv6("2001:db8:85a3:0:0:8A2E:0370:7334") == True
    assert is_valid_IPv6("2001:0db8:85a3:::8A2E:0370:7334") == False
    assert is_valid_IPv6("2001:db8:85a3:0:0: 8A2E:0370:7334") == False
    assert is_valid_IPv6("02001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert is_valid_IPv6("2001:0db8:85a3:0000:0000:8a2e:0370:defg") == False
    assert is_valid_IPv6("db8:85a3:0:0:8A2E:0370:7334") == False
    assert is_valid_IPv6("2001:db8:85a3:0:0:8A2E:0370:-7334") == False


def test_is_valid_IP():
    assert is_valid_IP("") == False
    assert is_valid_IP("192.168.0.1") == True
    assert is_valid_IP(".192.168.0.1") == False
    assert is_valid_IP(" 192.168.0.1") == False
    assert is_valid_IP("0.34.82.53") == True
    assert is_valid_IP("123.045.067.089") == True
    assert is_valid_IP("0192.168.0.1") == False
    assert is_valid_IP("0.0.0.0") == True
    assert is_valid_IP("255.255.255.255") == True
    assert is_valid_IP("192.168.1.256") == False
    assert is_valid_IP("abc.def.ghi.jkl") == False
    assert is_valid_IP("abc.def.ghi.1") == False
    assert is_valid_IP("12.34.56") == False
    assert is_valid_IP("12.34.56 .1") == False
    assert is_valid_IP("12.34.56.-1") == False
    assert is_valid_IP("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == True
    assert is_valid_IP(":2001:0db8:85a3:0000:0000:8a2e:0370:7334:") == False
    assert is_valid_IP(" 2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert is_valid_IP("2001:db8:85a3:0:0:8A2E:0370:7334") == True
    assert is_valid_IP("2001:0db8:85a3:::8A2E:0370:7334") == False
    assert is_valid_IP("2001:db8:85a3:0:0: 8A2E:0370:7334") == False
    assert is_valid_IP("02001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert is_valid_IP("2001:0db8:85a3:0000:0000:8a2e:0370:defg") == False
    assert is_valid_IP("db8:85a3:0:0:8A2E:0370:7334") == False
    assert is_valid_IP("2001:db8:85a3:0:0:8A2E:0370:-7334") == False
