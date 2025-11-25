# Smallest possible sum

def solution(lst):
    arr = lst
    
    while len(set(arr)) != 1:
        highest, index = float('-inf'), 0
        for i, num in enumerate(arr):
            if num > highest:
                highest, index = num, i

        for num in arr:
            if num < highest:
                highest -= num
        
        arr[index] = highest 
        
    return sum(arr)

print(solution ([6, 9, 21]))