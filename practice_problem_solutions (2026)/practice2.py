# Clear Digits

s = input("Enter the string: ")

arr = []

for i in range(len(s)):
    if s[i].isdigit() and arr:
        arr.pop()
    else:
        arr.append(s[i])
print(''.join(arr))