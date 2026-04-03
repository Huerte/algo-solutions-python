# Remove Outermost Parentheses

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