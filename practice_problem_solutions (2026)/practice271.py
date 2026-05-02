# Vowel and Consonant

n = int(input()) # "àç_èç_è_(-'(çè_-çàà)ç_è(_-v çè- çàè_-ponctuation"
v, c = 0, 0
for i in range(n):
    text = input().lower()
    v += len([c for c in text if c in 'aeiou' and c.isalpha()])
    c += len([c for c in text if c not in 'aeiou' and 97 <= ord(c) < 123])
    print(v)
    print(c)
print(v * c)