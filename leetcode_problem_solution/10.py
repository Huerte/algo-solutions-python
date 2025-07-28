import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = input()

nums = x.split(' ')
rev_num = nums[0][::-1]
print(nums, rev_num)
result = ''

for num in rev_num:
    print(num)
    result += str(math.pow(int(num), int(nums[1])))
    print(result)

print(result)