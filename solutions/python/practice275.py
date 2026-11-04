# Uncommon Words from Two Sentences
# Problem: Uncommon Words from Two Sentences
# Source: https://leetcode.com/problems/uncommon-words-from-two-sentences/
# Note: Combines both sentences, counts each word using Counter, and returns words that appear exactly once across both sentences.
from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        arr = []
        c = Counter((s1 + " " + s2).split())
        for key, val in c.items():
            if val == 1:
                arr.append(key)
        return arr

s = Solution()
print(s.uncommonFromSentences("this apple is sweet", "this apple is sour")) # ["sweet","sour"]
print(s.uncommonFromSentences("apple apple", "banana"))                     # ["banana"]
