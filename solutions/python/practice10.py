# Problem: First Letter to Appear Twice
# Source: https://leetcode.com/problems/first-letter-to-appear-twice/
# Note: Solves the First Letter to Appear Twice problem
# Time: O(n), Space: O(n)
# Topic: strings, hash map
# Description:
# Given a string, find the first letter that appears twice. Return the first letter that has
# a duplicate occurrence earlier in the string.
# 
# Example:
# - Input: "abccbaacz" → Output: "c" (first appears at index 2, then again at index 3)
# - Input: "abcdd" → Output: "d" (first appears at index 3, then again at index 4)
# 
# Explanation (plain English):
# We read the string one letter at a time and keep a "seen" box of letters.
# For each letter, we check the box. If the letter is already there, it is
# the first one to repeat, so we return it. If not, we put it in the box.
# If we reach the end with no repeat, we return None.
#
# Status: ✅ SOLVED

def first_letter_twice(s):
    if not s:
        return None
    
    seen = set()
    for letter in s:
        if letter in seen:
            return letter
        seen.add(letter)
    
    return None  # No letter appears twice

# Test cases with assertions
assert first_letter_twice("abccbaacz") == "c"
assert first_letter_twice("abcdd") == "d"
assert first_letter_twice("abcdefghijklmnopqrstuvwxyz") == None
assert first_letter_twice("a") == None
assert first_letter_twice("aa") == "a"
assert first_letter_twice("") == None
assert first_letter_twice("hello") == "l"

print("All test cases passed!")
