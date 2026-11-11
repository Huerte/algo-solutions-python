# CodeWars - Mexican Wave
# Problem: Mexican Wave
# Source: https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
# Note: Generates a Mexican wave by capitalizing one alphabetic character at a time while preserving spaces.
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
