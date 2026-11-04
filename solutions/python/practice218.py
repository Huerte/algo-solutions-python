# CodeWars - Data Reverse
# Problem: Data Reverse
# Source: https://www.codewars.com/kata/569d488d61b812a0f7000015
# Note: Reverses the order of 8-bit data blocks while preserving the order of bits within each block.
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
