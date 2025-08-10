# 📜 Problem — Insert Interval
# Description:
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order
# by starti. You are also given an interval newInterval = [start, end] that represents the start
# and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by
# starti and intervals still does not have any overlapping intervals.
#
# Input:
# - intervals: A 2D integer array where 0 <= intervals.length <= 10^4
# - intervals[i].length == 2
# - 0 <= starti <= endi <= 10^5
# - newInterval: A list of 2 integers [start, end]
#
# Output:
# - A 2D integer array representing the intervals after insertion
#
# Status: ✅ SOLVED

def insert(intervals, newInterval):
    result = []
    i = 0
    
    # Add all intervals that come before newInterval
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    result.append(newInterval)
    
    # Add remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result

# Test cases with assertions
# Example 1
assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]

# Example 2
assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]

# Edge cases
assert insert([], [5,7]) == [[5,7]]
assert insert([[1,5]], [2,3]) == [[1,5]]
assert insert([[1,5]], [6,8]) == [[1,5],[6,8]]
assert insert([[1,5]], [0,0]) == [[0,0],[1,5]]

print("All test cases passed!")
