# Problem: Container With Most Water
# Source: https://leetcode.com/problems/container-with-most-water/
# Note: Two pointer attempt that mistakenly shifts the taller boundary inwards, discarding maximum potential area.
# Status: In Progress (Logic Error)


class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            if current_area > max_water:
                max_water = current_area

            if height[left] > height[right]:
                left += 1
            else:
                right -= 1

        return max_water


if __name__ == "__main__":
    solution = Solution()
    result = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print("Result:", result)
    assert result == 49, f"Expected 49, got {result}"
