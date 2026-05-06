# CodeWars - Next bigger number with the same digits

def next_bigger(n):
    digits = list(str(n))
    
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i+1]:
        i -= 1
    
    if i == -1:
        return -1
    
    j = len(digits) - 1
    while j >= 0 and digits[j] <= digits[i]:
        j -= 1
    
    digits[i], digits[j] = digits[j], digits[i]
    
    digits[i+1:] = sorted(digits[i+1:])
    
    return int(''.join(digits))

print(next_bigger(2017))    # 2071
print(next_bigger(144))     # 414
print(next_bigger(12))      # 21