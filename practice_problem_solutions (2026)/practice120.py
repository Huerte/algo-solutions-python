# HackerRank - Word Order

from collections import Counter
arr = [input() for _ in range(int(input()))]

counts = {}
for word in arr:
    counts[word] = counts.get(word, 0) + 1

print(len(counts))
print(' '.join(str(count) for count in counts.values()))