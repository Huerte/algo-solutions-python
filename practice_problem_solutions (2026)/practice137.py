# CodeWars - Playing with Passphrases

def play_pass(s, n):
    res = []
    
    for word in s.split():
        
        temp = []
        for c in word:
            if c.isalpha():
                temp.append(chr(ord(c) + n))
            elif c.isdigit():
                temp.append(str(abs(int(c) - 9)))
            else:
                temp.append(c)
        res.append(''.join(temp[::-1]))

    words = ' '.join(res)
    final = []
    temp = ""
    for i in range(len(words)):
        if words[i] == " ":
            final.append(temp)
            temp = ""
            continue
        if i % 2 == 0:
            temp += words[i].upper()
        else:
            temp += words[i].lower()
    final.append(temp)

    print(final)
    return ' '.join(final[::-1])

print(play_pass("I LOVE YOU!!!", 1)) # "!!!vPz fWpM J"
# print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2)) # "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO"
# print(play_pass("BOY! YOU WANTED TO SEE HIM? IT'S YOUR FATHER:-)", 15)) # ")-:gTwIpU GjDn h'iX ?bXw tTh dI StIcPl jDn !NdQ"