def is_leap_year(year: int) -> bool:
    """
    Determines if a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is not divisible by 100, unless also divisible by 400.

    Args:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """

    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0






























print(is_leap_year(1600))


# Test cases
# Leap years
assert is_leap_year(1600) == True
assert is_leap_year(2000) == True
assert is_leap_year(2016) == True
assert is_leap_year(2020) == True
assert is_leap_year(2024) == True
assert is_leap_year(2400) == True
assert is_leap_year(2800) == True
assert is_leap_year(2028) == True
assert is_leap_year(2096) == True
assert is_leap_year(1932) == True

# Non-leap years
assert is_leap_year(1700) == False
assert is_leap_year(1800) == False
assert is_leap_year(1900) == False
assert is_leap_year(2017) == False
assert is_leap_year(2023) == False
assert is_leap_year(2100) == False
assert is_leap_year(2200) == False
assert is_leap_year(2300) == False
assert is_leap_year(2500) == False
assert is_leap_year(2600) == False
assert is_leap_year(1999) == False
assert is_leap_year(1987) == False
print("Pass all test cases!!!!!!!!")