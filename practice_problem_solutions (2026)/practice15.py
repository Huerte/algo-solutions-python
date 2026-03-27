# Calculate H-Index

n = int(input('Enter the number of papers: '))
print('Enter the number of citations for each paper:')
cit = list(map(int, input().split()))

res = 0

for i in range(n - 1, -1, -1):
    temp = 0
    for j in range(n):
        if cit[j] >= i:
            temp += 1
    if temp >= i:
        print(f"The researcher's h-index is: {temp}")
        break

