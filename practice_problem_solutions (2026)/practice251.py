# Sort an array of 0s, 1s and 2s without using any sorting algorithm.

class Solution:
    def sort012(self, arr):
        from collections import Counter
        d = Counter(arr)
        
        return [i for i in range(3) for _ in range(d[i])]

s = Solution()
print(s.sort012([0, 1, 2, 0, 1, 2])) # [0, 0, 1, 1, 2, 2]
print(s.sort012([1, 0, 1, 2, 0, 1])) # [0, 0, 1, 1, 1, 2]
print(s.sort012([2, 2, 0, 1, 0, 1])) # [0, 0, 1, 1, 2, 2]