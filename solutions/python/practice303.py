# Minimum Average of Smallest and Largest Elements
# Problem: Minimum Average of Smallest and Largest Elements
# Source: https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
# Note: Pairs the smallest and largest elements, calculates their averages, and returns the minimum average.
class Solution(object):
    def minimumAverage(self, nums):
        arr = []
        nums.sort()
        for i in range(len(nums) // 2):
            av = (nums[i] + nums[len(nums) - i - 1] ) / 2
            arr.append(av)

        return min(arr)

s = Solution()   
print(s.minimumAverage([7,8,3,4,15,13,4,1])) # 5.5
print(s.minimumAverage([1,9,8,3,10,5]))      # 5.5
print(s.minimumAverage([1,2,3,7,8,9]))       # 5.0
