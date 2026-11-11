# Geeksforgeeks - Sort 0s, 1s and 2s
# Problem: Sort 0s, 1s and 2s
# Source: https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
# Note: Sorts an array containing only 0s, 1s, and 2s in ascending order by counting their occurrences.
class Solution:
    def sort012(self, arr):
        arr[:] = [0] * arr.count(0) + [1] * arr.count(1) + [2] * arr.count(2)
        return arr

s = Solution()
print(s.sort012([0, 1, 2, 0, 1, 2])) # [0, 0, 1, 1, 2, 2]
print(s.sort012([2, 1, 0, 2, 1, 0])) # [0, 0, 1, 1, 2, 2]
print(s.sort012([0, 0, 1, 1, 2, 2])) # [0, 0, 1, 1, 2, 2]
