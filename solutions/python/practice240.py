# Decode XORed Array
# Problem: Decode XORed Array
# Source: https://leetcode.com/problems/decode-xored-array/
# Note: Reconstructs the original array by XORing each encoded element with the previously decoded element.
class Solution(object):
    def decode(self, encoded, first):
        decoded = [first]
        for i in range(len(encoded)):
            decoded.append(encoded[i] ^ decoded[-1])
        return decoded

s = Solution()
print(s.decode([1,2,3], 1))   # [1,0,2,1]
print(s.decode([6,2,7,3], 4)) # [4,2,0,7,4]
