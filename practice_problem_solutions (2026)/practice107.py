# GCD of Sums of Odd and Even Integers

# Brut Force Solution
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        odd = []
        even = []
        i = 1
        while len(odd) < n:
            odd.append(i)
            i += 2
        i = 0
        while len(even) < n:
            even.append(i)
            i += 2
        
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        return gcd(sum(even), sum(odd))

# Mathematical Solution
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        return gcd(n * n, n * (n + 1))
    

s = Solution()
print(s.gcdOfOddEvenSums(5)) # 5
print(s.gcdOfOddEvenSums(6)) # 3