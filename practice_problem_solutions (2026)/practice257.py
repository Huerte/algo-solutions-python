# Generate Parentheses

class Solution(object):
    def generateParenthesis(self, n):
        
        stack = []
        res = []

        def backtrack(open, close):
            if open == close == n:
                res.append("".join(stack))
                return 
            
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0, 0)
        return res
    
s = Solution()
print(s.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(s.generateParenthesis(2)) # ["(())","()()"]
print(s.generateParenthesis(1)) # ["()"]