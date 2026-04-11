# py.checkio - Subject is Stressful

def is_stressful(subj: str) -> bool:
    if subj.isupper():
        return True
    elif subj[-3:] == '!!!':
        return True
    else:
        reds = ["help", "asap", "urgent"]
        
        for word in subj.lower().split():
            temp = ""
            for c in word:
                if c.isalpha():
                    if temp and c == temp[-1]:
                        continue
                    temp += c
            print(temp)
            for code in reds:
                if code in temp:
                    return True
    return False

print(is_stressful("Hi"))           # False
print(is_stressful("I need HELP"))  # True
print(is_stressful("I neeed HLEP")) # False