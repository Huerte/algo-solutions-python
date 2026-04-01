# Shuffle String

class Solution(object):
    def restoreString(self, s, indices):
        arr = [""] * len(s)
        for i, num in enumerate(indices):
            arr[num] = s[i]
        return "".join(arr)

s = Solution()
print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3])) # "leetcode"
