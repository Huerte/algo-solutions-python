# Geeksforgeeks -Square Root
# Problem: Square Root
# Source: https://www.geeksforgeeks.org/problems/square-root/1
# Note: Returns the floor value of the square root of a given positive integer.
class Solution:
    def floorSqrt(self, n): 
        from math import floor
        num = n ** 0.5
        if num == int(num):
            return int(num)
        return floor(num)

s = Solution()
print(s.floorSqrt(4))  # 2
print(s.floorSqrt(11)) # 3
print(s.floorSqrt(25)) # 5
