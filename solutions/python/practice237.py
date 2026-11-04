# Clear Digits
# Problem: Clear Digits
# Source: https://leetcode.com/problems/clear-digits/
# Note: Uses a stack to remove each digit and the closest remaining letter to its left.
class Solution(object):
    def clearDigits(self, s):

        seen = []
        for letter in s:
            if not seen and letter.isalpha():
                seen.append(letter)
            elif letter.isalpha():
                seen.append(letter)
            else:
                if seen:
                    seen.pop()
                
        return ''.join(seen)

s = Solution()
print(s.clearDigits("abc")) # "abc"
print(s.clearDigits("cb34")) # ""
print(s.clearDigits("1234")) # ""
