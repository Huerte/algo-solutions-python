# Problem: Unique Morse Code Words
# Source: https://leetcode.com/problems/unique-morse-code-words/

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