def nearest_value(values: set[int], one: int) -> int:
    if len(values) == 1:
        return next(iter(values))
    elif one in values:
        return one

    values.add(one)
    values = sorted(values)

    one_index = 0
    while values[one_index] != one:
        one_index += 1

    if one_index == 0:
        return values[1]
    elif one_index == len(values) - 1:
        return values[-2]
    else:
        left = one - values[one_index - 1]
        right = values[one_index + 1] - one
        if left <= right:
            return values[one_index - 1]
        else:
            return values[one_index + 1]

print("Example:")
print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

assert nearest_value({17, 4, 7, 10, 11, 12}, 9) == 10
assert nearest_value({17, 4, 7, 10, 11, 12}, 8) == 7
assert nearest_value({17, 4, 8, 10, 11, 12}, 9) == 8
assert nearest_value({17, 4, 9, 10, 11, 12}, 9) == 9
assert nearest_value({17, 4, 7, 10, 11, 12}, 0) == 4
assert nearest_value({17, 4, 7, 10, 11, 12}, 100) == 17
assert nearest_value({100, 5, 8, 89, 10, 12}, 7) == 8
assert nearest_value({2, 3, -1}, 0) == -1
assert nearest_value({5}, 5) == 5
assert nearest_value({5}, 7) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")