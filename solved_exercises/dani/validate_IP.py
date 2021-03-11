"""Validate IP Address Exercise"""

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
    """we'll test the correctnes of is_valid_IPv4 function"""

    print("Testing is_valid_IPv4() function")

    test_data = [
        # (value, expected)
        ("", False),
        ("192.168.0.1", True),
        (".192.168.0.1.", False),
        (" 192.168.0.1", False),
        ("0.34.82.53", True),
        ("123.045.067.089", False),
        ("192.168. 1.1", False),
        ("0192.168.0.1", False),
        ("0.0.0.0", True),
        ("255.255.255.255", True),
        ("192.168.1.256", False),
        ("abc.def.ghi.jkl", False),
        ("abc.def.ghi.1", False),
        ("12.34.56", False),
        ("12.34.56 .1", False),
        ("12.34.56.-1", False),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = is_valid_IPv4(value)
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


def test_is_valid_IPv6():
    """we'll test the correctnes of is_valid_IPv4 function"""

    print("Testing is_valid_IPv6() function")

    test_data = [
        # (value, expected)
        ("", False),
        ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", True),
        (":2001:0db8:85a3:0000:0000:8a2e:0370:7334:", False),
        (" 2001:0db8:85a3:0000:0000:8a2e:0370:7334", False),
        ("2001:db8:85a3:0:0:8A2E:0370:7334", True),
        ("2001:0db8:85a3:::8A2E:0370:7334", False),
        ("2001:db8:85a3:0:0: 8A2E:0370:7334", False),
        ("02001:0db8:85a3:0000:0000:8a2e:0370:7334", False),
        ("2001:0db8:85a3:0000:0000:8a2e:0370:defg", False),
        ("db8:85a3:0:0:8A2E:0370:7334", False),
        ("2001:db8:85a3:0:0:8A2E:0370:-7334", False),
    ]

    fail_count = 0
    for value, expected in test_data:
        actual = is_valid_IPv6(value)
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
    test_is_valid_IPv4()
    test_is_valid_IPv6()


duration = timeit.timeit(main, number=1)
now = datetime.now().strftime("%H:%M:%S")
print(f"[{now}] Finished in {duration:.2f} seconds.")
