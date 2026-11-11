# CodeWars - Sort arrays - 1
# Problem: Sort arrays - 1
# Source: https://www.codewars.com/kata/51f41b98e8f176e70d0002a8
# Note: Sorts an array of strings in lexicographical (alphabetical) order.
def sortme(names):
    return sorted(names, key=lambda x: (ord(x[0]), ord(x[1])))

print(sortme(["one", "two", "three"])) # ['one', 'three', 'two']
