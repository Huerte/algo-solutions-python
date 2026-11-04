# Problem: Maximum Substrings With Distinct Start
# Source: https://leetcode.com/problems/maximum-substrings-with-distinct-start/
# Note: Finds the maximum number of substrings with distinct starting characters.
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
