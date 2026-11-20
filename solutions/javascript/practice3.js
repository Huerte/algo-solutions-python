// Problem: Two Sum
// Source: https://leetcode.com/problems/two-sum/
// Topic: Hash Table, Arrays

function twoSum(nums, target) {
  const seen = new Map();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (seen.has(complement)) {
      return [seen.get(complement), i];
    }
    seen.set(nums[i], i);
  }

  return [];
}

const res1 = twoSum([2, 7, 11, 15], 9);
console.assert(res1[0] === 0 && res1[1] === 1, "Test 1 failed");

const res2 = twoSum([3, 2, 4], 6);
console.assert(res2[0] === 1 && res2[1] === 2, "Test 2 failed");

const res3 = twoSum([3, 3], 6);
console.assert(res3[0] === 0 && res3[1] === 1, "Test 3 failed");

console.log("All Two Sum JS test cases passed!");

