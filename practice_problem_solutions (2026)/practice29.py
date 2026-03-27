# Rank Elements in an Array

n = int(input('Enter the number of elements: '))
print('Enter the elements: ', end='')
arr = list(map(int, input().split()))

rank = sorted(list(set(arr)))

res = []
for num in arr:
    res.append(rank.index(num) + 1)

print(f"Ranks: {' '.join(map(str, res))}")