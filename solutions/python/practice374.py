# Geeksforgeeks - Rotate Array by One
# Problem: Rotate Array by One
# Source: https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1
# Note: Cyclically rotates an array one position clockwise, moving the last element to the front.
class Solution:
    def rotate(self, arr):
        if not arr:
            return arr
            
        d = 1 % len(arr)
        arr[:] = arr[-d:] + arr[:-d]
        return arr
    
s = Solution()
print(s.rotate([1, 2, 3, 4, 5, 6, 7])) # [7, 1, 2, 3, 4, 5, 6]
print(s.rotate([1, 2, 3, 4, 5, 6]))    # [6, 1, 2, 3, 4, 5]
print(s.rotate([1, 2, 3, 4, 5]))       # [5, 1, 2, 3, 4]
