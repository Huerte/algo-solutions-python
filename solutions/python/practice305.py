# Sorting the Sentence

class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(word[:-1] for word in sorted(s.split(), key=lambda x: x[-1]))
    
s = Solution()
print(s.sortSentence("is2 sentence4 This1 a3")) # "This is a sentence"
print(s.sortSentence("Myself2 Me1 I4 and3"))    # "Me Myself and I"
