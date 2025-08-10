# 📜 Problem — Fibonacci Number
# Description:
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1.
# That is, F(0) = 0, F(1) = 1, F(n) = F(n - 1) + F(n - 2) for n > 1.
# Given n, calculate F(n).
#
# Input:
# - An integer `n` where 0 <= n <= 30
#
# Output:
# - An integer representing the nth Fibonacci number
#
# Status: ✅ SOLVED

class Solution1(object):
    def fib(self, n):
        if n <= 1:
            return n
            
        base_fib = [0, 1]
        right = 1

        while len(base_fib) <= n:
            base_fib.append(base_fib[right - 1] + base_fib[right])
            right += 1

        return base_fib[n]

class Solution2(object):
    def fib(self, n):
        if n <= 1:
            return n
            
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

# Test cases with assertions
sol1 = Solution1()
sol2 = Solution2()

# Example 1
assert sol1.fib(0) == 0
assert sol2.fib(0) == 0

# Example 2
assert sol1.fib(1) == 1
assert sol2.fib(1) == 1

# Example 3
assert sol1.fib(2) == 1
assert sol2.fib(2) == 1

# Example 4
assert sol1.fib(3) == 2
assert sol2.fib(3) == 2

# Example 5
assert sol1.fib(4) == 3
assert sol2.fib(4) == 3

# Example 6
assert sol1.fib(5) == 5
assert sol2.fib(5) == 5

# Example 7
assert sol1.fib(6) == 8
assert sol2.fib(6) == 8

# Example 8
assert sol1.fib(10) == 55
assert sol2.fib(10) == 55

print("All test cases passed!")