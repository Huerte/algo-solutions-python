#Reverse Every Ascending

def reverse_ascending(items):
    if not items:
        return []

    result = []
    temp = [items[0]]

    for k in range(1, len(items)):
        if items[k] > items[k - 1]:
            temp.append(items[k])
        else:
            if len(temp) > 1:
                result.extend(temp[::-1])
            else:
                result.extend(temp)
            temp = [items[k]]

    if len(temp) > 1:
        result.extend(temp[::-1])
    else:
        result.extend(temp)

    return result


print("Example:")
print(list(reverse_ascending([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []
assert list(reverse_ascending([1])) == [1]
assert list(reverse_ascending([1, 1])) == [1, 1]
assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
