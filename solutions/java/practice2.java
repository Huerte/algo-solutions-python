// Problem: Two Sum
// Source: https://leetcode.com/problems/two-sum/
// Note: Use a hash map to store seen values and find complements in one pass

import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[] {seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }

        return new int[0];
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] res1 = solution.twoSum(new int[]{2, 7, 11, 15}, 9);
        if (!Arrays.equals(res1, new int[]{0, 1})) {
            throw new AssertionError("Test 1 failed");
        }

        int[] res2 = solution.twoSum(new int[]{3, 2, 4}, 6);
        if (!Arrays.equals(res2, new int[]{1, 2})) {
            throw new AssertionError("Test 2 failed");
        }
        int[] res3 = solution.twoSum(new int[]{3, 3}, 6);
        if (!Arrays.equals(res3, new int[]{0, 1})) {
            throw new AssertionError("Test 3 failed");
        }
        System.out.println("All Two Sum Java test cases passed!");
    }
}

