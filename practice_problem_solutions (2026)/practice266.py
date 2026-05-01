# Geeksforgeeks - Rotate Array

class Solution:
    def rotateArr(self, arr, d):
        n = d % len(arr)
        arr[:] = arr[n:] + arr[:n]
        return arr
    
s = Solution()
print(s.rotateArr([1, 2, 3, 4, 5], 2)) # [3, 4, 5, 1, 2]
print(s.rotateArr([1, 2, 3, 4, 5], 3)) # [4, 5, 1, 2, 3]
print(s.rotateArr([1, 2, 3, 4, 5], 7)) # [3, 4, 5, 1, 2]