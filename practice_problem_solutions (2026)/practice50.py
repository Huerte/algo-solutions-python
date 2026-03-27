# 3Sum Closet

def three_sum(arr, target):

    nums = {}

    for i in range(len(arr)):
        nums[arr[i]] = abs(arr[i]) - abs(target)

    res = sorted(nums, key=lambda x: nums[x])

    return sum(res[:3])

print(three_sum([-1, 2, 1, -4], 1))
print(three_sum([0, 0, 0], 1))