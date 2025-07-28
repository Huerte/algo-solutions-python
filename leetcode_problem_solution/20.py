s = input()
count = 1

for word in s:
    if not word.islower():
        count += 1
print(count)