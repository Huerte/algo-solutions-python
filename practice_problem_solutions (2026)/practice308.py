# CodeWars - Convert PascalCase string into snake_case

def to_underscore(strng: str) -> str:
    words = []
    temp = ""
    for c in str(strng):
        if c.isupper() and temp:
            words.append(temp)
            temp = c
        else:
            temp += c
    if temp:
        words.append(temp)
    
    return '_'.join(w.lower() for w in words)

print(to_underscore('MoviesAndBooks')) # 'movies_and_books'
print(to_underscore('TestController')) # 'test_controller'
print(to_underscore('App7Test'))       # 'app7_test'