# Count CamelCase Words

s = input('Enter the CamelCase string: ')

word = []

i = 0
while i < len(s):
    temp = ""
    if i == 0 and s[i].islower():
        temp += s[i]
        i += 1
        while i < len(s) and s[i].islower():
            temp += s[i]
            i += 1
        print(f'First Word: {temp}')
        word.append(temp)
    else:
        temp += s[i]
        i += 1
        while i < len(s) and s[i].islower():
            temp += s[i]
            i += 1
        print(f"Others: {temp}")
        word.append(temp)
print(len(word))