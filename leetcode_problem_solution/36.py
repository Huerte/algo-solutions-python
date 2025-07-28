a = [chr(i + 97) for i in range(0, 26)]

s = input().lower()
result = []
for i in range(len(s)):
    if i % 2 == 0:
        result.append(s[i])
    else:
        jump = int(s[i])
        result.append(chr(ord(s[i - 1]) + jump))
print("".join(result))