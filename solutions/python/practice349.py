# Geeksforgeeks - Print n to 1 without loop
# Problem: Print n to 1 without loop
# Source: https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1
# Note: Prints numbers from n down to 1 without using loops, using recursion.
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
