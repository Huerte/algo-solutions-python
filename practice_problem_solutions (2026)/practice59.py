# Generate All Subsets

class Solution(object):
    def subsets(self, nums):
        res = [[]]

        for i in range(len(nums)):
            temp = []
            for subset in res:
                temp.append(subset + [nums[i]])
            res.extend(temp)

        return res

s = Solution()
print(s.subsets([1, 2, 3]))