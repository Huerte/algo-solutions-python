# Weighted Word Mapping
# Problem: Weighted Word Mapping
# Source: https://leetcode.com/problems/weighted-word-mapping/
# Note: Calculates each word's total character weight, takes modulo 26, and maps it to a reverse-alphabet character.
class Solution:
    def mapWordWeights(self, words, weights) -> str:
        alp = dict(zip(range(25, -1, -1),[chr(i) for i in range(97, 123)]))

        res = ""
        for word in words:
            t = sum([weights[ord(w) - 97] for w in word]) % 26
            print(t)
            res += alp[t]

        return res

s = Solution()
print(s.mapWordWeights(["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))
