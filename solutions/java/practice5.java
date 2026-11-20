// Problem: Binary Search
// Source: https://leetcode.com/problems/binary-search/
// Topic: Binary Search, Arrays
// Status: IN PROGRESS

class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        if (sol.search(new int[]{-1, 0, 3, 5, 9, 12}, 9) != 4) {
            throw new AssertionError("Test 1 failed");
        }
        if (sol.search(new int[]{-1, 0, 3, 5, 9, 12}, 2) != -1) {
            throw new AssertionError("Test 2 failed");
        }
        if (sol.search(new int[]{5}, 5) != 0) {
            throw new AssertionError("Test 3 failed");
        }
    }
}

