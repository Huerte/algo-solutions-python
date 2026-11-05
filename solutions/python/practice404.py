# Problem: Sum of Pairs
# Source: https://www.codewars.com/kata/54d81488b981293527000c8f
# Note: Finds the first pair of numbers, from left to right, that adds up to the target sum.
# CodeWars - Sum of Pairs
def sum_pairs(ints, s):
    
    seen = set()
    
    for num in ints:
        
        target = s - num
        
        if target in seen:
            return [target, num]
        
        seen.add(num)

print(sum_pairs([1, -2, 3, 0, -6, 1], -6)) # [0, -6]
print(sum_pairs([1, 4, 8, 7, 3, 15], 8))   # [1, 7]
print(sum_pairs([20, -13, 40], -7))        # None


if __name__ == "__main__":
    # Choose the pair with the earliest second index, not the earliest first index.
    assert sum_pairs([10, 5, 2, 3, 7, 5], 10) == [3, 7]

    # Negative values and zero are valid members of a pair.
    assert sum_pairs([1, -2, 3, 0, -6, 1], -6) == [0, -6]

    # Equal values require two separate entries.
    assert sum_pairs([5, 5], 10) == [5, 5]
    assert sum_pairs([5], 10) is None

    # Empty input cannot contain a pair.
    assert sum_pairs([], 0) is None
