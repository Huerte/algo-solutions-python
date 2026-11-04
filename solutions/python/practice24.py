# Problem: Equal Sides Of An Array
# Source: https://www.codewars.com/kata/5679aa472b8f57fb8c000047
# Note: Finds the lowest index where the sum of elements to the left equals the sum of elements to the right.

from math import floor
def find_even_index(arr):
    num = floor(len(arr) / 2)
    
    for i in range(num, 1, -1):
        if sum(arr[:i:]) == sum(arr[-i::]):
            return i
    
    if arr[0] == arr[-1]:
        return arr[0]
    
    return -1


print(find_even_index([1,2,3,4,3,2,1]))
