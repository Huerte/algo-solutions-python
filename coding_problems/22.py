# 📜 Problem — Reverse Integer
# Description:
# Given a 32-bit signed integer, reverse digits of an integer.
# If reversing x causes the value to go outside the signed 32-bit integer range 
# [-2^31, 2^31 - 1], then return 0.
#
# Input:
# - A 32-bit signed integer `x`
#
# Output:
# - The reversed integer, or 0 if overflow occurs
#
# Status: ✅ SOLVED

import math

def reverseN(n: int):
    if n == 0:
        return 0
        
    result = 0
    digitNum = math.ceil(math.log10(abs(n) + 1))
    temp = abs(n)
    
    while temp > 0:
        result += (temp % 10) * math.pow(10, digitNum - 1)
        temp //= 10
        digitNum -= 1
    
    result = math.trunc(result)
    return -result if n < 0 else result

def reverseNOptimized(x: int):
    if x == 0:
        return 0
        
    result = 0
    n = abs(x)
    
    while n > 0:
        result = result * 10 + (n % 10)
        n //= 10
    
    # Check for overflow
    if result > 2**31 - 1:
        return 0
        
    return -result if x < 0 else result

# Test cases with assertions
# Example 1
assert reverseN(123) == 321
assert reverseNOptimized(123) == 321

# Example 2
assert reverseN(146) == 641
assert reverseNOptimized(146) == 641

# Example 3
assert reverseN(135) == 531
assert reverseNOptimized(135) == 531

# Example 4
assert reverseN(-123) == -321
assert reverseNOptimized(-123) == -321

# Example 5
assert reverseN(120) == 21
assert reverseNOptimized(120) == 21

# Edge cases
assert reverseN(0) == 0
assert reverseNOptimized(0) == 0
assert reverseN(1) == 1
assert reverseNOptimized(1) == 1

print("All test cases passed!")
