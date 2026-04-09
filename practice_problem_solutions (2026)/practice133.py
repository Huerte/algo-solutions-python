# CodeWars - Data Reverse

def data_reverse(data):
    n = 8
    res = []
    
    i = 0
    for _ in range(len(data) // n):
        cur = []
        while i < len(data) and len(cur) < n:
            cur.append(data[i])
            i += 1
        res.append(cur)
    return [num for sublist in res[::-1] for num in sublist]

print(data_reverse([1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0])) # [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]
print(data_reverse([0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,0])) # [1,1,1,0,1,1,0,0,1,0,0,0,1,0,0,0]
print(data_reverse([1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0])) # [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0]