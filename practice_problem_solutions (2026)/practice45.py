# Insert Interval
# CONFUSE

def insert_interval(intervals, new_interval):
    
    res = []

    for interval in intervals:
        if interval[1] < new_interval[0]:
            res.append(interval)
        elif interval[0] > new_interval[1]:
            res.append(new_interval)
            new_interval = interval
        
        elif interval[1] >= new_interval[0] or interval[0] <= new_interval[1]:
            new_interval = [min(interval[0], new_interval[0]), max(interval[1], new_interval[1])]
    
    res.append(new_interval)
    
    return res


print(insert_interval([[1, 3], [6, 9]], [2, 5])) # == [[1, 5], [6, 9]]
print(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])) # == [[1, 2], [3, 10], [12, 16]]