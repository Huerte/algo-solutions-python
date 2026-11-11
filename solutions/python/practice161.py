# Find Closest Person
# Problem: Find Closest Person
# Source: https://leetcode.com/problems/find-closest-person/
# Note: Compares the distances of two people from a third person and returns the closer person's number.

class Solution(object):
    def findClosest(self, x, y, z):
        if abs(x - z) == abs(y - z):
            return 0
        elif abs(x - z) > abs(y - z):
            return 2
        else:
            return 1

s = Solution()
print(s.findClosest(1, 2, 3))
