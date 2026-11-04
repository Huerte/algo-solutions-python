# XOR Operation in an Array
# Problem: XOR Operation in an Array
# Source: https://leetcode.com/problems/xor-operation-in-an-array/
# Note: Creates an array using start + 2 * i and returns the XOR of all its elements.

class Solution(object):
    def xorOperation(self, n, start):
        arr = []
        i = 0
        while len(arr) < n:
            arr.append(start + 2 * i)
            i += 1
        xor = arr[0]
        for i in arr[1:]:
            xor ^= i
        return xor

s = Solution()
print(s.xorOperation(5, 0)) # 8
print(s.xorOperation(4, 3)) # 8
