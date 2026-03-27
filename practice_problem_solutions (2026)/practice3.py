# Count Integers with Even Number of Digits

n = int(input('Enter the number of integers: '))
arr = map(int, input("Enter the integers: ").split()[:n])
c = 0
for num in arr:
    if len(str(num)) % 2 == 0:
        c += 1
print(f"Count of integers with an even number of digits: {c}")