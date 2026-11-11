# Problem: Count Triplets
# Source: https://www.hackerrank.com/challenges/count-triplets-1/problem
# Note: Count partial triplets waiting for each next value in one left-to-right pass
# Time: O(n) expected, Space: O(n)


def countTriplets(arr, r):
    """Count index triples i < j < k with arr[j] = arr[i]*r and arr[k] = arr[j]*r."""
    waiting_second = {}
    waiting_third = {}
    total = 0

    for value in arr:
        # Only earlier indices may contribute to a triplet ending here.
        total += waiting_third.get(value, 0)
        next_value = value * r

        # Extend earlier single values into pairs waiting for their third value.
        pairs = waiting_second.get(value, 0)
        if pairs:
            waiting_third[next_value] = waiting_third.get(next_value, 0) + pairs

        # Register this value last so r = 1 never reuses the current index.
        waiting_second[next_value] = waiting_second.get(next_value, 0) + 1

    return total


if __name__ == "__main__":
    # Official examples.
    assert countTriplets([1, 2, 2, 4], 2) == 2
    assert countTriplets([1, 3, 9, 9, 27, 81], 3) == 6
    assert countTriplets([1, 5, 5, 25, 125], 5) == 4

    # Fewer than three elements cannot form a triplet, even when r = 1.
    assert countTriplets([1], 1) == 0
    assert countTriplets([1, 1], 1) == 0

    # Equal values must come from distinct indices.
    assert countTriplets([1, 1, 1], 1) == 1
    assert countTriplets([1, 1, 1, 1], 1) == 4
    assert countTriplets([5, 5, 7, 5, 7, 7], 1) == 2

    # Preserve input order and count each combination of duplicate indices.
    assert countTriplets([4, 2, 1], 2) == 0
    assert countTriplets([1, 2, 1, 2, 4], 2) == 3
    assert countTriplets([1, 1, 2, 2, 2, 4, 4], 2) == 12
    assert countTriplets([1, 2, 3, 5], 2) == 0

    # Large values and counts require exact integer arithmetic.
    assert countTriplets([1, 10_000, 100_000_000], 10_000) == 1
    assert countTriplets([1, 1_000_000_000, 1_000_000_000], 1_000_000_000) == 0
    assert countTriplets([1_000_000_000] * 3, 1) == 1
    assert countTriplets([1] * 100_000, 1) == 166_661_666_700_000

    print("All 16 test cases passed!")
