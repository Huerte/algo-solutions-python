// Problem: Contains Duplicate
// Source: https://leetcode.com/problems/contains-duplicate/
// Topic: Hash Table, Arrays

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (!seen.add(num)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        if (!sol.containsDuplicate(new int[]{1, 2, 3, 1})) {
            throw new AssertionError("Test 1 failed");
        }
        if (sol.containsDuplicate(new int[]{1, 2, 3, 4})) {
            throw new AssertionError("Test 2 failed");
        }
        if (!sol.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2})) {
            throw new AssertionError("Test 3 failed");
        }

        System.out.println("All Contains Duplicate Java test cases passed!");
    }
}

