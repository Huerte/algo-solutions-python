# CodeWars - The Vowel Code

vowels = 'aeiou'

def encode(st):
    res = ''
    for c in st:
        if c in vowels:
            res += str(vowels.index(c) + 1)
        else:
            res += c
    return res

def decode(st):
    res = ''
    for c in st:
        if c.isdigit() and 0 < int(c) <= 5:
            res += vowels[int(c) - 1]
        else:
            res += c
    return res

print(encode('hello')) # h2ll4
print(encode('h2ll4')) # h2ll4
print(encode('How are you today?')) # H4w 1r2 y45 t4d1y?

print(decode('h2ll4')) # hello
print(decode('How are you today?')) # How are you today?
print(decode('H4w 1r2 y45 t4d1y?')) # How are you today?