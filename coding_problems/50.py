# 📜 Problem — Pow(x, n)
# Description:
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
#
# Input:
# - x: A double representing the base number
# - n: An integer representing the exponent
# - -100.0 < x < 100.0
# - -2^31 <= n <= 2^31-1
# - n is an integer
# - -10^4 <= x^n <= 10^4
#
# Output:
# - A double representing x^n
#
# Status: ✅ SOLVED

def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1
    current_product = x
    
    while n > 0:
        if n % 2 == 1:
            result *= current_product
        current_product *= current_product
        n //= 2
    
    return result

# Test cases with assertions
# Example 1
assert abs(myPow(2.00000, 10) - 1024.00000) < 1e-5

# Example 2
assert abs(myPow(2.10000, 3) - 9.26100) < 1e-5

# Example 3
assert abs(myPow(2.00000, -2) - 0.25000) < 1e-5

# Edge cases
assert abs(myPow(1.00000, 2147483647) - 1.00000) < 1e-5
assert abs(myPow(2.00000, 0) - 1.00000) < 1e-5
assert abs(myPow(0.00001, 2147483647) - 0.00000) < 1e-5

print("All test cases passed!")