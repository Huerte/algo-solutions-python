import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

number_of_lines = int(input())
nums = []
for i in range(number_of_lines):
    nums.append(input())
num = set(nums)
d = dict()
for i in num:
    d[i] = nums.count(i)
count = []
for n, i in d.items():
    count.append(i)
count = count[::-1]
result = ""
stop = False
while not stop:
    for index,( n, i )in enumerate(d.items()):
        if i == count[index]:
            result += f"{n} - {i}"
            del d[index]
        if index != len(d.items()):
            result += ', '
        elif index == len(d.items()):
            stop = True
            break

print(result)