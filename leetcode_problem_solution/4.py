class Solution(object):
    def maxProfit(self, prices):
        minimum_price = min(prices)

        for i, price in enumerate(prices):
            if price == minimum_price:
                return max(prices[i:])

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
