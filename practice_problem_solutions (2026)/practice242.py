# Minimum Sum of Four Digit Number After Splitting Digits

class Solution:
    def minimumSum(self, num: int) -> int:
        temp = sorted(str(num))
        n1, n2 = f"{temp[0]}{temp[3]}", f"{temp[1]}{temp[2]}"
        return int(n1) + int(n2)

s = Solution()
print(s.minimumSum(2932)) # 52
print(s.minimumSum(4009)) # 13
print(s.minimumSum(2687)) # 95