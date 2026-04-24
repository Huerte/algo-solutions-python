# Group Anagrams

class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for w in strs:
            srt = ''.join(sorted(w))
            if groups and srt in groups:
                groups[srt].append(w)
            else:
                groups[srt] = [w]
        return list(groups.values())

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for w in strs:
            srt = ''.join(sorted(w))
            groups[srt].append(w)
        return list(groups.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["eat","tea","ate"],["tan","nat"],["bat"]]
print(s.groupAnagrams(["a"]))                                 # [["a"]]
print(s.groupAnagrams([""]))                                  # [[""]]