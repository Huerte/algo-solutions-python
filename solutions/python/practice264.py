# GeeksForGeeks - Indexes of Subarray Sum
# Problem: Indexes of Subarray Sum
# Source: https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
# Note: Uses nested loops to find the first continuous subarray whose sum equals the target and returns its 1-based starting and ending indices.
arr = [1, 2, 3, 7, 5]
def subarraySum(arr, target):
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                x = sum(arr[i:j+1])
                if x == target:
                    return [i+1, j+1]
                elif x > target:
                    break
        return [-1]

print(subarraySum(arr, 12))
