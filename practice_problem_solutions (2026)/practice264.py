# Geeksforgeeks - Print n to 1 without loop

class Solution:
    def printNos(self, n):
        return ' '.join(map(str,range(n,0,-1)))

# Accepted Sol; Not mine
class Solution:
    def printNos(self, n):
        if n == 0:
            return
        print(n, end=" ")
        self.printNos(n-1)

s = Solution()
print(s.printNos(10)) # 10 9 8 7 6 5 4 3 2 1
print(s.printNos(5))  # 5 4 3 2 1
print(s.printNos(2))  # 2 1