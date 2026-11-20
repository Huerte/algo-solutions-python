# Problem: Character Frequency Counter
# Source: Practice problem



from collections import Counter


def character_frequencies(text):
    frequencies = Counter(character for character in sorted(text.lower()) if character != " ")
    return [(character, count) for character, count in frequencies.items()]


if __name__ == "__main__":
    text = input()

    for character, count in character_frequencies(text):
        print(character, count, sep=": ")

    assert character_frequencies("aab C") == [("a", 2), ("b", 1), ("c", 1)]
    assert character_frequencies("   ") == []
