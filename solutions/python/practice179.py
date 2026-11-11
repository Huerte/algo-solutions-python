# Truncate Sentence
# Problem: Truncate Sentence
# Source: https://leetcode.com/problems/truncate-sentence/
# Note: Returns a sentence containing only the first k words using string splitting and joining.
class Solution(object):
    def truncateSentence(self, s, k):
        return " ".join(s.split()[:k])
