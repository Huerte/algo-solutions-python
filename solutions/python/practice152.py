# Problem: Decode the Message
# Source: https://leetcode.com/problems/decode-the-message/
# Note: Decodes a message using a substitution mapping based on the first occurrence of characters in the key.

class Solution(object):
    def decodeMessage(self, key, message):
        
        coord = {}
        alpha = 0
        for c in key.replace(' ', ''):
            if not coord:
                coord[c] = chr(97 + alpha)
                alpha += 1
            elif c not in coord:
                coord[c] = chr(97 + alpha)
                alpha += 1
        
        res = ""
        for c in message:
            if c == ' ':
                res += ' '
            else:
                res += coord[c]
        return res

s = Solution()
print(s.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
