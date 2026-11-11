# Sum of Multiples
# Problem: Sum of Multiples
# Source: https://leetcode.com/problems/sum-multiples/
# Note: Calculates the sum of all numbers from 1 to n that are divisible by 3, 5, or 7.
class Solution(object):
    def sumOfMultiples(self, n):
        return sum(num for num in range(1, n + 1) if num % 3 == 0 or num % 5 == 0 or num % 7 == 0)
    
s = Solution()
print(s.sumOfMultiples(7)) # 21
print(s.sumOfMultiples(10)) # 40
