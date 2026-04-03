# Find Closest Person

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