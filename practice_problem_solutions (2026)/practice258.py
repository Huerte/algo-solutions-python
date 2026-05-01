# Rank Transform of an Array

class Solution(object):
    def arrayRankTransform(self, arr):
        rank = dict(zip(sorted(set(arr)), range(1, len(set(arr))+1)))
        return [rank[x] for x in arr]

s = Solution()
print(s.arrayRankTransform([37,12,28,9,100,56,80,5,12])) # [5,3,4,2,8,6,7,1,3]
print(s.arrayRankTransform([40,10,20,30]))               # [4,1,2,3]
print(s.arrayRankTransform([100,100,100]))               # [1,1,1]