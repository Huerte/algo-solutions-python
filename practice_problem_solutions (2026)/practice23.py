# Buddy Strings Challenge

a = input('Enter string A: ')
b = input('Enter string B: ')

arr = list(a)

for i in range(len(arr)):
    for j in range(len(arr)):
        temp = arr.copy()
        if i == j:
            continue

        r = temp[i]
        temp[i] = temp[j]
        temp[j] = r

        if ''.join(temp) == b:
            print('true')
            import sys
            sys.exit(
                
            )

print('false')