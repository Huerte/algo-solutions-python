# GeeksForGeeks - Array Search
# Problem: Array Search
# Source: https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1
# Note: Uses Python's inbuilt index() method to return the first occurrence of the target element, or -1 if it is not found.
class Solution:
    def search(self, arr, x):
        return arr.index(x) if x in arr else -1

s = Solution()
print(s.search([1,2,3,5,6], 3)) # 2
