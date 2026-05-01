# Geeksforgeeks - Sort 0s, 1s and 2s

class Solution:
    def sort012(self, arr):
        arr[:] = [0] * arr.count(0) + [1] * arr.count(1) + [2] * arr.count(2)
        return arr

s = Solution()
print(s.sort012([0, 1, 2, 0, 1, 2])) # [0, 0, 1, 1, 2, 2]
print(s.sort012([2, 1, 0, 2, 1, 0])) # [0, 0, 1, 1, 2, 2]
print(s.sort012([0, 0, 1, 1, 2, 2])) # [0, 0, 1, 1, 2, 2]