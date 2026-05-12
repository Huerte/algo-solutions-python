# Combination Sum

class Solution(object):
    def combinationSum(self, candidates, target):

        res = []

        sol = []

        def backt(i):

            print(sol[:], i)
            if sum(sol) == target:
                res.append(sol[:])
                return
            if i == len(candidates) or sum(sol) > target:
                return

            backt(i+1)

            sol.append(candidates[i])
            backt(i)
            sol.pop()
        
        backt(0)
        return res

s = Solution()
print(s.combinationSum([2,3,5], 8))    # [[2,2,2,2],[2,3,3],[3,5]]
print(s.combinationSum([2,3,6,7], 7))  # [[2,2,3],[7]]
print(s.combinationSum([2], 1))        # []