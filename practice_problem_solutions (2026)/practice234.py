# Find Numbers with Even Number of Digits

from math import log10, ceil
class Solution:
    def findNumbers(self, nums) -> int:
        return sum([1 for num in nums if ceil(log10(num + 1)) % 2 == 0])
    
s = Solution()
print(s.findNumbers([12,345,2,6,7896]))  # 2
print(s.findNumbers([555,901,482,1771])) # 1