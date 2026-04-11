# Clear Digits

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