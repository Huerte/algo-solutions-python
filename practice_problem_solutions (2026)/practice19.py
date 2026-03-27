# Count Numbers with Unique Digits

n = int(input('Enter an integer: '))
ctr = 0
digits_range = int('9' * n)
for i in range(digits_range + 1):
    temp = str(i)
    if len(set(temp)) == len(temp):
        ctr += 1

print(f'Count of numbers with unique digits from 0 to {digits_range}: {ctr}')