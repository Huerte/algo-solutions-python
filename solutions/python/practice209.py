# Problem: WeIrD StRiNg CaSe
# Source: https://www.codewars.com/kata/52b757663a95b11b3d00062d
# Note: Converts characters at even indices to uppercase and odd indices to lowercase, restarting the pattern for each word.
def to_weird_case(words):
    res = []
    for word in words.split():
        temp = []
        for i in range(len(word)):
            if i % 2 == 0:
                temp.append(word[i].upper())
            else:
                temp.append(word[i].lower())
        res.append(''.join(temp))
    return ' '.join(res)

print(to_weird_case('This'))           # 'ThIs'
print(to_weird_case('THIs iS a TEST')) # 'ThIs Is A TeSt'
print(to_weird_case('Weird string case')) # 'WeIrD StRiNg CaSe'
