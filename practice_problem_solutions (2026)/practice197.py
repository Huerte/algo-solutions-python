# HackerRank - Number Line Jumps

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