# 📜 Problem — Alternating Digit Sum
# Description:
# Given a positive integer n, return the alternating digit sum of n.
# The alternating digit sum is the sum of the digits where the sign alternates 
# starting with positive for the leftmost digit.
#
# Input:
# - A positive integer `n`
#
# Output:
# - An integer representing the alternating digit sum
#
# Status: ✅ SOLVED

import math

def sumAlternatingDigit(n):
    if n == 0:
        return 0
        
    digitNum = math.floor(math.log10(abs(n))) + 1
    sign = 1

    if digitNum % 2 == 0:
       sign = -1

    totalSum = []

    while n > 0:
        m = n % 10 * sign
        totalSum.append(m)
        n //= 10
        sign *= -1

    return sum(totalSum)

# Test cases with assertions
# Example 1
assert sumAlternatingDigit(4567) == 4 - 5 + 6 - 7

# Example 2
assert sumAlternatingDigit(123) == 1 - 2 + 3

# Example 3
assert sumAlternatingDigit(10) == 1 - 0

# Example 4
assert sumAlternatingDigit(1) == 1

# Example 5
assert sumAlternatingDigit(100) == 1 - 0 + 0

# Example 6
assert sumAlternatingDigit(999) == 9 - 9 + 9

# Edge cases
assert sumAlternatingDigit(0) == 0
assert sumAlternatingDigit(111) == 1 - 1 + 1

print("All test cases passed!")