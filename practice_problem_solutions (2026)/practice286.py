# Geeksforgeeks - Maximum Product Subarray

# My Sol;
from math import prod
class Solution:
    def maxProduct(self, arr):
        maxN = float('-inf')
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                maxN = max(maxN, prod(arr[i:j+1]))

        return maxN

# Accepted Sol;
class Solution:
    def maxProduct(self, arr):
        max_prod = min_prod = ans = arr[0]

        for x in arr[1:]:
            if x < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(x, max_prod * x)
            min_prod = min(x, min_prod * x)

            ans = max(ans, max_prod)

        return ans
    
s = Solution()
print(s.maxProduct([10, 9, 1, 9, 8, -5, 0]))   # 6480
print(s.maxProduct([1, 2, -8, -4, 8, -3, -1])) # 1536
print(s.maxProduct([1, 2, 3, 4, 5]))           # 120
print(s.maxProduct([-1, 2]))                   # 2