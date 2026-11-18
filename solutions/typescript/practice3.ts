// Problem: Best Time to Buy and Sell Stock
// Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Note: Track the minimum price seen so far and update maximum profit in a single pass

function maxProfit(prices: number[]): number {
  if (prices.length === 0) {
    return 0;
  }

  let minPrice = prices[0];
  let maximumProfit = 0;

  for (let i = 1; i < prices.length; i++) {
    if (prices[i] < minPrice) {
      minPrice = prices[i];
    } else {
      const profit = prices[i] - minPrice;
      if (profit > maximumProfit) {
        maximumProfit = profit;
      }
    }
  }

  return maximumProfit;
}

const testCases: Array<{ prices: number[]; expected: number }> = [
  { prices: [7, 1, 5, 3, 6, 4], expected: 5 },
  { prices: [7, 6, 4, 3, 1], expected: 0 },
  { prices: [2, 4, 1], expected: 2 },
];

for (const { prices, expected } of testCases) {
  const result = maxProfit(prices);
  if (result !== expected) {
    throw new Error(`Failed for prices: ${prices}, expected ${expected}, got ${result}`);
  }
}

console.log(`All ${testCases.length} Best Time to Buy and Sell Stock TypeScript test cases passed!`);
