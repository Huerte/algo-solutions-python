# Permutation Sequence

from itertools import permutations
def kth_permutation(n, k):
    return f'"{list(map(lambda x: ''.join(x), permutations(''.join(map(str, range(1, n + 1))))))[k - 1]}"'

print(kth_permutation(3, 3))
print(kth_permutation(4, 9))
print(kth_permutation(3, 1))
