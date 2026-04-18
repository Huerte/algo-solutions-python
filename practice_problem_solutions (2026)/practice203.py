# HackerRank - Counting Valleys

def countingValleys(steps, path):
    
    cur = 0
    val = 0
    for c in path:
        if cur < 0 and c == 'U':
            if cur + 1 == 0:
                val += 1
                cur += 1
                continue
        if c == 'U': cur += 1
        else: cur -= 1
    return val

print(countingValleys(8, "UDDDUDUU")) # 1