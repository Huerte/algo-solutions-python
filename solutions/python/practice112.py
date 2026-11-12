# Problem: Count CamelCase Words
# Source: https://www.hackerrank.com/challenges/camelcase/problem
# Note: Walks the string once, starting a new word at each uppercase letter, and prints how many words were found

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