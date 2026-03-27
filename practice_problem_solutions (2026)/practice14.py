# Days to Wait for a Luckier Day

n = int(input('Enter the number of days: '))
odd = list(map(int, input('Enter the odds of luck for each day:\n').split()))
print('Number of days to wait for a luckier day:\n')

for i in range(n - 1):
    temp = 0
    for j in range(i + 1, n):
        if odd[j] > odd[i]:
            temp = j - i
            break
    print(temp, end=' ')

    if i + 1 == n - 1:
        print(0)