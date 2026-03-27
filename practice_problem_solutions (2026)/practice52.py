# Maximum Substrings With Distinct Start
class Solution(object):
    def maxDistinct(self, s):
        l=len(s)
        if len(set(s)) == l:
            return l

        arr = [s]
        for i in range(1, l):
            arr.append(s[i:])
        
        return len(set([a[0] for a in arr]))
    
s = Solution()
temp = "abab"
print(s.maxDistinct(temp))