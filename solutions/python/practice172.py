# HackerRank - Maximize It!
# Problem: Maximize It!
# Source: https://www.hackerrank.com/challenges/maximize-it/problem
# Note: Finds the maximum modulo value of the sum of squares by selecting one element from each list.
k, m = map(int, input().split())

arr = []
for _ in range(k):
    temp = list(map(int, input().split()))
    x = temp[0]
    arr.append(temp[1:x+1])

result = [[]]

for lst in arr:
    new_comb = []
    for ar in result:
        for val in lst:
            new_comb.append(ar + [val])
    result = new_comb

cur_max = float('-inf')
for ar in result:
    temp = []
    for val in ar:
        temp.append(val ** 2)
    cur_max = max(cur_max, sum(temp) % m)

print(cur_max)
