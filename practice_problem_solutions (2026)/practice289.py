# Geeksforgeeks - Rotate Array by One

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