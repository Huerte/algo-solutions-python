# Minimum Distance to the Target Element
# Problem: Minimum Distance to the Target Element
# Source: https://leetcode.com/problems/minimum-distance-to-the-target-element/
# Note: Finds the minimum absolute distance between start and an index containing target.
class Solution(object):
    def getMinDistance(self, nums, target, start):
        closest = float('inf')
        for i in range(start, len(nums)):
            if nums[i] == target:
                closest = min(closest, abs(start - i))
        
        for i in range(start, -1, -1):
            if nums[i] == target:
                closest = min(closest, abs(start - i))
        
        return closest
