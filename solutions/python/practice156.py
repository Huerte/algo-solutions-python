# Split a String in Balanced Strings
# Problem: Split a String in Balanced Strings
# Source: https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Note: Finds the maximum number of balanced substrings with equal numbers of L and R.

class Solution(object):
    def balancedStringSplit(self, s):
        
        count = 0

        r_count = 0
        l_count = 0

        for c in s:
            if c == 'R':
                r_count += 1
            elif c == 'L':
                l_count += 1
            
            if r_count == l_count:
                count += 1
                r_count = 0
                l_count = 0
        return count

s = Solution()
print(s.balancedStringSplit("RLRRLLRLRL"))
