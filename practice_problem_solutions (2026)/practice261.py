# Geeksforgeeks - Count Even Letters

from collections import Counter
class Solution:
    def count(self, s):
        alp = Counter(s)
        return sum(1 for k in alp.values() if k % 2 == 0)

s = Solution()
print(s.count("abcde")) # 0
print(s.count("aabbcde")) # 2
print(s.count("aabbccde")) # 3