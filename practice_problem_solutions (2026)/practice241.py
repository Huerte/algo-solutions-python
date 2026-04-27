# Counting Words With a Given Prefix

class Solution:
    def prefixCount(self, words, pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count

s = Solution()
print(s.prefixCount(["leetcode","win","loops","success"], 'code'))  # 0
print(s.prefixCount(["pay","attention","practice","attend"], 'at')) # 2