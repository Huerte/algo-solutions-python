from collections import Counter


def buddy_strings(a, b):
    return len(a) == len(b) and Counter(a) == Counter(b)


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

print("All test cases passed! ✅")