// Problem: Valid Anagram
// Source: https://leetcode.com/problems/valid-anagram/
// Topic: String, Hash Table

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        for (int c : count) {
            if (c != 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        if (!sol.isAnagram("anagram", "nagaram")) {
            throw new AssertionError("Test 1 failed");
        }
        if (sol.isAnagram("rat", "car")) {
            throw new AssertionError("Test 2 failed");
        }
        if (!sol.isAnagram("a", "a")) {
            throw new AssertionError("Test 3 failed");
        }

        System.out.println("All Valid Anagram Java test cases passed!");
    }
}

