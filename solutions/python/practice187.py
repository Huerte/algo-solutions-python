# Count the Digits That Divide a Number
# Problem: Count the Digits That Divide a Number
# Source: https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Note: Counts how many digits of a number divide the original number without a remainder.
class Solution(object):
    def countDigits(self, num):
        count = 0
        n = num

        while n > 0:
            temp = n % 10
            if num % temp == 0:
                count += 1
            n //= 10
        return count

s = Solution()
print(s.countDigits(7)) # 1
print(s.countDigits(121)) # 2
print(s.countDigits(1248)) # 4
