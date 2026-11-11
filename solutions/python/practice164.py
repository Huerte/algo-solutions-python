# Remove Outermost Parentheses
# Problem: Remove Outermost Parentheses
# Source: https://leetcode.com/problems/remove-outermost-parentheses/
# Note: Removes the outermost opening and closing parentheses from each primitive valid parentheses string.

class Solution(object):
    def removeOuterParentheses(self, s):
        
        seen = []
        ans = ""
        for c in s:
            if not seen:
                seen.append(c)
            elif c == '(':
                seen.append(c)
                ans += c
            elif c == ')':
                seen.pop()
                if seen:
                    ans += c
        
        return ans
    
s = Solution()
print(s.removeOuterParentheses("(()())(())"))           # Expected: "()()()"
print(s.removeOuterParentheses("(()())(())(()(()))"))   # Expected: "()()()()(())"
