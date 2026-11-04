# HackerRank - Word Order
# Problem: Word Order
# Source: https://www.hackerrank.com/challenges/word-order/problem
# Note: Counts the occurrences of distinct words while preserving their order of first appearance.
from collections import Counter
arr = [input() for _ in range(int(input()))]

counts = {}
for word in arr:
    counts[word] = counts.get(word, 0) + 1

print(len(counts))
print(' '.join(str(count) for count in counts.values()))
