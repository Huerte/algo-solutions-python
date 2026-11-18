// Problem: Two Sum
// Source: https://leetcode.com/problems/two-sum/
// Note: Use a Map to store seen values and find complements in one pass

function twoSum(nums: number[], target: number): number[] {
  const seen = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    const complementIndex = seen.get(complement);

    if (complementIndex !== undefined) {
      return [complementIndex, i];
    }

    seen.set(nums[i], i);
  }

  return [];
}

const testCases: Array<{ nums: number[]; target: number; expected: number[] }> = [
  { nums: [2, 7, 11, 15], target: 9, expected: [0, 1] },
  { nums: [3, 2, 4], target: 6, expected: [1, 2] },
  { nums: [3, 3], target: 6, expected: [0, 1] },
];

for (const { nums, target, expected } of testCases) {
  const result = twoSum(nums, target);
  if (result.length !== expected.length || result[0] !== expected[0] || result[1] !== expected[1]) {
    throw new Error(`Failed for nums: ${nums}, target: ${target}`);
  }
}

console.log(`All ${testCases.length} Two Sum TypeScript test cases passed!`);
