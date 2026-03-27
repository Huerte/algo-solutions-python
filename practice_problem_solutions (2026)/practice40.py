# Two Sum

def twoSum(arr, target):

    seen = {}

    for i in range(len(arr)):
        if not seen:
            seen[arr[i]] = i
            continue

        to_find = target - arr[i]
        if to_find in seen:
            return [seen[to_find], i]
        else:
            seen[arr[i]] = i

    return []


print(twoSum([1, 2, 3, 5], 7))