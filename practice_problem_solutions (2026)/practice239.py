# Maximum 69 Number

class Solution:
    def maximum69Number (self, num: int) -> int:
        cur = list(str(num))
        maxs = num
        for i in range(len(cur)):
            if cur[i] == '6':
                cur[i] = '9'
                maxs = max(maxs, int(''.join(cur)))
                cur[i] = '6'
        return maxs

s = Solution()
print(s.maximum69Number(9999)) # 9999
print(s.maximum69Number(9996)) # 9999
print(s.maximum69Number(9669)) # 9969