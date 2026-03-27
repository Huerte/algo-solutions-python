# 📜 Problem — Changing Direction
# Description:
# Given a list of integers, count the number of times the direction changes from increasing to decreasing
# or vice versa. A direction change occurs when the sequence switches from going up to going down,
# or from going down to going up.
# 
# Example:
# - Input: [1, 2, 3, 2, 1] → Output: 1 (changes from increasing to decreasing at index 2)
# - Input: [1, 2, 3, 4, 5] → Output: 0 (always increasing)
# - Input: [1, 2, 2, 1, 2, 2] → Output: 2 (changes at index 2 and 3)
# 
# Status: ✅ SOLVED

def changing_direction(elements: list[int]) -> int:
    if len(elements) < 2:
        return 0

    count_turns = 0
    is_increasing = None

    for i in range(1, len(elements)):
        if elements[i] == elements[i - 1]:
            continue

        if is_increasing is None:
            is_increasing = elements[i] > elements[i - 1]
        elif (elements[i] > elements[i - 1] and not is_increasing) or (elements[i] < elements[i - 1] and is_increasing):
            is_increasing = not is_increasing
            count_turns += 1
    return count_turns

# Test cases with assertions
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
assert changing_direction([1, 2, 3, 5, 4, 2, 5, 7, 8, 3, 2, 1]) == 3
assert changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]) == 7

print("All test cases passed!")
