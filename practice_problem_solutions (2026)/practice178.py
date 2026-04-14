class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        arr = [0, 0]
        for num in nums1:
            if num in nums2:
                arr[0] += 1
        
        for num in nums2:
            if num in nums1:
                arr[1] += 1

        return arr

s = Solution()
print(s.findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6])) # [3,4]
print(s.findIntersectionValues([3,4,2,3], [1,5])) # [0,0]
print(s.findIntersectionValues([2,3,2], [1,2])) # [2,1]
