# HackerRank - Non-Divisible Subset

# Other Sol
def nonDivisibleSubset(k, s):
    freq = [0] * k
    for num in s:
        freq[num % k] += 1
    
    count = 0

    if freq[0] > 0:
        count += 1

    for i in range(1, k // 2 + 1):
        if i == k - i:
            if freq[i] > 0:
                count += 1
        else:
            count += max(freq[i], freq[k - i])
    
    return count


print(nonDivisibleSubset(7, list(map(int, "278 576 496 727 410 124 338 149 209 702 282 718 771 575 436".split())))) # 11