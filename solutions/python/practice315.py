# Count and Say
# Problem: Count and Say
# Source: https://leetcode.com/problems/count-and-say/
# Note: Generates the nth sequence term by counting consecutive repeated digits in the previous term.
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        res = ""
        c = 1

        for i in range(len(prev)):
            if i + 1 < len(prev) and prev[i] == prev[i + 1]:
                c += 1
            else:
                res += str(c) + prev[i]
                c = 1
        
        return res
    
s = Solution()
print(s.countAndSay(1)) # "1"
print(s.countAndSay(4)) # "1211"
