# Kids With the Greatest Number of Candies
# Problem: Kids With the Greatest Number of Candies
# Source: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Note: Checks whether each kid can have the greatest number of candies after receiving all extra candies.

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        return [(num + extraCandies) >= max(candies) for num in candies]
