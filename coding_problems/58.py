# 📜 Problem — Length of Last Word
# Description:
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
#
# Input:
# - s: A string where 1 <= s.length <= 10^4
# - s consists of only English letters and spaces ' '
# - There will be at least one word in s
#
# Output:
# - An integer representing the length of the last word
#
# Status: ✅ SOLVED

def lengthOfLastWord(s):
    # Remove trailing spaces and split by spaces
    words = s.strip().split()
    
    if not words:
        return 0
    
    return len(words[-1])

# Test cases with assertions
# Example 1
assert lengthOfLastWord("Hello World") == 5

# Example 2
assert lengthOfLastWord("   fly me   to   the moon  ") == 4

# Example 3
assert lengthOfLastWord("luffy is still joyboy") == 6

# Edge cases
assert lengthOfLastWord("a") == 1
assert lengthOfLastWord("   a   ") == 1
assert lengthOfLastWord("word") == 4
assert lengthOfLastWord("   word   ") == 4

print("All test cases passed!")