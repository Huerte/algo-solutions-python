// Problem: Maximum Subarray
// Source: https://leetcode.com/problems/maximum-subarray/
// Topic: Dynamic Programming, Arrays

function maxSubArray(nums) {
  let currentSum = nums[0];
  let maxSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum;
}

console.assert(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) === 6, "Test 1 failed");
console.assert(maxSubArray([1]) === 1, "Test 2 failed");
console.assert(maxSubArray([5, 4, -1, 7, 8]) === 23, "Test 3 failed");

console.log("All Maximum Subarray JS test cases passed!");

