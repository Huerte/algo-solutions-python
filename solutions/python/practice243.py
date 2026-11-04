# Height Checker
# Problem: Height Checker
# Source: https://leetcode.com/problems/height-checker/
# Note: Counts the positions where the original height order differs from the sorted expected order.
class Solution(object):
    def heightChecker(self, heights):
        srt = sorted(heights)
        count = 0
        for x, y in zip(heights, srt):
            if x != y:
                count += 1
        return count

s = Solution()
print(s.heightChecker([1,1,4,2,1,3])) # 3
print(s.heightChecker([5,1,2,3,4]))   # 5
print(s.heightChecker([1,2,3,4,5]))   # 0
