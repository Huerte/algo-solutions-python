# Two Sum Variant
# Problem: Two Sum
# Source: https://leetcode.com/problems/two-sum/
# Note: Finds two indices whose corresponding elements add up to the target using a hash map for efficient lookup.
# Simple Solution 0(n2)
def sums(arr, targ):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == targ:
                return [i, j]
    return -1


# Accepted solution
def sums(arr, targ):
    seen = {}

    for i in range(len(arr)):
        need = targ - arr[i]
        if need in seen:
            return seen[need], i
        seen[arr[i]] = i
        
    return -1

print(sums([1,2,3,4], 7))
print(sums([1,2,3], 7))
