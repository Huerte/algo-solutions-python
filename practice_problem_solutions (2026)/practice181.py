# GeeksForGeeks - Array Search

class Solution:
    def search(self, arr, x):
        return arr.index(x) if x in arr else -1

s = Solution()
print(s.search([1,2,3,5,6], 3)) # 2