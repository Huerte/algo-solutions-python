# Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n != 1:
            sums = 0
            temp = n
            while temp > 0:
                sums += (temp % 10) ** 2
                temp //= 10
            if sums in seen:
                return False

            seen.add(sums)
            n = sums
        
        return True

s = Solution()
print(s.isHappy(19)) # True
print(s.isHappy(2)) # False
print(s.isHappy(7)) # True