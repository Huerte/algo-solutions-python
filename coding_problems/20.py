# 📜 Problem — Count Capital Letters in String
# Description:
# Given a string, count the number of capital letters (uppercase characters) in it.
# The count starts at 1 and increments for each capital letter found.
#
# Input:
# - A string `s` containing letters
#
# Output:
# - An integer representing the count of capital letters plus 1
#
# Status: ✅ SOLVED

def countCapitalLetters(s):
    if not s:
        return 1
        
    count = 1
    for char in s:
        if char.isupper():
            count += 1
    return count

# Test cases with assertions
# Example 1
assert countCapitalLetters("HelloWorld") == 3  # H, W are capital

# Example 2
assert countCapitalLetters("hello") == 1  # No capitals

# Example 3
assert countCapitalLetters("HELLO") == 6  # All capitals

# Example 4
assert countCapitalLetters("hElLo") == 2  # E, L are capital

# Example 5
assert countCapitalLetters("A") == 2  # A is capital

# Example 6
assert countCapitalLetters("a") == 1  # No capitals

# Edge cases
assert countCapitalLetters("") == 1
assert countCapitalLetters("123") == 1  # No letters
assert countCapitalLetters("!@#") == 1  # No letters

print("All test cases passed!")