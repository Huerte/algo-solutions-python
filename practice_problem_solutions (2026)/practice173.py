# Count of Matches in Tournament

class Solution(object):
    def numberOfMatches(self, n):
        count = 0
        while n > 1:
            if n % 2 == 0:
                count += n // 2
                n //= 2
            else:
                count += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return count
    
s = Solution()
print(s.numberOfMatches(n=7)) # 6