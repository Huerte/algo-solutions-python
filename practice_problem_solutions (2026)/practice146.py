# CodeWars - Consonant Value

def solve(s):
    words = []
    temp = ""
    for c in s:
        if c in 'aeiou':
            words.append(temp)
            temp = ""
        else:
            temp += c
    words.append(temp)
    maxt = float('-inf')
    for word in words:
        maxt = max(maxt, sum(ord(c) - 96 for c in word))
    return maxt

print(solve("cozy"), 51)
print(solve("xyzzy"), 126)
print(solve("zodiac"), 26)
print(solve("chruschtschov"), 80)
print(solve("khrushchev"), 38)
print(solve("strength"), 57)
print(solve("catchphrase"), 73)
print(solve("twelfthstreet"), 103)
print(solve("mischtschenkoana"), 80)