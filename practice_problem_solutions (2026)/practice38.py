# Keypad Phone Simulator

number_of_word = int(input())

res = []

keypad_coord = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': ' '
}


for _ in range(number_of_word):

    seq = input()
    word = ""
    cur = []

    for c in seq:
        if not cur:
            cur.append(c)
        elif c in cur:
            cur.append(c)
        else:
            if c == ' ':
                word += keypad_coord[cur[-1]][len(cur) - 1]
                cur = []
                continue
            word += keypad_coord[cur[-1]][len(cur) - 1]
            cur = [c]
    
    if cur:
        word += keypad_coord[cur[-1]][len(cur) - 1]
        
    res.append(word)

print('\n'.join(res))