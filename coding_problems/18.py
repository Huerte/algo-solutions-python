# 📜 Problem — Remove Digits from String
# Description:
# Given a string s, remove all digits from the string. When a digit is encountered, 
# remove the character that comes before it as well.
# This appears to be a custom string manipulation problem.
#
# Input:
# - A string `s` containing letters and digits
#
# Output:
# - A string with digits and their preceding characters removed
#
# Status: ✅ SOLVED

# def clearDigits(s):
#     if not s:
#         return ""
        
#     result = []
#     for char in s:
#         if char.isdigit():
#             if result:  # Only pop if there's something to pop
#                 result.pop()
#         else:
#             result.append(char)

#     return ''.join(result)

def clearDigits(s):
    arr = []

    for c in s:
        if arr and c.isdigit():
            arr.pop()
        elif not c.isdigit():
            arr.append(c)
            
    return ''.join(arr)

# Test cases with assertions
# Example 1
assert clearDigits("a1bc2d3") == "b"

# Example 2
assert clearDigits("abc123") == ""

# Example 3
assert clearDigits("a1b2c3") == ""

# Example 4
assert clearDigits("1a2b3c") == "c"

# Example 5
assert clearDigits("abc") == "abc"

# Example 6
assert clearDigits("a1b") == "b"

# Edge cases
assert clearDigits("") == ""
assert clearDigits("1") == ""
assert clearDigits("a") == "a"
assert clearDigits("12") == ""

print("All test cases passed!")