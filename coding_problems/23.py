# 📜 Problem — Better Days
# Description:
# Given an array representing temperatures for n days, for each day find how many days 
# you have to wait until a warmer temperature. If there is no future day for which 
# this is possible, put 0 instead.
# This is similar to the "Daily Temperatures" problem.
#
# Input:
# - An array of integers `days` representing temperatures for each day
#
# Output:
# - An array where each element represents the number of days to wait for a warmer temperature
#
# Status: ✅ SOLVED

def betterDays(days):
    if not days:
        return []
        
    n = len(days)
    results = [0] * n
    
    for i in range(n):
        not_lucky = True
        for j in range(i + 1, n):
            if days[i] < days[j]:
                results[i] = j - i
                not_lucky = False
                break
        if not_lucky:
            results[i] = 0
    
    return results

# Test cases with assertions
# Example 1
days1 = [73, 74, 75, 71, 69, 72, 76, 73]
assert betterDays(days1) == [1, 1, 4, 2, 1, 1, 0, 0]

# Example 2
days2 = [30, 40, 50, 60]
assert betterDays(days2) == [1, 1, 1, 0]

# Example 3
days3 = [30, 60, 90]
assert betterDays(days3) == [1, 1, 0]

# Example 4
days4 = [70, 60, 50, 40]
assert betterDays(days4) == [0, 0, 0, 0]

# Edge cases
days5 = []
assert betterDays(days5) == []

days6 = [100]
assert betterDays(days6) == [0]

print("All test cases passed!")