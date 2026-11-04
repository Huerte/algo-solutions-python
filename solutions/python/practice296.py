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
