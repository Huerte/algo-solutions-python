# Minimum Distance to the Target Element

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