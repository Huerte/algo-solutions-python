# HackerRank - collections.Counter()
# Problem: collections.Counter()
# Source: https://www.hackerrank.com/challenges/collections-counter/problem
# Note: Tracks available shoe sizes and calculates total earnings from customer purchases.

from collections import Counter

x = int(input())
arr = Counter(list(map(int, input().split()[:x+1])))

total = 0
for _ in range(int(input())):
    size, prize = map(int, input().split())
    if arr[size] > 0:
        arr[size] -= 1
        total += prize

print(total)
