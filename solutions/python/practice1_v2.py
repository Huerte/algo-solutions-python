# Problem: N-Queens II (bitmask optimization)
# Source: https://leetcode.com/problems/n-queens-ii/
# Note: Counts valid boards using bitmasks instead of scanning a 2D board.
#
# Optimization for issue #274:
# The original practice1.py checks rows, columns, and diagonals by scanning
# the board for every candidate position. This version represents occupied
# columns and diagonals as integer bitmasks, so each candidate set is computed
# with bitwise operations. It also avoids allocating and mutating an N x N board.
#
# Complexity: O(number of explored search states), with O(N) recursion space.
# The search is still backtracking, but each state performs constant-time
# bitmask operations rather than O(N) board scans per candidate.

def total_n_queens(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    full_mask = (1 << n) - 1

    def backtrack(columns, diagonals_left, diagonals_right):
        if columns == full_mask:
            return 1

        available = full_mask & ~(columns | diagonals_left | diagonals_right)
        count = 0

        while available:
            position = available & -available
            available ^= position
            count += backtrack(
                columns | position,
                ((diagonals_left | position) << 1) & full_mask,
                (diagonals_right | position) >> 1,
            )

        return count

    return backtrack(0, 0, 0)


if __name__ == "__main__":
    expected = {
        0: 1,
        1: 1,
        2: 0,
        3: 0,
        4: 2,
        5: 10,
        6: 4,
        7: 40,
        8: 92,
        9: 352,
        10: 724,
        11: 2680,
        12: 14200,
        13: 73712,
        14: 365596,
    }

    for size, answer in expected.items():
        assert total_n_queens(size) == answer

    try:
        total_n_queens(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative board sizes must be rejected")

    print("All N-Queens bitmask tests passed!")
