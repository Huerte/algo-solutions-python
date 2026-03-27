# 📜 Problem — Create Phone Number
# Description:
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns 
# a string of those numbers in the form of a phone number.
# The returned format must be correct in order for this challenge to pass.
#
# Input:
# - An array of 10 integers where each integer is between 0 and 9
#
# Output:
# - A string in the format "(XXX) XXX-XXXX"
#
# Status: 🔄 IN PROGRESS - Needs fixing

def create_phone_number(n):
    if len(n) != 10 or max(n) > 9 or min(n) < 0:
        return ''
    
    # Convert integers to strings and join them
    n_str = ''.join(map(str, n))
    
    # Format as phone number
    return f"({n_str[:3]}) {n_str[3:6]}-{n_str[6:]}"

# Test cases with assertions
# Example 1
assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"

# Example 2
assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"

# Example 3
assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"

# Example 4
assert create_phone_number([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "(987) 654-3210"

# Edge cases
assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == "(123) 456-7899"

print("All test cases passed!")