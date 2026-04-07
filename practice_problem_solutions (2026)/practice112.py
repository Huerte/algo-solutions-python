# Are they the "same"?

from collections import Counter
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    counter = Counter(array1)
    res = 0
    for key, rept in counter.items():
        i = 0
        temp = key ** 2
        found = 0
        while i < len(array2) and found < rept:
            if array2[i] == temp:
                found += 1
            i += 1
        res += found
    return res == len(array2)

print(comp([1, 2, 3, 2], \
           [1, 4, 9, 4])) # True
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361])) # True
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361])) # False
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736]))      # False
print(comp([1, 2, 3], [1, 9])) # False
print(comp([], [])) # True