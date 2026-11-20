# Problem: Word Pattern
# Source: https://leetcode.com/problems/word-pattern/
# Note: Hash map from letter to word, rejecting a word already claimed by another letter, then rebuild the string from the pattern and compare
# Complexity: O(n) time, O(n) space

class Solution(object):
    def wordPattern(self, pattern, s):
        mapped = {}
        words = s.split() if ' ' in s else list(s)
        for i, l in enumerate(pattern):
            if mapped:
                if l in mapped and mapped[l] != words[i]:
                    return False
                
                elif l not in mapped and words[i] in mapped.values():
                    return False
                
            mapped[l] = words[i]

        result = []
        for ltr in pattern:
            result.append(mapped[ltr])
        
        return ' '.join(result) == s

s = Solution()
# print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("jquery","jquery"))