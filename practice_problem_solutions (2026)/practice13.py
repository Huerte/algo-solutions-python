# Count Beautiful Days in a Range

st = int(input('Enter start: '))
end = int(input('Enter end: '))
div = int(input('Enter divisor: '))

res = 0

for i in range(st, end):
    temp = ((i - int(str(i)[::-1])) / div)
    if temp == int(temp):
        res += 1

print(f"The number of just right number is: {res}")