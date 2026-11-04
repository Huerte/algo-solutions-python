# Decompress Run-Length Encoded List
# Problem: Decompress Run-Length Encoded List
# Source: https://leetcode.com/problems/decompress-run-length-encoded-list/
# Note: Decompresses a list by repeating each value according to its corresponding frequency in adjacent pairs.
class Solution(object):
    def decompressRLElist(self, nums):
        arr = []

        for i in range(0, len(nums) - 1, 2):
            arr.extend([nums[i + 1]] * nums[i])
        
        return arr
    
s = Solution()
print(s.decompressRLElist([1,2,3,4])) # [2,4,4,4]
print(s.decompressRLElist([1,1,2,3])) # [1,3,3]
