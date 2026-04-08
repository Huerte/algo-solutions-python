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