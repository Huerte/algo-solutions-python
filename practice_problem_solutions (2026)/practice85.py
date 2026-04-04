# How Broke Are You?

def broke_count(exp):
    n = len(exp)
    i = 0
    count = 0
    while i < n:
        temp = 0
        if (n - i) >= 7:
            if all(j <= 10 for j in exp[i:i+7]):
                count += 1
                i += 7
                continue
        if (n - i) >=  3:
            if all(j <= 7 for j in exp[i:i+3]):
                count += 1
                i += 3
                continue
        if exp[i] <= 3:
            count += 1
        i += 1
    return count