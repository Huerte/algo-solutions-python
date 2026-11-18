/**
 * Problem: Maximum Subarry
 * Source: https://leetcode.com/problems/maximum-subarray/
 * Note: simply solution in C. Probably not the fastest though.
 */

int maxSubArray(int *nums, int numsSize){
	int max = nums[0];
	int current = nums[0];
	for (int i = 1; i < numsSize; i++) {
		if(nums[i] > current + nums[i]) {
			current = nums[i];
		} else {
			current += nums[i];
		}

		if(current > max) {
			max = current;
		}
	}

	return max;
}