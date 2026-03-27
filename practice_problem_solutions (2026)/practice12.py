# Count Elements Smaller Than Current Element

n = int(input('Enter the number of elements: '))
print(f'Enter {n} integers:')
arr = [int(input()) for _ in range(n)]

res = [0] * len(arr)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if arr[i] < arr[j]:
            res[i] += 1

print(f'Results: {res}')