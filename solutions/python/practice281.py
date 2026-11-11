# HackerRank - Number Line Jumps
# Problem: Number Line Jumps
# Source: https://www.hackerrank.com/challenges/kangaroo/problem
# Note: Uses the difference in starting positions and jump distances to determine whether two kangaroos can meet at the same position after the same number of jumps.
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return 'YES' if x1 == x2 else 'NO'

    diff_pos = x2 - x1
    diff_vel = v1 - v2

    if diff_vel == 0:
        return 'NO'

    if diff_pos % diff_vel == 0 and diff_pos / diff_vel >= 0:
        return 'YES'

    return 'NO'
