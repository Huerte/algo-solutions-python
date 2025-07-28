scrambled = "H!e ldllor ow"

result = ''
for i in range(0, len(scrambled), 2):
    result += scrambled[i]

for j in range(len(scrambled)-2, 0, -2):
    result += scrambled[j]

print(result)