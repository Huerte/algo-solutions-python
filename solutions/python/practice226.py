# Convert an Array Into a 2D Array With Conditions
# Problem: Convert an Array Into a 2D Array With Conditions
# Source: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
# Note: Distributes array elements into rows while ensuring each row contains distinct integers and the total number of rows is minimized.
class Solution(object):
    def findMatrix(self, nums):
        res = []

        while nums:
            cur = []
            for num in nums:
                if cur and num in cur:
                    continue
                cur.append(num)
            res.append(cur)
            for val in cur:
                nums.remove(val)
        return res
    
s = Solution()
print(s.findMatrix([1, 3, 4, 1, 2, 3, 1])) # [[1, 3, 4, 2], [1, 3], [1]]
print(s.findMatrix([1, 1, 1, 1, 1])) # [[1], [1], [1], [1], [1]]
print(s.findMatrix([1, 2, 3, 4])) # [[1, 2, 3, 4]]
