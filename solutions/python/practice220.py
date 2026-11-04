# CodeWars - Highest Rank Number in an Array
# Problem: Highest Rank Number in an Array
# Source: https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004
# Note: Returns the most frequent number in an array, choosing the largest number when frequencies are tied.
from collections import Counter
def highest_rank(arr):
    return max(set(arr), key=lambda x: (Counter(arr)[x], x))

print(highest_rank([1, 2, 3, 2, 1, 3, 3])) # 3
print(highest_rank([1, 1, 2, 2, 3])) # 2
print(highest_rank([1, 2, 3, 4, 5])) # 5
