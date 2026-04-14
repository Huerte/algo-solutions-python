# Number of Islands

def islands(arr):
    island = 0

    for ar in arr:
        for num in ar:
            if num == '1':
                island += 1
    
    return island


print(islands([['1','0','1'], ['1','1','1'], ['1','0','1']]))