# Self Dividing Numbers

class Solution(object):
    def selfDividingNumbers(self, left, right):
        arr = []
        for i in range(left, right + 1):
            digits = list(map(int, list(str(i))))
            score = len(digits)
            for d in digits:
                if d == 0:
                    break
                if i % d == 0:
                    score -= 1
            if score == 0:
                arr.append(i)
        return arr
    
s = Solution()
print(s.selfDividingNumbers(1, 22))  # [1,2,3,4,5,6,7,8,9,11,12,15,22]
print(s.selfDividingNumbers(47, 85)) # [48,55,66,77]