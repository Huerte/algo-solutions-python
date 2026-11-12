# Problem: Find the Missing Number
# Source: https://leetcode.com/problems/missing-number/
# Note: Sorts the array, then scans neighbouring elements for the first gap; the missing number is one more than the element before the gap

n = int(input('Enter the number of elements: '))
print(f'Enter {n} elements (between 1 and {n + 1}): ')
arr = sorted(list(map(int, input().split())))

it = 0
recent = None
missing = None
while it < len(arr):
    if recent and recent + 1 != arr[it]:
        missing = recent + 1
        break
    else:
        recent = arr[it]
    it += 1

print(f'The missing number is: {missing}')