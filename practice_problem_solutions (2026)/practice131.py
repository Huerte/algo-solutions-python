# CodeWars - Title Case

def title_case(title, minor_words=''):
    result = []
    minors = [word.lower() for word in minor_words.split()]
    for i, word in enumerate(title.lower().split()):
        if word in minors and i > 0:
            result.append(word.lower())
        else:
            result.append(word.title())
            
    return ' '.join(result)

print(title_case("a clash of KINGS", "a an the of")) # "A Clash of Kings"
print(title_case("THE WIND IN THE WILLOWS", "The In")) # "The Wind in the Willows"
print(title_case("the quick brown fox")) # "The Quick Brown Fox"