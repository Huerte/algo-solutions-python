# Vowel Recognition
# Problem: Vowel Recognition
# Source: https://www.codewars.com/kata/5bed96b9a68c19d394000b1d
# Note: Calculates the total number of vowels across all possible substrings in linear time.

def vowel_recognition(s):
    vowels = set("aeiouAEIOU")
    count = 0
    n = len(s)
    for i, c in enumerate(s):
        if c in vowels:
            count += (i + 1) * (n - i)
    return count

print(vowel_recognition("aba")) # 6
print(vowel_recognition("abc")) # 3
