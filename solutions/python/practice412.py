# Problem: Container With Most Water
# Source: https://leetcode.com/problems/container-with-most-water/
# Note: Two pointers from both ends; always move the shorter wall inward, because moving the taller one can never give a larger area.
# Status: ✅ Done


class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            if current_area > max_water:
                max_water = current_area

            # The area is limited by the shorter wall. Moving the taller wall
            # inward only shrinks the width, so the shorter wall has to move.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


if __name__ == "__main__":
    solution = Solution()
    result = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print("Result:", result)
    assert result == 49, f"Expected 49, got {result}"
    assert solution.maxArea([1, 1]) == 1
    assert solution.maxArea([4, 3, 2, 1, 4]) == 16
    assert solution.maxArea([1, 2, 1]) == 2
    assert solution.maxArea([2, 3, 4, 5, 18, 17, 6]) == 17
