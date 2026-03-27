# Kids With the Greatest Number of Candies

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        return [(num + extraCandies) >= max(candies) for num in candies]