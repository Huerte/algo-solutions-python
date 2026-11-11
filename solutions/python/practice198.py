# Find the Number of Good Pairs I
# Problem: Find the Number of Good Pairs I
# Source: https://leetcode.com/problems/find-the-number-of-good-pairs-i/
# Note: Counts pairs where an element in nums1 is divisible by the corresponding element in nums2 multiplied by k.
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1
        return count

s = Solution()
print(s.numberOfPairs([1,2,3,4], [1,2,3,4], 1))  # 8
print(s.numberOfPairs([1,2,3,4], [1,2,3,4], 2))  # 3
print(s.numberOfPairs([1,2,3,4], [1,2,3,4], 3))  # 1
