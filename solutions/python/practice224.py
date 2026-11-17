# Problem: 4Sum
# Source: https://leetcode.com/problems/4sum/
# Note: Sort, fix two values, then find the remaining pair with two pointers.
# Status: ✅ Done


class Solution(object):
    def fourSum(self, nums, target):
        nums = sorted(nums)
        result = []
        size = len(nums)
        for first in range(size - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, size - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                left, right = second + 1, size - 1
                while left < right:
                    total = nums[first] + nums[second] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[first], nums[second], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.fourSum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1],
    ]
    assert solution.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    assert solution.fourSum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]]
