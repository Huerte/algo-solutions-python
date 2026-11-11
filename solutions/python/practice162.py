# Mirror Distance of an Integer
# Problem: Mirror Distance of an Integer
# Source: https://leetcode.com/problems/mirror-distance-of-an-integer/
# Note: Calculates the absolute difference between an integer and its reversed form.

class Solution(object):
    def mirrorDistance(self, n):
        return abs(n - int(str(n)[::-1]))
