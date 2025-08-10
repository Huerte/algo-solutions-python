# 📜 Problem — Jump Game
# Description:
# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
#
# Input:
# - nums: An integer array where 1 <= nums.length <= 10^4
# - 0 <= nums[i] <= 10^5
#
# Output:
# - A boolean indicating whether you can reach the last index
#
# Status: ✅ SOLVED

def canJump(nums):
    if not nums:
        return False
    
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + nums[i])
        
        if max_reach >= len(nums) - 1:
            return True
    
    return True

# Test cases with assertions
# Example 1
assert canJump([2,3,1,1,4]) == True

# Example 2
assert canJump([3,2,1,0,4]) == False

# Edge cases
assert canJump([0]) == True
assert canJump([1, 0]) == True
assert canJump([0, 1]) == False
assert canJump([2, 0, 0]) == True
assert canJump([1, 1, 1, 1]) == True

print("All test cases passed!")