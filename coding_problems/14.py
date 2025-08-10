# 📜 Problem — Palindrome Number
# Description:
# Given an integer x, return true if x is a palindrome, and false otherwise.
# An integer is a palindrome when it reads the same backward as forward.
#
# Input:
# - An integer `x` where -2^31 <= x <= 2^31 - 1
#
# Output:
# - A boolean indicating whether the number is a palindrome
#
# Status: ✅ SOLVED

def isPalindrome1(n):
    if n < 0:
        return False
        
    extracted_n = []
    temp = n
    while temp > 0:
        extracted_n.append(temp % 10)
        temp //= 10
    return extracted_n == extracted_n[::-1]

def isPalindrome2(n):
    if n < 0:
        return False
        
    n_str = str(n)
    return n_str == n_str[::-1]

# Test cases with assertions
# Example 1
assert isPalindrome1(121) == True
assert isPalindrome2(121) == True

# Example 2
assert isPalindrome1(-121) == False
assert isPalindrome2(-121) == False

# Example 3
assert isPalindrome1(10) == False
assert isPalindrome2(10) == False

# Example 4
assert isPalindrome1(123) == False
assert isPalindrome2(123) == False

# Example 5
assert isPalindrome1(1001) == True
assert isPalindrome2(1001) == True

# Example 6
assert isPalindrome1(0) == True
assert isPalindrome2(0) == True

# Edge cases
assert isPalindrome1(1) == True
assert isPalindrome2(1) == True
assert isPalindrome1(12321) == True
assert isPalindrome2(12321) == True

print("All test cases passed!")
