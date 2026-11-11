# HackerRank - Utopian Tree
# Problem: Utopian Tree
# Source: https://www.hackerrank.com/challenges/utopian-tree/problem
# Note: Calculates tree height after n growth cycles, doubling in spring and increasing by 1 in summer.
def utopianTree(n):
    res = 1
    for i in range(n):
        if i % 2 == 0:
            res *= 2
        else:
            res += 1
    return res
# Test cases
assert utopianTree(0) == 1
assert utopianTree(1) == 2
assert utopianTree(3) == 6
assert utopianTree(4) == 7
assert utopianTree(5) == 14

print("All test cases passed!")
