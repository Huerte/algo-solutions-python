# py.checkio - Monkey Typing
# Problem: Monkey Typing
# Source: https://py.checkio.org/mission/monkey-typing/
# Note: Counts how many distinct words from the given set appear as substrings in the text, ignoring case.
def count_words(text: str, words: set) -> int:
    w = dict(zip([w.lower()for w in words], [0] * len(words)))
    print(w)
    for txt in text.lower().split():
        for word in words:
            if word.lower() in txt:
                w[word.lower()] += 1
    count = 0
    for k,v in w.items():
        if v > 0: count += 1
    return count

print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"})) # 2
