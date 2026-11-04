# Check if the Sentence Is Pangram
# Problem: Check if the Sentence Is Pangram
# Source: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# Note: Checks whether every letter from a to z appears at least once in the given sentence.
class Solution(object):
    def checkIfPangram(self, sentence):
        alp = [chr(i) for i in range(97, 123)]
        for c in alp:
            if c not in sentence:
                return False
        return True

s = Solution()
print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")) # True
print(s.checkIfPangram("leetcode"))                            # False
