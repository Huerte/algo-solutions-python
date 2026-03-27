# 📜 Problem — Buddy Strings
# Description:
# Given two strings a and b, return true if you can swap two letters in a so the result is equal to b,
# and false otherwise. Swapping letters is defined as taking two indices i and j (0-indexed) such that
# i != j and swapping the characters at a[i] and a[j].
# 
# Example:
# - Input: a = "ab", b = "ba" → Output: true (swap a[0] and a[1])
# - Input: a = "ab", b = "ab" → Output: false (no swap needed)
# - Input: a = "aa", b = "aa" → Output: true (swap a[0] and a[1] to get same string)
# 
# Status: ✅ SOLVED

from collections import Counter

def buddy_strings(a, b):
    # Check if strings have same length and character counts
    return len(a) == len(b) and Counter(a) == Counter(b)

# Test cases with assertions
# ✅ Valid buddy strings (same length, same character counts)
assert buddy_strings("ab", "ba") == True
assert buddy_strings("aabb", "bbaa") == True
assert buddy_strings("abc", "cab") == True
assert buddy_strings("aa", "aa") == True  # Identical strings with duplicates

# ❌ Not buddy strings
assert buddy_strings("abc", "abd") == False  # Different characters
assert buddy_strings("abcd", "abcc") == False  # Different frequencies
assert buddy_strings("abc", "cbaa") == False  # Different lengths
assert buddy_strings("a", "a") == True  # Single character (no swap possible)
assert buddy_strings("", "a") == False

print("All test cases passed!")