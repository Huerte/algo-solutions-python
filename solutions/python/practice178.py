# Water Bottles
# Problem: Water Bottles
# Source: https://leetcode.com/problems/water-bottles/
# Note: Calculates the maximum number of water bottles that can be consumed through repeated exchanges of empty bottles.
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        res = 0
        empty = 0
        
        while numBottles > 0:
            res += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange

        return res

    
s = Solution()
print(s.numWaterBottles(9, 3))  # 13
print(s.numWaterBottles(15, 4)) # 19
