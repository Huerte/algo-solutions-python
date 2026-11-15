# Problem: Playing with Passphrases
# Source: https://www.codewars.com/kata/559536379512a64472000053
# Note: Shifts each word by its position and alternates the case of its letters.
# Status: ✅ Done
def play_pass(s, n):
    words = s.split(" ")
    transformed = []

    for word_index, word in enumerate(words):
        shift = (n * word_index) % 26
        result = []
        letter_index = 0

        for char in word:
            if char.isalpha() and char.isascii():
                base = ord("A") if char.isupper() else ord("a")
                shifted = chr((ord(char) - base + shift) % 26 + base)
                result.append(
                    shifted.upper() if letter_index % 2 == 0 else shifted.lower()
                )
                letter_index += 1
            else:
                result.append(char)

        transformed.append("".join(result))

    return " ".join(transformed)
