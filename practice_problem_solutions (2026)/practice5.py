# Find Strings Containing a Specific Character

n = int(input('Enter the number of strings: '))
print(f'Enter {n} strings:')
arr = []
for _ in range(n):
    arr.append(input())

s = input('Enter the character to search for: ')
print(f"Strings containing the character '{s}'")
for w in arr:
    if s in w:
        print(w)