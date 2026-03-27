# Check if Number is Same After Double Reversal

n = int(input('Enter an integer: '))
temp = n
for i in range(2):
    temp = int(str(temp)[::-1])

if temp == n:
    print(True)
else:
    print(False)