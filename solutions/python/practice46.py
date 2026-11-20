# Problem: Unique Morse Code Words
# Source: https://leetcode.com/problems/unique-morse-code-words/
# Note: Translate each word to Morse and count distinct codes with a set. Unfinished: ord(ltr) - 64 should be ord(ltr) - 97 (IndexError on lowercase input), and it returns len(result) - len(set(result)) instead of len(set(result))
# Complexity: O(total letters) time and space

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        result = []
        for word in words:
            temp = ""
            for ltr in word.lower():
                temp += morse[ord(ltr) - 64]
            result.append(temp)
        return len(result) - len(set(result))

print(ord('a'))