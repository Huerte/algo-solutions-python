# Geeksforgeeks - Smallest Positive Missing
# Problem: Smallest Positive Missing
# Source: https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1
# Note: Finds the smallest positive integer missing from an array after filtering non-positive values and sorting.
class Solution:
    def missingNumber(self, arr):
        arr[:] = sorted([num for num in arr if num > 0])
        if arr:
            for i in range(1, max(arr)):
                if i not in arr:
                    return i
        return max(arr) + 1 if arr else 1

s = Solution()
print(s.missingNumber([7, 8, 9, 11, 12])) # 1
print(s.missingNumber([3, 4, -1, 1]))     # 2
print(s.missingNumber([1, 2, 0]))         # 3
print(s.missingNumber([-12, 0]))          # 1
