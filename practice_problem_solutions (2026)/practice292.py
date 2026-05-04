# CodeWars - Sort arrays - 1

def sortme(names):
    return sorted(names, key=lambda x: (ord(x[0]), ord(x[1])))

print(sortme(["one", "two", "three"])) # ['one', 'three', 'two']