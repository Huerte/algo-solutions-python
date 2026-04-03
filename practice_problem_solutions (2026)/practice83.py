# XOR Operation in an Array

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