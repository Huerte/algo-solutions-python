# Most Frequent Even Element

n = int(input('Enter the number of integers: '))
print(f'Enter {n} integers:')

dis = {}

for _ in range(n):
    num = int(input())
    if num not in dis:
        dis[num] = 1
    else:
        dis[num] += 1

most_freq = [0, 0]
for key, value in dis.items():
    if key % 2 != 0:
        continue
    if value == most_freq[1]:
        most_freq[0] = min(most_freq[0], key)
    elif value > most_freq[1]:
        most_freq = [key, value]

print(f'Most frequent Even Element: {most_freq[0]}')