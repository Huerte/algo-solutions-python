# Problem: Decode Ways
# Source: https://leetcode.com/problems/decode-ways/
# Topic: Dynamic Programming, String
# Status: IN PROGRESS

def decode(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        one = int(s[i-1:i])
        two = int(s[i-2:i])
        if one >= 1:
            dp[i] += dp[i-1]
        if 10 <= two <= 26:
            dp[i] += dp[i-2]
    return dp[n]

assert decode("12") == 2
assert decode("226") == 3
assert decode("06") == 0
assert decode("0") == 0
