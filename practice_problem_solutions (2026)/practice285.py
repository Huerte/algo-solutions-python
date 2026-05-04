class Solution:
    def twoSum(self, arr, target):
        arr.sort()
        left = 0
        right = len(arr) - 1
        
        while left < right:
            res = arr[left] + arr[right]
            if res == target:
                return True
            
            if res > target:
                right -= 1
            else:
                left += 1
        
        return False

s = Solution()
print(s.twoSum([1, 2, 3, 4, 5], 9))  # True
print(s.twoSum([1, 2, 3, 4, 5], 10)) # False
print(s.twoSum([1, 2, 3, 4, 5], 5))  # True