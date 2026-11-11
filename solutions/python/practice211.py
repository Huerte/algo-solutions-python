# CodeWars - IP Validation
# Problem: IP Validation
# Source: https://www.codewars.com/kata/515decfd9dcfc23bb6000006
# Note: Validates IPv4 addresses by checking four numeric octets, their valid range, and the absence of leading zeros.
# My waster unelegant solution
import re
def is_valid_IP(strng):
    pattern = re.compile(
        r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
    )
    return bool(pattern.fullmatch(strng))

# Solution of other user
def is_valid_IP(strng):
    if len(strng.split(".")) != 4:
        return False
    
    for group in strng.split("."):
        if not group.isdigit() or group != str(int(group)) or not 0 <= int(group) <= 255:
            return False
    return True

print(is_valid_IP("123.123.123.123"))  # True
print(is_valid_IP("123.123.123.1234")) # False
print(is_valid_IP("123.123.123"))      # False
print(is_valid_IP("1.2.3.4"))          # True
print(is_valid_IP("1.2.3"))            # False
