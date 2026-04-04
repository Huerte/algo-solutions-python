# HackerRank - collections.Counter()

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