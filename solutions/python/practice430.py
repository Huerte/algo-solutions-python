# Problem: Ice Cream Parlor
# Source: https://www.hackerrank.com/challenges/icecream-parlor/problem
# Topic: Search, Hash Table

def icecream_parlor(m, arr):
    # stores cost -> 1-based index
    seen = {}
    for idx, cost in enumerate(arr, 1):
        target = m - cost
        if target in seen:
            return [seen[target], idx]
        seen[cost] = idx
    return []

# test cases from problem statement
assert icecream_parlor(4, [1, 4, 5, 3, 2]) == [1, 4]
assert icecream_parlor(4, [2, 2, 4, 3]) == [1, 2]
assert icecream_parlor(9, [1, 3, 4, 6, 7, 9]) == [2, 4]
assert icecream_parlor(8, [2, 1, 9, 4, 4, 56, 90, 3]) == [4, 5]
