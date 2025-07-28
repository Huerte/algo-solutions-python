#equal and divisible pairs

def equalDivisiblePairs(loop, k):
    count_valid_pairs = 0
    arr = []
    for _ in range(loop):
        arr.append(int(input()))

    for i in range(len(arr)-1):
        for j in range(i + 1, len(arr)):
            if (arr[i] == arr[j]) and (i * j) % k == 0:
                count_valid_pairs += 1

    return count_valid_pairs

print(equalDivisiblePairs(4, 1))