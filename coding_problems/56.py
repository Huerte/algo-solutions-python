# 📜 Problem — Merge Intervals
# Description:
# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping
# intervals that cover all the intervals in the input.
#
# Input:
# - intervals: A 2D integer array where 1 <= intervals.length <= 10^4
# - intervals[i].length == 2
# - 0 <= starti <= endi <= 10^4
#
# Output:
# - A 2D integer array representing the merged intervals
#
# Status: ✅ SOLVED

def merge(intervals):
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for interval in intervals[1:]:
        # If current interval overlaps with the last merged interval
        if interval[0] <= merged[-1][1]:
            # Merge the intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            # Add new interval
            merged.append(interval)
    
    return merged

# Test cases with assertions
# Example 1
assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

# Example 2
assert merge([[1,4],[4,5]]) == [[1,5]]

# Edge cases
assert merge([[1,4],[2,3]]) == [[1,4]]
assert merge([[1,4]]) == [[1,4]]
assert merge([]) == []
assert merge([[1,4],[5,6]]) == [[1,4],[5,6]]

print("All test cases passed!")