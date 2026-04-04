# Truncate Sentence

class Solution(object):
    def truncateSentence(self, s, k):
        return " ".join(s.split()[:k])