# Problem: Pascal Triangle
# Source: https://leetcode.com/problems/pascals-triangle/

## Prints Pascal's Triangle with the number of rows entered by the user.
# Each row starts and ends with 1.
# The numbers in between are calculated using the previous number.
# Time Complexity: O(n²), where n is the number of rows.

n = int(input('Enter the number of rows: '))
for i in range(n):
    c = 1
    for j in range(i + 1):
        print(c, end=' ')
        c = c * (i - j) // (j + 1)
    print()