# Find Indices of Stable Mountains

class Solution(object):
    def stableMountains(self, height, threshold):
        
        stables = []
        n = len(height)
        for i in range(1, n):
            if height[i - 1] > threshold and height[i] > 0:
                stables.append(i)
        return stables

s = Solution()
print(s.stableMountains([1,2,3,4,5], 2)) # [3, 4]