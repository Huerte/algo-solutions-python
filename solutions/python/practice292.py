# HackerRank - Append and Delete
# Problem: Append and Delete
# Source: https://www.hackerrank.com/challenges/append-and-delete/problem
# Note: Checks whether one string can be converted into another using exactly k append and delete operations.
def appendAndDelete(s, t, k):
    i = 0
    while i < min(len(s), len(t)) and s[i] == t[i]:
        i += 1

    ops = (len(s) - i) + (len(t) - i)

    if k >= len(s) + len(t):
        return "Yes"

    if k >= ops and (k - ops) % 2 == 0:
        return "Yes"

    return "No"

print(appendAndDelete("hackerhappy", "hackerrank", 9)) # Yes
print(appendAndDelete("ashley", "ash", 2))             # No
print(appendAndDelete("ash", "ashley", 1))             # No
