#Int to Words

def number_to_words(n):
    if n == 0:
        return 'zero'

    ones = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }

    teens = {
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen'
    }

    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
    }

    def to_word(num):
        temp = []
        if num >= 100:
            temp.append(ones[num // 100] + ' hundred')
            num %= 100
        if 10 <= num <= 19:
            temp.append(teens[num])
        else:
            if num >= 20:
                temp.append(tens[num // 10])
                num %= 10
            if 1 <= num <= 9:
                temp.append(ones[num])
        return ' '.join(temp)

    parts = []
    if n >= 1000:
        parts.append(to_word(n // 1000) + ' thousand')
        n %= 1000

    if n > 0:
        parts.append(to_word(n))

    return ' '.join(parts)











































assert number_to_words(0) == "zero"
assert number_to_words(1) == "one"
assert number_to_words(9) == "nine"
assert number_to_words(10) == "ten"
assert number_to_words(11) == "eleven"
assert number_to_words(15) == "fifteen"
assert number_to_words(19) == "nineteen"
assert number_to_words(20) == "twenty"
assert number_to_words(21) == "twenty one"
assert number_to_words(45) == "forty five"
assert number_to_words(99) == "ninety nine"

assert number_to_words(100) == "one hundred"
assert number_to_words(101) == "one hundred one"
assert number_to_words(115) == "one hundred fifteen"
assert number_to_words(120) == "one hundred twenty"
assert number_to_words(121) == "one hundred twenty one"
assert number_to_words(199) == "one hundred ninety nine"

assert number_to_words(200) == "two hundred"
assert number_to_words(305) == "three hundred five"
assert number_to_words(999) == "nine hundred ninety nine"

assert number_to_words(1000) == "one thousand"
assert number_to_words(1001) == "one thousand one"
assert number_to_words(1015) == "one thousand fifteen"
assert number_to_words(1100) == "one thousand one hundred"
assert number_to_words(1111) == "one thousand one hundred eleven"
assert number_to_words(2020) == "two thousand twenty"
assert number_to_words(4321) == "four thousand three hundred twenty one"
assert number_to_words(9999) == "nine thousand nine hundred ninety nine"
print("Problem Solved!!!")