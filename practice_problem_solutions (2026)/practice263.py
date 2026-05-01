# Geeksfor Geeks - Bits Counting

from typing import List

class Solution:
    def countBits(self, n : int) -> List[int]:
        arr = []
        
        for i in range(n + 1):
            arr.append(bin(i)[2:].count('1'))
        
        return arr
        
s = Solution()
print(s.countBits(10)) # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
print(s.countBits(5))  # [0, 1, 1, 2, 1, 2]
print(s.countBits(2))  # [0, 1, 1]