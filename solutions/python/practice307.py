# Find Missing Elements
# Problem: Find Missing Elements
# Source: https://leetcode.com/problems/find-missing-elements/
# Note: Finds all missing integers between the minimum and maximum values in the array.
class Solution:
    def findMissingElements(self, nums):
        complete = list(range(min(nums), max(nums) + 1))
        arr = []
        for num in complete:
            if num not in nums:
                arr.append(num)
        return arr

s = Solution()
print(s.findMissingElements([1,4,2,5])) # [3]
print(s.findMissingElements([5,1]))     # [2,3,4]
