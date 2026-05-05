def correct_polish_letters(st): 
    polish = {
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ź": "z",
        "ż": "z",
    }
    res = ""
    for c in st:
        res += polish.get(c, c)
    return res

print(correct_polish_letters("Maria Skłodowska-Curie"))  # "Maria Sklodowska-Curie"
print(correct_polish_letters("Jędrzej Błądziński"))      # "Jedrzej Bladzinski"
print(correct_polish_letters("Lech Wałęsa"))             # "Lech Walesa"