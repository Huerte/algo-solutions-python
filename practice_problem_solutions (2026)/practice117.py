# Number of Steps to Reduce a Number to Zero

class Solution(object):
    def numberOfSteps(self, num):
        count = 0

        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1
        return count

s = Solution()
print(s.numberOfSteps(14)) # 6
print(s.numberOfSteps(8)) # 4
print(s.numberOfSteps(123)) # 12