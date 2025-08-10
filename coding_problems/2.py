# 📜 Problem — Sqrt(x)
# Description:
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
#
# Input:
# - A non-negative integer `x` where 0 <= x <= 2^31 - 1
#
# Output:
# - An integer representing the square root of x rounded down
#
# Status: ✅ SOLVED

class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
            
        difference = 1
        initial_guess = x / 2
        prev_result = 0

        while difference > 0.1:
            initial_guess = (initial_guess + (x / initial_guess)) / 2
            difference = abs(prev_result - initial_guess)
            prev_result = initial_guess

        return int(initial_guess)

# Test cases with assertions
sol = Solution()

# Example 1
assert sol.mySqrt(4) == 2

# Example 2
assert sol.mySqrt(8) == 2

# Example 3
assert sol.mySqrt(16) == 4

# Example 4
assert sol.mySqrt(25) == 5

# Example 5
assert sol.mySqrt(0) == 0

# Example 6
assert sol.mySqrt(1) == 1

# Edge cases
assert sol.mySqrt(2) == 1
assert sol.mySqrt(3) == 1
assert sol.mySqrt(15) == 3

print("All test cases passed!")