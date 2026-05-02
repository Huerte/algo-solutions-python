# HackerRank - Alternating Characters

def alternatingCharacters(s):
    seen = []
    count = 0
    for c in s:
        if seen and c == seen[-1]:
            count += 1
            continue
        seen.append(c)
    return count

print(alternatingCharacters('AAAA'))     # 3
print(alternatingCharacters('BBBBB'))    # 4
print(alternatingCharacters('ABABABAB')) # 0
print(alternatingCharacters('AAABBB'))   # 4