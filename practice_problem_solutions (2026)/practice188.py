# Distribute Candies

class Solution(object):
    def distributeCandies(self, candyType):
        cd = len(set(candyType))
        ce = len(candyType) // 2
        return min(ce, cd)

s = Solution()
print(s.distributeCandies([1,1,2,2,3,3])) # 3
print(s.distributeCandies([1,1,2,3]))     # 2
print(s.distributeCandies([6,6,6,6]))     # 1