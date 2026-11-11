# HackerRank - Subarray Division
# Problem: Subarray Division (Birthday Chocolate)
# Source: https://www.hackerrank.com/challenges/the-birthday-bar/problem
# Note: Counts contiguous subarrays of length m whose sum equals d.
def birthday(s, d, m):
    count = 0
    
    for i in range(len(s)):
        cur = []
        for j in range(i, len(s)):
            if len(cur) < m:
                cur.append(s[j])
            else:
                break
        print(cur)
        if sum(cur) == d:
            count += 1
    
    return count

print(birthday([4], 4, 1)) # 1
