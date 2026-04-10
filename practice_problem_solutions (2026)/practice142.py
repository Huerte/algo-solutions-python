# Relative Ranks

class Solution(object):
    def findRelativeRanks(self, score):
        s = sorted(score)
        res = []
        winners = s[-3:][::-1]
        not_ranked = []
        for num in score:
            if num in winners:
                res.append(["Gold Medal","Silver Medal","Bronze Medal"][winners.index(num)])
            else:
                res.append('')
                not_ranked.append((num, len(res) - 1))

        cur_ranked = 4
        for _, i in sorted(not_ranked, key=lambda x: x[0], reverse=True):
            res[i] = str(cur_ranked)
            cur_ranked += 1

        return res
    
s = Solution()
print(s.findRelativeRanks([5, 4, 3, 2, 1])) # ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
print(s.findRelativeRanks([10, 3, 8, 9, 4])) # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
print(s.findRelativeRanks([1, 2, 3, 4, 5])) # ["5","4","Bronze Medal","Silver Medal","Gold Medal"]