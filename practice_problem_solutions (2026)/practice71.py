# Unique Morse Code Words

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        for word in words:
            temp = ""
            for c in word:
                temp += morse[ord(c.lower()) - 97]
            res.append(temp)
        print(res)
        return len(set(res))

s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
print(s.uniqueMorseRepresentations(["a"]))