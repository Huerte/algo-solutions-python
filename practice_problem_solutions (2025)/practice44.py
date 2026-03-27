# 📜 Problem — Character Percentage in String
# Description:
# Given a string s and a character c, return the percentage of characters in s that equal c.
# The percentage is rounded down to the nearest integer.
#
# Input:
# - A string `s` where 1 <= s.length <= 100
# - A character `c` to count in the string
#
# Output:
# - An integer representing the percentage of characters equal to c
#
# Status: ✅ SOLVED

# def percentageString(s, c):
#     if not s:
#         return 0
        
#     count = s.count(c)
#     return int((count / len(s)) * 100)

def percentageString(s, c):
    if not s:
        return 0
    return int(s.count(c)/len(s) * 100)

# Test cases with assertions
# Example 1
assert percentageString("hello", "l") == 40

# Example 2
assert percentageString("aabbcc", "a") == 33

# Example 3
assert percentageString("testcase", "t") == 25

# Example 4
assert percentageString("aaaaa", "a") == 100

# Example 5
assert percentageString("abcde", "z") == 0

# Example 6
assert percentageString("a", "a") == 100

# Edge cases
assert percentageString("", "a") == 0
assert percentageString("abc", "a") == 33

print("All test cases passed!")