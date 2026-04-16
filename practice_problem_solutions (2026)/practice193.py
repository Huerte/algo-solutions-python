# Check if the Sentence Is Pangram

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