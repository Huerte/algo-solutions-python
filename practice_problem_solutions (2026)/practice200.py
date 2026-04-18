
def punctuation_score(msg):
    punc = {
        '.': 2,
        '!': 5,
        '?': 10
    }

    t = 0
    i = 0

    while i < len(msg):
        if msg[i] in punc:
            cur = i

            while cur < len(msg) and msg[cur] in punc:
                cur += 1

            group_score = sum(punc[c] for c in msg[i:cur])

            t += group_score * (i + 1)

            i = cur
        else:
            i += 1

    return t

print(punctuation_score("I like to write multiple sentences. Don't you? Come on!")) # 805
print(punctuation_score("Hello world!"))                                            # 60
