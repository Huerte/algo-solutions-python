# Maximum Number of Words Found in Sentences

class Solution(object):
    def mostWordsFound(self, sentences):
        cur_max = float('-inf')
        for words in sentences:
            cur_max = max(cur_max, len(words.split()))
        return cur_max

s = Solution()
print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])) # 6
print(s.mostWordsFound(["please wait", "continue to fight", "continue to win"])) # 3