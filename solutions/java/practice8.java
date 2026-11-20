// Problem: Maximum Product Subarray
// Source: https://leetcode.com/problems/maximum-product-subarray/
// Topic: Dynamic Programming, Arrays
// Status: IN PROGRESS

class Solution {
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int maxProd = nums[0];
        int minProd = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];

            maxProd = Math.max(num, Math.max(maxProd * num, minProd * num));
            minProd = Math.min(num, Math.min(maxProd * num, minProd * num));

            result = Math.max(result, maxProd);
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        if (sol.maxProduct(new int[]{2, 3, -2, 4}) != 6) {
            throw new AssertionError("Test 1 failed");
        }
        if (sol.maxProduct(new int[]{-2, 0, -1}) != 0) {
            throw new AssertionError("Test 2 failed");
        }
        if (sol.maxProduct(new int[]{-2, 3, -4}) != 24) {
            throw new AssertionError("Test 3 failed");
        }
    }
}

