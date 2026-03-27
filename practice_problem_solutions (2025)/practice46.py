class Solution(object):
    def isValid(self, s):
        
        parenthesis = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        seen = []

        for par in s:
            if par in parenthesis:

                if seen and seen[-1] == parenthesis[par]:
                    seen.pop()
                else:
                    seen.append(par)
            
            else:
                seen.append(par)
                
        return not seen

s = Solution()
print(s.isValid("({{{{}}}))"))