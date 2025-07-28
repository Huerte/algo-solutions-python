# You are given a list of numbers.
# Find the absolute difference between each two numbers that are next to each other.
# Do this again and again on the new list, until only one number is left.
# Print that final number.
#
# Example:
# Input: 5
#        2 -4 9 9 -4
# Steps: [6 13 0 13] → [7 13 13] → [6 0] → [6]
# Output: 6

n = int(input())
arr = []
for i in input().split():
    arr.append(int(i))

while len(arr) != 1:
    temp = []
    for i in range(1, len(arr)):
        temp.append(abs(arr[i] - arr[i - 1]))
    arr = temp
    print(arr)
print(arr[0])