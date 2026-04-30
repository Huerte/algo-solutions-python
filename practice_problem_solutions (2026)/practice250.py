# Jump Game II

class Solution:
    def jumps(self, arr):
        jump = 0
        
        l, r = 0, 0
        
        while r < len(arr) - 1:
            farthest = 0
            
            for i in range(l, r + 1):
                farthest = max(farthest, i + arr[i])
            
            l = r
            r = farthest
            
            jump += 1
        
        return jump

s = Solution()
print(s.jumps([2, 3, 1, 1, 4])) # 2
print(s.jumps([2, 3, 0, 1, 4])) # 2
print(s.jumps([0])) # 0