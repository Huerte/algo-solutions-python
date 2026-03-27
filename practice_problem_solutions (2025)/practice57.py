# 📜 Problem — Number Power Sum
# Description:
# Given a number and a power, reverse the number, raise each digit to the given power, 
# and concatenate the results to form a new number.
# This appears to be a custom mathematical problem.
#
# Input:
# - A number as a string `x` in format "number power"
# - Example: "123 2" means number 123 with power 2
#
# Output:
# - A string representing the concatenated results
#
# Status: 🔄 IN PROGRESS - Needs clarification

import math

def number_power_sum(x):
    # Parse input
    nums = x.split(' ')
    if len(nums) != 2:
        return "Invalid input format"
    
    number = nums[0]
    power = int(nums[1])
    
    # Reverse the number
    rev_num = number[::-1]
    result = ''
    
    # Raise each digit to the power and concatenate
    for digit in rev_num:
        result += str(int(math.pow(int(digit), power)))
    
    return result

# Test cases with assertions
# Example 1
assert number_power_sum("123 2") == "941"

# Example 2
assert number_power_sum("12 3") == "81"

# Example 3
assert number_power_sum("5 2") == "25"

# Example 4
assert number_power_sum("10 1") == "01"

print("All test cases passed!")