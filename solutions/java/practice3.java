// Problem: Best Time to Buy and Sell Stock
// Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Note: Track the minimum price seen so far and update maximum profit in a single pass

class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0) {
            return 0;
        }

        int minPrice = prices[0];
        int maxProfit = 0;

        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            } else {
                int profit = prices[i] - minPrice;
                if (profit > maxProfit) {
                    maxProfit = profit;
                }
            }
        }

        return maxProfit;
    }
    public static void main(String[] args) {
        Solution solution = new Solution();

        if (solution.maxProfit(new int[]{7, 1, 5, 3, 6, 4}) != 5) {
            throw new AssertionError("Test 1 failed: expected 5");
        }
        if (solution.maxProfit(new int[]{7, 6, 4, 3, 1}) != 0) {
            throw new AssertionError("Test 2 failed: expected 0");}
        if (solution.maxProfit(new int[]{2, 4, 1}) != 2) {
            throw new AssertionError("Test 3 failed: expected 2");
        }
        System.out.println("All Best Time to Buy and Sell Stock Java test cases passed!");
    }
}

