# Shift Odd-Indexed Characters

s = input('Enter the string: ')
res = []

pass_char = ""
for i in range(len(s)):
    if not res:
        res.append(s[i])
        pass_char = s[i]
        
    elif i % 2 != 0:
        res.append(chr(ord(pass_char) + int(s[i])))
    else:
        res.append(s[i])
        pass_char = s[i]

print(f'Transformed string: {''.join(res)}')