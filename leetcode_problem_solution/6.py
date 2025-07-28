class Solution(object):
    def reverseStr(self, s, k):
        return s[k::-1] + s[k+1:]


sol = Solution()
print(sol.reverseStr("abcdefg", 2))