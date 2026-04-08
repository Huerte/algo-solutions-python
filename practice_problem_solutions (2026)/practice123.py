# CodeWars - Mexican Wave

def wave(people):
    arr = []
    for i in range(len(people)):
        if not people[i].isalpha():
            continue
        temp = list(people)
        temp[i] = temp[i].upper()
        arr.append(''.join(temp))
    return arr

print(wave('hello')) # ['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']
print(wave('gap')) # ['Gap', 'gAp', 'gaP']
print(wave('two words')) # ['Two words', 'tWo words', 'twO words', 'two Words', 'two wOrds', 'two woRds', 'two worDs', 'two wordS']