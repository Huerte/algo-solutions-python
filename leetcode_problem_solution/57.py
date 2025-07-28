from collections import *
s1 = "aab"
s2 = "xxy"

k1 = [i for k, i in Counter(s1).items()]
k2 = [i for s, i in Counter(s2).items()]
print(k1, k2)

# def areRotations(s1, s2):
#     if len(s1) != len(s2):
#         return False
#
#     return s2 in (s1 + s1)

# print(areRotations("abcd", "cdab"))
# n = int(input())
# m = int(input())
#
# # Initialize the sequence with N-1 zeros and a 1
# a = [0] * (n - 1) + [1]
#
# # Generate the N-bonacci sequence up to the Mth term
# print(a)
# for i in range(n, m):
#     a.append(sum(a[-n:]))
#     print(a)
#
# print(a[m-1])  # Correct indexing: Mth term is at index M-1
