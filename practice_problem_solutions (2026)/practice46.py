# Merge Intervals

def merge_intervals(intervals):

    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merge_intervals = [sorted_intervals[0]]

    for interval in sorted_intervals[1:]:
        if interval[0] <= merge_intervals[-1][1]:
            merge_intervals[-1] = [merge_intervals[-1][0], max(merge_intervals[-1][1], interval[1])]
        else:
            merge_intervals.append(interval)

    return merge_intervals

"""

[[1, 3]]

check -> [1, 3] == [2, 6] True

[[1, 6]]

check -> [1, 6] == [8, 10] False

[[1, 6], [8, 10]]

check -> [8, 10] == [15, 18] False

[[1, 6], [8, 10], [15, 18]]

end

"""

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])) # == [[1, 6], [8, 10], [15, 18]]
print(merge_intervals([[1, 4], [4, 5]])) # == [[1, 5]]