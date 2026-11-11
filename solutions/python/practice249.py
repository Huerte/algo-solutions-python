# Palindrome Check (Ignoring Non-Alphanumeric)
# Problem: Valid Palindrome
# Source: https://leetcode.com/problems/valid-palindrome/
# Note: Removes non-alphanumeric characters, converts the remaining characters to lowercase, and checks whether the resulting string reads the same forwards and backwards.
def palindrome(s):
    new_s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()
    return new_s == new_s[::-1]

print(palindrome("A man, a plan, a canal: Panama"))
