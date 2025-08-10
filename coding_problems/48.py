# 📜 Problem — Character Triangle Pattern
# Description:
# Given a character and a number n, print a triangle pattern where each row contains an odd number
# of characters, starting with 1 character and incrementing by 2 for each row.
# 
# Example:
# - Input: character="*", n=3
# - Output:
#   *
#  ***
# *****
# 
# Status: ✅ SOLVED

def print_character_triangle(character, n):
    if n <= 0:
        return ""
    
    result = []
    level = 1
    
    for i in range(n):
        # Calculate leading spaces
        spaces = " " * ((n + 2) - (i + 3))
        
        # Create the row with characters
        row = spaces + character * level
        result.append(row)
        
        level += 2
    
    return "\n".join(result)

# Test cases with assertions
# Test with n=3
expected_3 = " *\n***\n*****"
assert print_character_triangle("*", 3) == expected_3

# Test with n=1
assert print_character_triangle("#", 1) == "#"

# Test with n=2
expected_2 = " #\n###"
assert print_character_triangle("#", 2) == expected_2

# Test with n=0
assert print_character_triangle("*", 0) == ""

print("All test cases passed!")