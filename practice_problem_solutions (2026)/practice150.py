# Find Common Characters

# My solution
from collections import Counter
class Solution(object):
    def commonChars(self, words):
        
        temp = []
        for word in words:
            temp.append(Counter(word))
        
        res = []
        for c in words[0]:
            if c in res:
                continue
            mins = min(word[c] for word in temp)
            res.extend([c] * mins)
        return res

# Elegant Solution
class Solution(object):
    def commonChars(self, words):
        count = Counter(words[0])
        for word in words[1:]:
            count &= Counter(word)
        return list(count.elements())

# Easy to understand Solution
class Solution(object):
    def commonChars(self, words):
        result = list(words[0])
        
        for word in words[1:]:
            temp = []
            for ch in result:
                if ch in word:
                    temp.append(ch)
                    word = word.replace(ch, "", 1)
            result = temp
        
        return result

s = Solution()
print(s.commonChars(["bella","label","roller"])) # ["e","l","l"]
print(s.commonChars(["cool","lock","cook"]))     # ["c","o"]
print(s.commonChars(["abc","bcd","cde"]))        # ["c"]