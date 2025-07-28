def missing_number(items: list[int]) -> int:
    items = sorted(items)
    step = (items[-1] - items[0]) // len(items)
    print(step)
    print(set(range(items[0], items[-1] + step, step)))

    expected = set(range(items[0], items[-1] + step, step)) - set(items)
    return list(expected)[0]


# These "asserts" are used for self-checking
assert missing_number([2, 6, 8]) == 4
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([1, 3, 7, 9]) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")