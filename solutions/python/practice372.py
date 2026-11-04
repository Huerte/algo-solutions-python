# Geeksforgeeks: Power of 2
# Problem: Power of 2
# Source: https://www.geeksforgeeks.org/problems/power-of-2-1587115620/1
# Note: Checks whether a non-negative integer is an exact power of 2.
class Solution:
    def isPowerofTwo(self, n):
        return bin(n).count('1') == 1

s = Solution()
print(s.isPowerofTwo(1))  # True
print(s.isPowerofTwo(8))  # True
print(s.isPowerofTwo(98)) # False
