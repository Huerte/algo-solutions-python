# Merge Intervals

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        res = []

        temp = []
        for l, r in intervals:
            if not temp:
                temp = [l, r]
            elif l > temp[1]:
                res.append(temp)
                temp = [l, r]
            elif r > temp[1]:
                temp[1] = r
        
        if temp:
            res.append(temp)
        
        return res

s = Solution()
print(s.merge([[1,3],[2,7],[8,10],[15,18],[17,23],[3,4],[4,5],[10,14],[11,12],[13,14]])) # [[1,7],[8,14],[15,23]]
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))                                             # [[1,6],[8,10],[15,18]]
print(s.merge([[1,4],[4,5]]))                                                            # [[1,5]]
