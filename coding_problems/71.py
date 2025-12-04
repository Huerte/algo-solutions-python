def pow_sum_dig_term(n):
    arr = []
    
    for i in range(2, 9 * len(str(n)) + 1):
        for j in range(2, 21):
            if sum(map(int, str(i ** j))) == i:
                arr.append(i ** j)
                
    return sorted(arr)[n-1]

print(pow_sum_dig_term(1))