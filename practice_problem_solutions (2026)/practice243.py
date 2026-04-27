from collections import Counter
class Solution:
    def findEvenNumbers(self, digits):
        arr = []
        
        D = Counter(map(str, digits))

        for i in range(100, 999, 2):
            temp = Counter(str(i))

            if all(temp[k] <= D[k] for k in temp):
                arr.append(i)
                
        return arr
    
s = Solution()
print(s.findEvenNumbers([2,1,3,0]))   # [102,120,130,132,210,230,302,310,312,320]
print(s.findEvenNumbers([2,2,8,8,2])) # [222,228,282,288,822,828,882]
print(s.findEvenNumbers([3,7,5]))     # []