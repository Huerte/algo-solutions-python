# Find the Difference of Two Arrays

class Solution:
    def findDifference(self, nums1, nums2):
        return [[num for num in set(nums1) if num not in nums2], [num for num in set(nums2) if num not in nums1]]
    
s = Solution()
print(s.findDifference([1,2,3], [2,4,6])) # [[1,3], [4,6]]
print(s.findDifference([1,2,3,3], [1,1,2,2])) # [[3], []]
print(s.findDifference([1,2,3], [1,2,3])) # [[], []]